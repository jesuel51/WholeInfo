# this script is used to plot the MTM frequency of different ky versus rho
# the input needs to be input.tgyro, input.profiles 
if not root['INPUTS'].has_key('input.profiles'):
    raise Exception('input.profiles must exist')
if not root['OUTPUTS']['TGYRO']['TGLF'].has_key('out.tglf.localdump_1'):
    root['SCRIPTS']['TGYRO_tglf.py'].run()
# plot the kinetic profiles and profile gradient
inputpro=root['INPUTS']['input.profiles']
inputtgyro=root['INPUTS']['input.tgyro']
rho=inputpro['rho']
p_tgyro=len(inputtgyro['DIR'])
rho_sparse=linspace(inputtgyro['TGYRO_RMIN'],inputtgyro['TGYRO_RMAX'],p_tgyro)
lw=2
#aLTi=zeros([p_tgyro])
aLTe=zeros([p_tgyro])
aLne=zeros([p_tgyro])
#s=zeros([p_tgyro])
tglfout=root['OUTPUTS']['TGYRO']['TGLF']
for k in range(1,p_tgyro+1):
#    aLTi[k-1]=tglfout['out.tglf.localdump_'+str(k)]['RLTS_2']
    aLTe[k-1]=tglfout['out.tglf.localdump_'+str(k)]['RLTS_1']
    aLne[k-1]=tglfout['out.tglf.localdump_'+str(k)]['RLNS_1']
#    s[k-1]=tglfout['out.tglf.localdump_'+str(k)]['SHAT_SA']
# dimension paramter calculation
Te_sparse=1.e3*interp(rho_sparse,inputpro['rho'],inputpro['Te'])
qe=1.6e-19;   # charge of a electron
mp=1.67e-27;  # mass of a proton
mass_ion=tglfout['out.tglf.localdump_1']['MASS_2']
#=SQRT(D38*H10/H12/E32)
cs=sqrt(Te_sparse*qe/mp/mass_ion/2.)
a=inputpro['rmin'][-1]
Bt=inputpro['BT_EXP']
qion=inputpro['IONS'][1][1]
ky=array([0.05,0.1,0.15])
#rho_s==H12*E32*C42/H10/E35/D32
rho_s=mp*2*mass_ion*cs/qe/Bt/qion
lenky=len(ky)
ky_dim=zeros([lenky,p_tgyro])
omega_nondim=zeros([lenky,p_tgyro])
omega_dim=zeros([lenky,p_tgyro])
for k in range(lenky):
    omega_nondim[k]=ky[k]*(aLne+aLTe)
    omega_dim[k]=ky[k]*(aLne+aLTe)*cs/a/2./pi/1.e3
    ky_dim[k]=ky[k]/rho_s
# plotprint('cs='c)
print('cs(km/s)=',cs/1.e3)
figure(figsize=[18,6])
lab=['-bo','-ro','-ko','-mo']
fs1=24
fs2=20
fs3=16
rct1=[0.1,0.15,0.2,0.6]
rct2=[0.4,0.15,0.2,0.6]
rct3=[0.7,0.15,0.2,0.6]
ax1=plt.axes(rct1)
#subplot(131)
for k in range(lenky):
    plot(rho_sparse,omega_nondim[k],lab[k],linewidth=lw,label=str(ky[k]))
#legend(loc=0,fontsize=fs3).draggable(True)
ylim([0,max(omega_nondim[lenky-1])*1.2])
xlabel('$\\rho$',fontsize=fs1,family='serif')
ylabel('w(cs/a)',fontsize=fs1,family='serif')
#xticks(fontsize=fs1,family='serif')
xticks(linspace(0.2,0.8,4),fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
#subplot(132)
ax2=plt.axes(rct2)
for k in range(lenky):
    plot(rho_sparse,omega_dim[k],lab[k],linewidth=lw,label=str(ky[k]))
ylim([0,max(omega_dim[lenky-1])*1.2])
legend(loc=0,fontsize=fs3).draggable(True)
xlabel('$\\rho$',fontsize=fs1,family='serif')
ylabel('w(kHz)',fontsize=fs1,family='serif')
#xticks(fontsize=fs1,family='serif')
xticks(linspace(0.2,0.8,4),fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
#subplot(133)
ax3=plt.axes(rct3)
for k in range(lenky):
    plot(rho_sparse,ky_dim[k]/100,lab[k],linewidth=lw,label=str(ky[k]))
#legend(loc=0,fontsize=fs3).draggable(True)
xlabel('$\\rho$',fontsize=fs1,family='serif')
xticks(linspace(0.2,0.8,4),fontsize=fs1,family='serif')
ylabel('$ky(rad/cm)$',fontsize=fs1,family='serif')
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
