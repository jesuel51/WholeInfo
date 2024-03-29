# plot the kinetic profiles and profile gradient
inputpro=root['INPUTS']['input.profiles']
inputtgyro=root['INPUTS']['input.tgyro']
rho=inputpro['rho']
p_tgyro=len(inputtgyro['DIR'])
rho_sparse=linspace(inputtgyro['TGYRO_RMIN'],inputtgyro['TGYRO_RMAX'],p_tgyro)
lw=2
aLTi=zeros([p_tgyro])
aLTe=zeros([p_tgyro])
aLne=zeros([p_tgyro])
s=zeros([p_tgyro])
tglfout=root['OUTPUTS']['TGYRO']['TGLF']
for k in range(1,p_tgyro+1):
    aLTi[k-1]=tglfout['out.tglf.localdump_'+str(k)]['RLTS_2']
    aLTe[k-1]=tglfout['out.tglf.localdump_'+str(k)]['RLTS_1']
    aLne[k-1]=tglfout['out.tglf.localdump_'+str(k)]['RLNS_1']
    s[k-1]=tglfout['out.tglf.localdump_'+str(k)]['SHAT_SA']
#find the max a/LT&a/Ln for better visualization
aLT_max=max([max(aLTi),max(aLTe),max(aLne)]);
aLT_max=floor(aLT_max)+1
aLT_min=min([min(aLTi),min(aLTe),min(aLne)]);
aLT_min=floor(aLT_min)
s_max=floor(max(s))+1
s_min=floor(min(s))
imatch=1; # 0: xlim 0~1; 1: xlim tgyro_rmin, tgyro_rmax
figure(figsize=[20,10])
fs1=24
fs2=20
fs3=16
T_max=int(max(inputpro['Ti_1'][0],inputpro['Te'][0]))+1
subplot(2,4,1)
plot(rho,inputpro['Ti_1'],'-b',linewidth=lw)
xlim([0,1])
ylim([0,T_max])
xticks([],fontsize=fs2)
yticks(fontsize=fs2)
title('$T_i(keV)$',fontsize=fs1,family='serif')
subplot(2,4,5)
plot(rho_sparse,aLTi,'-ko',linewidth=lw)
#plot(array([0,1]),array([0,0]),'--k',linewidth=lw/2)
plot(array([rho_sparse[0],rho_sparse[1]]),array([0,0]),'-ko',linewidth=lw/2)
if imatch==1:
    xlim([0,1])
    xticks(linspace(0,1.0,6),fontsize=fs2)
#ylim([0,4.5])
ylim([aLT_min,aLT_max])
xticks(fontsize=fs2)
yticks(fontsize=fs2)
xlabel('$\\rho$',fontsize=fs1,family='serif')
title('$a/L_{Ti}$',fontsize=fs1,family='serif')
subplot(2,4,2)
plot(rho,inputpro['Te'],'-b',linewidth=lw)
ylim([0,T_max])
xlim([0,1])
xticks([],fontsize=fs2)
yticks(fontsize=fs2)
title('$T_e(keV)$',fontsize=fs1,family='serif')
subplot(2,4,6)
plot(rho_sparse,aLTe,'-ko',linewidth=lw)
#ylim([0,4.5])
ylim([aLT_min,aLT_max])
#plot(array([0,1]),array([0,0]),'--k',linewidth=lw/2)
plot(array([rho_sparse[0],rho_sparse[1]]),array([0,0]),'--k',linewidth=lw/2)
if imatch==1:
    xlim([0,1])
    xticks(linspace(0,1.0,6),fontsize=fs2)
xticks(fontsize=fs2)
yticks(fontsize=fs2)
xlabel('$\\rho$',fontsize=fs1,family='serif')
title('$a/L_{Te}$',fontsize=fs1,family='serif')
subplot(2,4,3)
plot(rho,inputpro['ne'],'-b',linewidth=lw)
ylim([0,10])
#xlim([0,1])
xticks([],fontsize=fs2)
yticks(fontsize=fs2)
title('$n_e(10^{19}m^{-3})$',fontsize=fs1,family='serif')
subplot(2,4,7)
plot(rho_sparse,aLne,'-ko',linewidth=lw)
#ylim([0,4.5])
ylim([aLT_min,aLT_max])
#plot(array([0,1]),array([0,0]),'--k',linewidth=lw/2)
plot(array([rho_sparse[0],rho_sparse[1]]),array([0,0]),'--k',linewidth=lw/2)
if imatch==1:
    xlim([0,1])
    xticks(linspace(0,1.0,6),fontsize=fs2)
xticks(fontsize=fs2)
yticks(fontsize=fs2)
xlabel('$\\rho$',fontsize=fs1,family='serif')
title('$a/L_{ne}$',fontsize=fs1,family='serif')
subplot(2,4,4)
plot(rho,sign(inputpro['q'][-1])*inputpro['q'],'-b',linewidth=lw)
xlim([0,1])
ylim([int(min(abs(inputpro['q'])))-1,int(max(abs(inputpro['q'])))+1])
xticks([],fontsize=fs2)
yticks(fontsize=fs2)
title('q',fontsize=fs1,family='serif')
subplot(2,4,8)
plot(rho_sparse,s,'-ko',linewidth=lw)
#plot(array([rho_sparse[0],rho_sparse[1]]),array([0,0]),'--k',linewidth=lw/2)
plot(array([0,1]),array([0,0]),'--g',linewidth=lw/2)
#ylim([-1,3])
ylim([s_min,s_max])
if imatch==1:
    xlim([0,1])
    xticks(linspace(0,1.0,6),fontsize=fs2)
xticks(fontsize=fs2)
yticks(fontsize=fs2)
xlabel('$\\rho$',fontsize=fs1,family='serif')
title('s',fontsize=fs1,family='serif')
# plot some other important parameters,like BetaE, Collisionality
BetaE=zeros([p_tgyro])
Vu=zeros([p_tgyro])
for k in range(1,p_tgyro+1):
    BetaE[k-1]=tglfout['out.tglf.localdump_'+str(k)]['BETAE']
    Vu[k-1]=tglfout['out.tglf.localdump_'+str(k)]['XNUE']
figure(figsize=[10,6])
subplot(1,2,1)
plot(rho_sparse,BetaE,'-bo',linewidth=lw)
#xlim([0,1])
xticks(fontsize=fs3)
yticks(fontsize=fs3)
title('$\\beta_E$',fontsize=fs1,family='serif')
subplot(1,2,2)
semilogy(rho_sparse,Vu,'-bo',linewidth=lw)
#plot(rho_sparse,Vu,'-bo',linewidth=lw)
#xlim([0,1])
xticks(fontsize=fs3)
yticks(fontsize=fs3)
title('$\\nu$',fontsize=fs1,family='serif')
