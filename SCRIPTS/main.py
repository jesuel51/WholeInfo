# manage the whole workflow
# you have two options to run
#1. load the gfile, trpltout.nc and statefile.nc before running this script (recommendated)
#2. load the input.profiles and input.profiles.geo
if root['INPUTS'].has_key('statefile.nc'):
    # step 1, run the profiles_gen.py to generate the input.profiles
    print('Running Profiles_gen....')
    root['SCRIPTS']['profiles_gen.py'].run()
    print('Finished Profiles_gen!')
    # step 2, take the output of profiles_gen to be the input of TGYRO
    root['INPUTS']['input.profiles']=root['OUTPUTS']['Profiles_gen']['input.profiles'].duplicate()
    root['INPUTS']['input.profiles.geo']=root['OUTPUTS']['Profiles_gen']['input.profiles.geo'].duplicate()
# step 3, run the tgyro to generate the input.tglf, input.gyro and input.cgyro
print('Running TGYRO for input.tglf...')
root['SCRIPTS']['tgyro_tglf.py'].run()
print('Running TGYRO for input.gyro...')
root['SCRIPTS']['tgyro_gyro.py'].run()
print('Transforming the input.gyro to input.cgyro')
root['SCRIPTS']['inputgyro2cgyro.py'].run()
