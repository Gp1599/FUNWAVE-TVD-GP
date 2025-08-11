import numpy as np
import matplotlib.pyplot as plt
#clear all

foldname =      'st_360_av_240'
fdir_results =  '/Volumes/DISK_2020_5/OceanBeach_onyx/PlaneBeach_' + foldname + '/'
fdir_curr =     '/Users/fengyanshi/WORK/papers/zhang_etal_2022/idealized_beach/'
fdir = "../../../simulationRuns/single_crest_radiation/output/"
# st means start averaging, av means averaging interval
# in /PlaneBeach_st_360_av_240/ use output number 2,3, looks great to represent small sxx along node

m = 960
n = 480

dx = 2.0
x = np.arange(0, m) * dx
y = np.arange(0, n) * dx
[X, Y] = np.meshgrid(x, y)

xshift = -m * 2
yshift = -n + 20.0 - 318

X = X + xshift
Y = Y + yshift
x = x + xshift
y = y + yshift

icount = 0

SHsig = np.zeros((n, m))
Setamean = np.zeros((n, m))
Sum = np.zeros((n, m))
Svm = np.zeros((n, m))
SDxSxx = np.zeros((n, m))
SDySxy = np.zeros((n, m))
SPgrdX = np.zeros((n, m))
SFRCX = np.zeros((n, m))
SDxUUH = np.zeros((n, m))
SDyUVH = np.zeros((n, m))
SDySyy = np.zeros((n, m))
SDxSxy = np.zeros((n, m))
SPgrdY = np.zeros((n, m))
SFRCY = np.zeros((n, m))
SDxUVH = np.zeros((n, m))
SDyVVH = np.zeros((n, m))

ncount = 0
for numb in range(2, 3):
    ncount = ncount + 1

    #eval('cd ' + fdir_results)
    fnum = '%.5d' % numb

    fname = fdir + 'eta_' + fnum
    #fileID = open(fname);
    eta = np.loadtxt(fname) #eta = fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    eta = np.transpose(eta)

    fname = fdir + 'Hsig_' + fnum
    #fileID = open(fname)
    #Hsig = fread(fileID,DimsX{1},'*single');
    #fileID.close()
    Hsig = np.loadtxt(fname)
    Hsig = np.transpose(Hsig)
    SHsig = SHsig + Hsig

    fname = fdir + 'etamean_' + fnum
    #fileID = fopen(fname);
    #etamean = fread(fileID,DimsX{1},'*single');
    #fclose(fileID)
    etamean = np.loadtxt(fname)
    etamean = np.transpose(etamean)
    Setamean = Setamean + etamean

    fname = fdir + 'umean_' + fnum
    #fileID = fopen(fname);
    #um=fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    um = np.loadtxt(fname)
    um = np.transpose(um)
    Sum = Sum + um

    fname = fdir + 'vmean_' + fnum
    #fileID=fopen(fname);
    #vm=fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    vm = np.loadtxt(fname)
    vm = np.transpose(vm)
    Svm = Svm + vm

    #% x -direction ----------

    fname = fdir + 'DxSxx_' + fnum
    #fileID = fopen(fname);
    #DxSxx=fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    DxSxx = np.loadtxt(fname)
    DxSxx = np.transpose(DxSxx)
    SDxSxx = SDxSxx + DxSxx

    fname = fdir + 'DySxy_' + fnum
    #fileID=fopen(fname);
    #DySxy=fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    DySxy = np.loadtxt(fname)
    DySxy = np.transpose(DySxy)
    SDySxy = SDySxy + DySxy

    fname = fdir + 'PgrdX_' + fnum
    #fileID=fopen(fname);
    #PgrdX=fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    PgrdX = np.loadtxt(fname)
    PgrdX = np.transpose(PgrdX)
    SPgrdX = SPgrdX + PgrdX


    fname = fdir + 'FRCX_' + fnum
    #fileID=fopen(fname);
    #FRCX=fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    FRCX = np.loadtxt(fname)
    FRCX = np.transpose(FRCX)
    SFRCX = SFRCX + FRCX

    fname = fdir + 'DxUUH_' + fnum
    #fileID=fopen(fname);
    #DxUUH=fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    DxUUH = np.transpose(DxUUH)
    SDxUUH = SDxUUH + DxUUH

    fname = fdir + 'DyUVH_' + fnum
    #fileID=fopen(fname);
    #DyUVH=fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    DyUVH = np.loadtxt(fname)
    DyUVH = np.transpose(DyUVH)
    SDyUVH = SDyUVH + DyUVH

    #% y -direction ----------

    fname = fdir + 'DySyy_' + fnum
    #fileID=fopen(fname);
    #DySyy=fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    DySyy = np.loadtxt(DySxy)
    DySyy = np.transpose(DySyy)
    SDySyy = SDySyy + DySyy

    fname = fdir + 'DxSxy_' + fnum
    #fileID=fopen(fname);
    #DxSxy=fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    DxSxy = np.loadtxt(fname)
    DxSxy = np.transpose(DxSxy)
    SDxSxy = SDxSxy + DxSxy

    fname = fdir + 'PgrdY_' + fnum
    #fileID=fopen(fname);
    #PgrdY=fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    PgrdY = np.loadtxt(fname)
    PgrdY = np.transpose(PgrdY)
    SPgrdY = SPgrdY + PgrdY

    fname = fdir + 'FRCY_' + fnum
    #fileID=fopen(fname);
    #FRCY=fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    FRCY = np.loadtxt(fname)
    FRCY = np.transpose(FRCY)
    SFRCY = SFRCY + FRCY

    fname = fdir + 'DyVVH_' + fnum
    #fileID=fopen(fname);
    #DyVVH=fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    DyVVH = np.loadtxt(fname)
    DyVVH = np.transpose(DyVVH)
    SDyVVH = SDyVVH + DyVVH

    fname = fdir + 'DxUVH_' + fnum
    #fileID=fopen(fname);
    #DxUVH=fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    DxUVH = np.loadtxt(fname)
    DxUVH = np.transpose(DxUVH)
    SDxUVH = SDxUVH + DxUVH

#% avg
Hsig = SHsig / ncount
etam = Setamean / ncount
um = Sum / ncount
vm = Svm / ncount
DxSxx = SDxSxx / ncount
DySxy = SDySxy / ncount
PgrdX = SPgrdX / ncount
FRCX = SFRCX / ncount
DxUUH = SDxUUH / ncount
DyUVH = SDyUVH / ncount
DySyy = SDySyy / ncount
DxSxy = SDxSxy / ncount
PgrdY = SPgrdY / ncount
FRCY = SFRCY / ncount
DxUVH = SDxUVH / ncount
DyVVH = SDyVVH / ncount

#From: https://www.mathworks.com/help/matlab/ref/curl.html#mw_1bfbc405-c17b-403d-ac3f-4398eeb41a8c
def curl(x, y, XX, YY, U, V):
    # 
    dX = np.zeros((np.shape(XX)))
    dY = np.zeros((np.shape(XX)))

    dY[0, :]                = (U[1, :] - U[0, :]) / (y[1] - y[0])
    dY[len(XX) - 1, :]      = (U[len(XX) - 1, :] - U[len(XX) - 2, :]) / (y[len(XX) - 1] - y[len(XX) - 2])

    dX[:, 0]                = (V[:, 1] - V[:, 0]) / (x[1] - x[0])
    dY[:, len(XX[0]) - 1]   = (V[:, len(XX[0]) - 1] - V[:, len(XX[0]) - 2]) / (x[len(XX[0]) - 1] - x[len(XX[0]) - 2])

    for j in range(1, len(XX) - 1):
        for i in range(1, len(XX[0]) - 1):
            dX[:, i] = (V[:, i + 1] - V[:, i + 1]) / (x[i + 1] - x[i - 1])
            dY[j, :] = (U[j + 1, :] - U[j - 1, :]) / (y[j + 1] - y[j - 1])

    return dX - dY

vort = curl(x, y, X, Y, um, vm)

#% --------- residual
Rx = DxSxx + DySxy + PgrdX + FRCX + DxUUH + DyUVH
Ry = DySyy + DxSxy + PgrdY + FRCY + DyVVH + DxUVH

#% ---------

eval('cd ' + fdir_curr)


nn2 = 390 #;  % anti
nn1 = 370 #;  % middle
nn3 = 350 #;  % node 

mm1 = 950
mm2 = 900
mm3 = 800
mm4 = 625

yy1 = Y(nn2, 1)
yy2 = Y(nn1, 1)
yy3 = Y(nn3, 1)

xx1 = X(1, mm1)
xx2 = X(1, mm2)
xx3 = X(1, mm3)
xx4 = X(1, mm4)

ax1 = [-700, 0, -225, 175]
txt_x = -650
txt_y = 150


#clf
figure_w = 8.0
figure_l = 10.0

fig = plt.figure(1, (figure_w, figure_l))
#%set(fig,'units','inches','paperunits','inches','papersize',...
#%    [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);
#colormap jet
#t = tiledlayout(2,2,'TileSpacing','Compact','Padding','Compact')
#nexttile
plt.pcolormesh(X, Y, eta) #,shading interp

plt.axis(ax1)
#hold on
plt.plot([-748, -748], [-500, 500], 'k', linewidth = 2)
ht = plt.text(-700,-100,'slope toe', rotation = 90, fontsize = 14, color = 'k')
#%set(ht,'Rotation',)
#%set(ht,'FontSize',14)
#%set(ht,'Color','k')
plt.plot([-1000, 0],[yy1, yy1],'w-','LineWidth',2)
plt.plot([-1000, 0],[yy2, yy2],'w-','LineWidth',2)
plt.plot([-1000, 0],[yy3, yy3],'w-','LineWidth',2)

plt.plot([xx1, xx1],[-1000, 1000],'w--','LineWidth',2)
plt.plot([xx2, xx2],[-1000, 1000],'w--','LineWidth',2)
plt.plot([xx3, xx3],[-1000, 1000],'w--','LineWidth',2)
plt.plot([xx4, xx4],[-1000, 1000],'w--','LineWidth',2)

plt.text(-250,17,'X 1')
#%text(-180,-27,'Prof 2')
plt.text(-250,-70,'X 2')


plt.text(xx1-35,75,'Y4')
plt.text(xx2-35,75,'Y3')
plt.text(xx3-20,75,'Y2')
plt.text(xx4-20,75,'Y1')

#%xlabel('x (m)')
plt.ylabel('y (m)')
plt.text(txt_x, txt_y, '(a)','Color','w','FontSize',14)

cbar = plt.colorbar()
cbar.ax.set_ylabel("\eta (m)") #set(get(cbar,'ylabel'),'String','\eta ( m ) ')
cbar.ax.axis([-0.9, 1.9, 0, 1])

#set(gca, 'LineWidth',  1)

#nexttile
plt.pcolormesh(X, Y, Hsig) #,shading interp
vbh = np.arange(0.0, 3.0, 1.0)
plt.contourf(X,Y,Hsig,np.arange(0, 3, 0.1)) #,shading interp
#caxis([0 3.0])
plt.axis(ax1)
#hold on
#%plot([-1000 0],[yy2 yy2],'w-','LineWidth',2)
plt.plot([-1000, 0],[yy1,   yy1],   'w-',   linewidth = 2)
plt.plot([-1000, 0],[yy3,   yy3],   'w-',   linewidth = 2)
plt.plot([xx1, xx1],[-1000, 1000],  'w--',  linewidth = 2)
plt.plot([xx2, xx2],[-1000, 1000],  'w--',  linewidth = 2)
plt.plot([xx3, xx3],[-1000, 1000],  'w--',  linewidth = 2)
plt.plot([xx4, xx4],[-1000, 1000],  'w--',  linewidth = 2)

#%xlabel('x (m)')
#%ylabel('y (m)')
cbar = plt.colorbar()
cbar.ax.set_xlabel("wave height (m)") #set(get(cbar,'xlabel'),'String','wave height ( m ) ')
plt.text(txt_x, txt_y, '(b)','Color','w','FontSize',14)

#nexttile
vb = np.concatenate(arrays = [np.arange(-0.2, -0.02, 0.03), np.arange(0.01, 0.1, 0.03), np.arange(0.1, 0.3, 0.02)])

plt.contourf(X, Y, etam, vb) #,shading interp
#caxis([-0.3 0.3])
plt.axis(ax1)
#hold on
#%plot([-1000 0],[yy2 yy2],'w-','LineWidth',2)
plt.plot([-1000, 0],[yy1,   yy1],   'w-',   linewidth = 2)
plt.plot([-1000, 0],[yy3,   yy3],   'w-',   linewidth = 2)
plt.plot([xx1, xx1],[-1000, 1000],  'w--',  linewidth = 2)
plt.plot([xx2, xx2],[-1000, 1000],  'w--',  linewidth = 2)
plt.plot([xx3, xx3],[-1000, 1000],  'w--',  linewidth = 2)
plt.plot([xx4, xx4],[-1000, 1000],  'w--',  linewidth = 2)
plt.text(txt_x, txt_y, '(c)','Color','k','FontSize',14)

plt.xlabel('x (m)')
plt.ylabel('y (m)')
cbar = plt.colorbar()
cbar.ax.set_xlabel("setup (m)") #set(get(cbar,'xlabel'),'String','setup ( m ) ')

#set(gca, 'LineWidth',  1)

#nexttile
plt.pcolormesh(X, Y, vort) #,shading interp
#hold on
sk = 8
sc = 50
plt.quiver(X[1:len(X):sk,1:len(X[0]):sk], Y[1:len(Y):sk, 1:len(Y[0]):sk], um[1:len(um):sk, 1:len(um[0]):sk] * sc, vm[1:len(vm):sk,1:len(vm[0]):sk] * sc,0)
plt.axis(ax1)
#%plot([-1000 0],[yy2 yy2],'w-','LineWidth',2)
plt.plot([-1000, 0],[yy1, yy1],'w-','LineWidth',2)
plt.plot([-1000, 0],[yy3, yy3],'w-','LineWidth',2)
plt.plot([xx1, xx1],[-1000, 1000],'w--','LineWidth',2)
plt.plot([xx2, xx2],[-1000, 1000],'w--','LineWidth',2)
plt.plot([xx3, xx3],[-1000, 1000],'w--','LineWidth',2)
plt.plot([xx4, xx4],[-1000, 1000],'w--','LineWidth',2)
plt.xlabel('x (m)')
cbar = plt.colorbar()
cbar.ax.set_ylabel("vort (1/s)") #set(get(cbar,'ylabel'),'String','vort ( 1/s ) ')
plt.text(txt_x, txt_y, '(d)','Color','k','FontSize',14)
#set(gca, 'LineWidth',  1)

plt.xlabel('x (m)')
#%ylabel('y (m)')

#set(fig, 'PaperPositionMode', 'auto')

#print('-depsc2',['plots/ideal_4_frame_4prof_',foldname, '.eps'])
#print('-djpeg',['plots/ideal_4_frame_4prof_',foldname, '.jpg'])


fig = plt.figure(3)
#clf

ax1 = [-175, 175, -0.001, 0.0012]
ax2 = [-175, 175, -0.01, 0.012]
ax3 = [-175, 175, -0.05, 0.075]
ax4 = [-175, 175, -0.05, 0.075]
txt_x = -160
txt_y = 0.09

figure_w = 9.0
figure_l = 10.0
#set(fig,'units','inches','paperunits','inches','papersize',... [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);
#colormap jet

fig = plt.figure(2, (figure_w, figure_l))
plt.subplot(4, 1, [4])

plt.plot(y, PgrdY[:,mm1], 'b', y, DySyy[:,mm1], 'r', y, DxSxy[:,mm1], 'r--', y, DyVVH[:,mm1], 'k', y, DxUVH[:,mm1], 'k--', y, FRCY[:,mm1], 'b:', y, Ry[:,mm1], 'c--', linewidth = 1)
plt.grid()
plt.ylabel(r'$m^2/s^2$')
plt.xlabel('y (m)')
plt.legend('$gH\frac{\partial \bar{\eta}}{\partial y}$','$\frac{\partial Syy}{\partial y}$', '$ \frac{\partial Sxy}{\partial x}$','$\frac{\partial \bar{Q}\bar{Q}/H}{\partial y}$', '$\frac{\partial \bar{P}\bar{Q}/H}{\partial x}$','$\bar{\tau}_y$','Ry',fontsize = 14)

plt.axis(ax1)

plt.text(-150, 0.0014, '(d)', fontsize = 14)

plt.subplot(4, 1, [3])
plt.plot(y, PgrdY[:,mm2], 'b', y, DySyy[:,mm2],'r', y, DxSxy[:,mm2], 'r--', y, DyVVH[:,mm2], 'k', y, DxUVH[:,mm2], 'k--', y, FRCY[:,mm2], 'b:', y, Ry[:,mm2], 'c--', linewidth = 1)
plt.grid()
plt.ylabel(r'$m^2/s^2$')
#%xlabel('y (m)')
plt.legend('$gH\frac{\partial \bar{\eta}}{\partial y}$','$\frac{\partial Syy}{\partial y}$', '$ \frac{\partial Sxy}{\partial x}$','$\frac{\partial \bar{Q}\bar{Q}/H}{\partial y}$', '$\frac{\partial \bar{P}\bar{Q}/H}{\partial x}$','$\bar{\tau}_y$','Ry', fontsize = 14)

plt.text(-150,0.014,'(c)','FontSize',14)
plt.axis(ax2)

plt.subplot(4,1,[2])
plt.plot(y, PgrdY[:, mm3], 'b', y, DySyy[:, mm3] ,'r', y, DxSxy[:, mm3],'r--', y, DyVVH[:, mm3],'k',y, DxUVH[:, mm3], 'k--', y, FRCY[:, mm3], 'b:', y, Ry[:, mm3], 'c--', linewidth = 1)
plt.grid()
plt.ylabel('m^2/s^2')
#xlabel('y (m)')
plt.legend('$gH\frac{\partial \bar{\eta}}{\partial y}$','$\frac{\partial Syy}{\partial y}$', '$ \frac{\partial Sxy}{\partial x}$','$\frac{\partial \bar{Q}\bar{Q}/H}{\partial y}$', '$\frac{\partial \bar{P}\bar{Q}/H}{\partial x}$', '$\bar{\tau}_y$', 'Ry', fontsize = 14)

plt.text(-150,0.09,'(b)','FontSize',14)
plt.axis(ax3)

plt.subplot(4,1,[1])
plt.plot(y, PgrdY[:,mm4], 'b', y, DySyy[:,mm4], 'r', y, DxSxy[:,mm4], 'r--', y, DyVVH[:,mm4], 'k', y, DxUVH[:, mm4], 'k--', y, FRCY[:, mm4], 'b:', y, Ry[:, mm4], 'c--', linewidth = 1)
plt.grid()
plt.ylabel(r'$m^2/s^2$')
#%xlabel('y (m)')
plt.legend('$gH\frac{\partial \bar{\eta}}{\partial y}$','$\frac{\partial Syy}{\partial y}$', '$ \frac{\partial Sxy}{\partial x}$','$\frac{\partial \bar{Q}\bar{Q}/H}{\partial y}$', '$\frac{\partial \bar{P}\bar{Q}/H}{\partial x}$','$\bar{\tau}_y$','Ry', fontsize = 14)

plt.text(-150,0.09,'(a)','FontSize',14)
plt.axis(ax4)


print('-depsc2', ['plots/momentum_xy2_', foldname, '.eps'])
print('-djpeg', ['plots/momentum_xy2_', foldname, '.jpg'])

fig = plt.figure(2)

txt_x = -690
txt_y = 0.09

ax1 = [-700, -40, -0.04, 0.075]
ax2 = [-700, -40, -0.1, 0.135]
ax3 = [-700, -40, -0.015, 0.025]
ax4 = [-700, -40, -0.035, 0.09]

figure_w = 9.0
figure_l = 10.0
fig2 = plt.figure(3, (figure_w, figure_l)) #set(fig,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);
#colormap jet

plt.subplot(4,1,[1])

plt.plot(x, PgrdX[nn2, :], 'b', x, DxSxx[nn2, :], 'r', x, DySxy[nn2, :], 'r--', x, DxUUH[nn2, :], 'k', x, DyUVH[nn2, :], 'k--', x, FRCX[nn2, :], 'b:', x, Rx[nn2, :], 'c--', linewidth = 1)

plt.axis(ax1)
plt.grid()
plt.ylabel(r'$m^2/s^2$')
plt.legend('$gH\frac{\partial \bar{\eta}}{\partial x}$','$\frac{\partial Sxx}{\partial x}$', '$ \frac{\partial Sxy}{\partial y}$','$\frac{\partial \bar{P}\bar{P}/H}{\partial x}$', '$\frac{\partial \bar{P}\bar{Q}/H}{\partial y}$','$\bar{\tau}_x$','Rx', fontsize = 14)

plt.text(-690, 0.086, '(a)', fontsize = 14)

plt.subplot(4,1,[2])
plt.plot(x, PgrdX[nn3, :], 'b', x, DxSxx[nn3, :], 'r', x, DySxy[nn3, :], 'r--', x, DxUUH[nn3, :], 'k', x, DyUVH[nn3, :],'k--', x, FRCX[nn3, :],'b:', x, Rx[nn3, :], 'c--', linewidth = 1)

plt.axis(ax2)
plt.grid()
plt.ylabel('m^2/s^2')

plt.text(-690, 0.15, '(b)', fontsize = 14)

plt.legend('$gH\frac{\partial \bar{\eta}}{\partial x}$','$\frac{\partial Sxx}{\partial x}$', '$ \frac{\partial Sxy}{\partial y}$','$\frac{\partial \bar{P}\bar{P}/H}{\partial x}$', '$\frac{\partial \bar{P}\bar{Q}/H}{\partial y}$','$\bar{\tau}_x$','Rx', fontsize = 14)


plt.subplot(4,1,[3])

plt.plot(x, PgrdY[nn2, :], 'b', x, DySyy[nn2, :], 'r', x, DxSxy[nn2, :], 'r--', x, DyVVH[nn2, :], 'k', x, DxUVH[nn2, :], 'k--', x, FRCY[nn2, :], 'b:', x, Ry[nn2, :], 'c--', linewidth = 1)

plt.axis(ax3)
plt.grid()
plt.ylabel(r'$m^2/s^2$')
plt.legend('$gH\frac{\partial \bar{\eta}}{\partial y}$','$\frac{\partial Syy}{\partial y}$', '$ \frac{\partial Sxy}{\partial x}$','$\frac{\partial \bar{Q}\bar{Q}/H}{\partial y}$', '$\frac{\partial \bar{P}\bar{Q}/H}{\partial x}$','$\bar{\tau}_y$','Ry', fontsize = 14)

plt.text(-690, 0.028, '(c)', fontsize = 14)

plt.subplot(4, 1, [4])
plt.plot(x, PgrdY[nn3,:], 'b', x, DySyy[nn3, :], 'r', x, DxSxy[nn3, :],'r--', x, DyVVH[nn3, :], 'k', x, DxUVH[nn3, :], 'k--', x, FRCY[nn3, :], 'b:', x, Ry[nn3, :], 'c--', linewidth = 1)

plt.axis(ax4)
plt.grid()
plt.xlabel('x (m)')
plt.ylabel(r'$m^2/s^2$')
plt.text(-690,0.1,'(d)','FontSize',14)

plt.legend('$gH\frac{\partial \bar{\eta}}{\partial y}$','$\frac{\partial Syy}{\partial y}$', '$ \frac{\partial Sxy}{\partial x}$','$\frac{\partial \bar{Q}\bar{Q}/H}{\partial y}$', '$\frac{\partial \bar{P}\bar{Q}/H}{\partial x}$','$\bar{\tau}_y$','Ry', fontsize = 14)

print('-depsc2',['plots/momentum_xy1_', foldname, '.eps'])
print('-djpeg',['plots/momentum_xy1_', foldname, '.jpg'])

#return