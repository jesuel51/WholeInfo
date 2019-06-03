# prepare the input.tglf
p_tgyro=len(root['INPUTS']['input.tgyro']['DIR'])
# What are the input files
inputs=[(root['INPUTS']['input.profiles'],'input.profiles'),
#        (root['INPUTS']['input.profiles.geo'],'input.profiles.geo'),
        (root['INPUTS']['input.tgyro'],'input.tgyro')
	]
if root['INPUTS'].has_key('input.profiles.geo'):
    inputs.append((root['INPUTS']['input.profiles.geo'],'input.profiles.geo'))
##----------------------
### output
##----------------------
#outputs=[]
outputs=['out.tgyro.alpha',
         'out.tgyro.flux_e','out.tgyro.flux_i1','out.tgyro.flux_i2',
#'out.tgyro.flux_target',
         'out.tgyro.evo_ne','out.tgyro.evo_te','out.tgyro.evo_ti','out.tgyro.evo_er',
         'out.tgyro.evo_n1','out.tgyro.evo_n2',
         'out.tgyro.power_e','out.tgyro.power_i',
         'out.tgyro.profile','out.tgyro.profile_e','out.tgyro.profile_i1','out.tgyro.profile_i2',
#        'out.tgyro.mflux_e','out.tgyro.mflux_i','out.tgyro.mflux_i2',
         'out.tgyro.gyrobohm','out.tgyro.gradient',
         'out.tgyro.geometry.1','out.tgyro.nu_rho',
         'out.tgyro.residual','out.tgyro.control',
         'out.tgyro.geometry.2','out.tgyro.run',
         'input.profiles.gen','input.tgyro.gen'
         ]
if root['INPUTS']['input.tgyro']['LOC_N_ION'] == 3:
    outputs.append('out.tgyro.flux_i3')
    outputs.append('out.tgyro.profile3')
    outputs.append('out.tgyro.mflux_i3')
    outputs.append('out.tgyro.evo_n3')
DIR=root['INPUTS']['input.tgyro']['DIR']
for item in DIR.keys():
    del DIR[item]
for k in range(1,p_tgyro+1):
    DIR['TGLF'+str(k)]=1
    outputs.append('TGLF'+str(k)+'/out.tglf.localdump')
executable ='tglffolder;'
executable =executable + 'pbsMonitor '\
            +' -jq '+str(root['SETTINGS']['SETUP']['pbs_queue']) \
            +' -jn '+str(root['SETTINGS']['SETUP']['num_nodes']) \
            +' -cn '+str(root['SETTINGS']['SETUP']['num_cores']) \
            +' -wt '+str(root['SETTINGS']['SETUP']['wall_time']) \
            +' -exe '+' tgyro -e . -n ' + str(root['SETTINGS']['SETUP']['num_nodes']*root['SETTINGS']['SETUP']['num_cores'])

#-----------------------
# Execute ONETWO
#-----------------------
ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)

#-----------------------
# load the results
#-----------------------
for item in outputs[0:-p_tgyro]:
    root['OUTPUTS']['TGYRO'][item]=OMFITasciitable(item)
count=1
for item in outputs[-p_tgyro:]:
    root['OUTPUTS']['TGYRO']['TGLF']['out.tglf.localdump_'+str(count)]=OMFITgaCode(item)
    count=count+1
