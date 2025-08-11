import numpy as np
import matplotlib.pyplot as plt
#clear all

#fdir='/Volumes/Seagate Backup Plus Drive/VESSEL_MORPHO/results/single_vessel_fr_13/';
fdir = "../../../simulationRuns/multi_vessel_morphology/"

dep = np.loadtxt(fdir + 'dep_00000')

[n, m]= np.shape(dep)
N = 2 * n - 1
M = m

dx = 1.0
dy = 1.0
x = np.arange(0, M - 1) * dx
y = np.arange(0, N - 1) * dy

nfile = [   40,     80,     120     ]

min =   [   '80',   '160',  '240'   ]

width =     8
length =    8
fig = plt.subplots(6, 1)
#set(gcf,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);
#clf

ETA = np.zeros((N, M))
CH = np.zeros((N, M))

ax = [0, 4500, 0, 120]

for num in range(1, length(nfile)):
    #
    fnum = '%.5d' % nfile(num)
    eta = np.loadtxt(fdir + 'eta_' + fnum)
    mask = np.loadtxt(fdir + 'mask_' + fnum)
    ch = np.loadtxt(fdir + 'C_' + fnum)

    eta[mask < 1] = np.nan
    ch[mask < 1] = np.nan

    ETA[1:n, :] = eta[:, :]
    ETA[n+1:len(ETA), :] = eta[n-1:-1:1, :]
    CH[1:n, :] = ch[:, :]
    CH[n+1:len(CH), :] = ch[n-1:-1:1, :]

    plt.subplot(1, length(nfile), num)
    #plt.subplot(6,1,2*(num-1)+1)

    #plt.axes(ha(2 * (num - 1) + 1));

    plt.pcolormesh(x, y, ETA) #,shading flat
    #hold on
    plt.axis([-0.3, 1.0, -10.0, 10.0])
    plt.title(' Time = ' + min[num] + ' sec ')
    plt.axis(ax)

    cbar = plt.colorbar()
    #set(get(cbar,'ylabel'),'String',' \eta (m) ')
    cbar.ax.yaxis.label = "eta (m)"

    plt.ylabel(' y (m) ')

    plt.subplot(6, 1, 2 * (num - 1) + 2)
    #plt.axes(ha(2*(num-1)+2));

    plt.pcolormesh(x, y, np.log10(CH * 2680 * 1000.0))#,shading flat
    plt.axis([0, 2.999, -10.0, 10.0])

    plt.title(' Time = ' + min[num] + ' sec ')
    cbar = plt.colorbar();
    #set(get(cbar,'ylabel'),'String',' log10(C) (mg/L) ')
    cbar.ax.yaxis.label = "log10(C) (mg/L)"
    plt.axis(ax)

    if num == length(nfile) - 1:
        plt.xlabel(' x (m) ')

plt.ylabel(' y (m) ')


cbar = plt.colorbar()
#%set(get(cbar,'ylabel'),'String','\eta (m) ')
cbar.ax.yaxis.label = "eta (m)"

plt.show()
#%print -djpeg eta_inlet_shoal_irr.jpg