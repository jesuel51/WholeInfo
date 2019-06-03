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
outputs=[]
DIR=root['INPUTS']['input.tgyro']['DIR']
for item in DIR.keys():
    del DIR[item]
for k in range(1,p_tgyro+1):
    DIR['GYRO'+str(k)]=1
    outputs.append('GYRO'+str(k)+'/out.gyro.localdump')
executable ='gyrofolder;'
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
count=1
for item in outputs[-p_tgyro:]:
    root['OUTPUTS']['TGYRO']['GYRO']['out.gyro.localdump_'+str(count)]=OMFITgaCode(item)
    count=count+1
