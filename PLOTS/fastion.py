# this script is used to read the fast ions from the input.profiles
# with the fast ions density and it's pressure, specifically,compared witht he telectron density and total pressure
inputpro=root['INPUTS']['input.profiles']
n_ion=inputpro['N_ION']
n_exp=inputpro['N_EXP']
denpro=zeros([n_ion+1,n_exp])
tempro=zeros([n_ion+1,n_exp])
denpro[0]=inputpro['ne']
tempro[0]=inputpro['Te']
for k in arange(n_ion)+1:
    denpro[k]=inputpro['ni_'+str(k)]
    tempro[k]=inputpro['Ti_'+str(k)]
# the last ions species is treated to be fast ions by default
ntpro=sum(denpro*tempro,0)  # the profile of n*T sumed over all species
ntfastpro=denpro[n_ion]*tempro[n_ion]
pres=inputpro['ptot']
pres_fast=pres*ntfastpro/ntpro
# start to plot
rho=inputpro['rho']
fs1=24
fs2=20
figure('fast ions info',figsize=[12,8])
subplot(1,2,1)
plot(rho,inputpro['ne'],'-b',linewidth=2,label='ne')
plot(rho,10*inputpro['ni_'+str(n_ion)],'-r',linewidth=2,label='10*$n_{fast}$')
xticks(fontsize=fs2,family='serif')
yticks(fontsize=fs2,family='serif')
title('density',fontsize=fs1,family='serif')
ylabel('$10^19m^{-3}$',fontsize=fs2,family='serif')
xlabel('$\\rho$',fontsize=fs2,family='serif')
legend(loc=0,fontsize=fs2).draggable(True)
subplot(1,2,2)
plot(rho,inputpro['ptot']/1.e3,'-b',linewidth=2,label='$p_{tot}$')
plot(rho,pres_fast/1.e3,'-r',linewidth=2,label='$p_{fast}$')
xticks(fontsize=fs2,family='serif')
yticks(fontsize=fs2,family='serif')
title('pressure',fontsize=fs1,family='serif')
ylabel('kpa',fontsize=fs2,family='serif')
xlabel('$\\rho$',fontsize=fs2,family='serif')
legend(loc=0,fontsize=fs2).draggable(True)
