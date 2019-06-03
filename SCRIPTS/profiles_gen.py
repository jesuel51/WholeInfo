##--------------------------
# What are the input files
##--------------------------
inputs=[(root['INPUTS']['statefile.nc'],'statefile.nc'),
        (root['INPUTS']['gfile'],'gfile'),
	]
##----------------------
### output
##----------------------
outputs=['input.profiles','input.profiles.geo']
executable ='profiles_gen -i statefile.nc -g gfile'
#-----------------------
# Execute Profile_gen
#-----------------------
ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)
#-----------------------
# load the results
#-----------------------
root['OUTPUTS']['Profiles_gen']['input.profiles']=OMFITgaCode('input.profiles')
root['OUTPUTS']['Profiles_gen']['input.profiles.geo']=OMFITgaCode('input.profiles.geo')
# determine whether to generate the Er profile in the input.profiles
if root['SETTINGS']['PHYSICS']['iGenEr']==1:
    inputs=[root['OUTPUTS']['Profiles_gen']['input.profiles'],'input.profiles']
    executable ='pbsMonitor -jq short -wt 00:30:00 -cn 8 -exe profiles_gen -vgen -i input.profiles -er 2 -vel 1 -in DC -ix 2'
    ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)
    root['OUTPUTS']['Profiles_gen']['input.profiles']=OMFITgaCode('vgen/input.profiles')
