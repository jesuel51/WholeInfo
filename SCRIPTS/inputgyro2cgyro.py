# this script is used to transform the input.gyro to input.cgyro
p_tgyro=len(root['INPUTS']['input.tgyro']['DIR'])
for m in arange(1,14):
    pathcgyro='/home/jianx/testrun/cgyro/reg01/'  # path of reg01
    root['OUTPUTS']['TGYRO']['CGYRO']['input.cgyro_'+str(m)]=OMFITgaCode(pathcgyro+'input.cgyro')
    inputcgyro=root['OUTPUTS']['TGYRO']['CGYRO']['input.cgyro_'+str(m)]
    inputgyro=root['OUTPUTS']['TGYRO']['GYRO']['out.gyro.localdump_'+str(m)]
    inputcgyro['EQUILIBRIUM_MODEL']=2
    inputcgyro['RMIN']=inputgyro['RADIUS']
    inputcgyro['RMAJ']=inputgyro['ASPECT_RATIO']
    inputcgyro['SHIFT']=inputgyro['SHIFT']
    inputcgyro['KAPPA']=inputgyro['KAPPA']
    inputcgyro['S_KAPPA']=inputgyro['S_KAPPA']
    inputcgyro['DELTA']=inputgyro['DELTA']
    inputcgyro['S_DELTA']=inputgyro['S_DELTA']
    inputcgyro['ZETA']=inputgyro['ZETA']
    inputcgyro['S_ZETA']=inputgyro['S_ZETA']
    inputcgyro['ZMAG']=inputgyro['ZMAG']
    inputcgyro['DZMAG']=inputgyro['DZMAG']
    # magnetic profile
    inputcgyro['Q']=inputgyro['SAFETY_FACTOR']
    inputcgyro['S']=inputgyro['SHEAR']
    inputcgyro['BTCCW']=inputgyro['BTCCW']
#    inputcgyro['IPCCW']=inputgyro['IPCCW']
    inputcgyro['IPCCW']=-1
    inputcgyro['UDSYMMETRY_FLAG']=inputgyro['UDSYMMETRY_FLAG']
    # control parameters, use the default
    #### not listed here
    # fields
    inputcgyro['N_FIELD']=inputgyro['N_FIELD']
    inputcgyro['BETAE_UNIT']=inputgyro['BETAE_UNIT']
    inputcgyro['BETA_STAR_SCALE']=inputgyro['GEO_BETAPRIME_SCALE']  
    # numerical resolution, use the default 
    # numerical dissipation, use the default
    # time stepping, use the default,
    # collisions model, use the default 
    inputcgyro['NU_EE']=inputgyro['NU_EI']
    # species, first ions and then electrons
    # determine how many ion species
    n_ion=1
    while (1):
        n_ion=n_ion+1
        if inputgyro['NI_OVER_NE_'+str(n_ion)]==0.:
            n_ion=n_ion-1
            n_s=n_ion+1
            break
    inputcgyro['N_SPECIES']=n_s
    inputcgyro['Z_1']=inputgyro['Z']
    inputcgyro['MASS_1']=1./inputgyro['MU']**2
    inputcgyro['DENS_1']=inputgyro['NI_OVER_NE']
    inputcgyro['TEMP_1']=inputgyro['TI_OVER_TE']
    inputcgyro['DLNNDR_1']=inputgyro['DLNNDR']
    inputcgyro['DLNTDR_1']=inputgyro['DLNTDR']
    for k in arange(n_ion-1)+2:
        inputcgyro['Z_'+str(k)]=inputgyro['Z_'+str(k)]
        inputcgyro['MASS_'+str(k)]=1./inputgyro['MU_'+str(k)]**2
        inputcgyro['DENS_'+str(k)]=inputgyro['NI_OVER_NE_'+str(k)]
        inputcgyro['TEMP_'+str(k)]=inputgyro['TI_OVER_TE_'+str(k)]
        inputcgyro['DLNNDR_'+str(k)]=inputgyro['DLNNDR_'+str(k)]
        inputcgyro['DLNTDR_'+str(k)]=inputgyro['DLNTDR_'+str(k)]
    inputcgyro['Z_'+str(n_s)]=-1
    inputcgyro['MASS_'+str(n_s)]=1./inputgyro['MU_ELECTRON']**2
    inputcgyro['DENS_'+str(n_s)]=1
    inputcgyro['TEMP_'+str(n_s)]=1
    inputcgyro['DLNNDR_'+str(n_s)]=inputgyro['DLNNDR_ELECTRON']
    inputcgyro['DLNTDR_'+str(n_s)]=inputgyro['DLNTDR_ELECTRON']
    # rotation physics
    inputcgyro['GAMMA_E']=inputgyro['GAMMA_E']
    inputcgyro['GAMMA_P']=inputgyro['PGAMMA']
    inputcgyro['MACH']=inputgyro['MACH']
    inputcgyro['GAMMA_P_SCALE']=inputgyro['PGAMMA_SCALE']
    inputcgyro['MACH_SCALE']=inputgyro['MACH_SCALE']  
    inputcgyro['COLLISION_MODEL']=4
