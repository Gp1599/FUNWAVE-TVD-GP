import numpy as np
import matplotlib.pyplot as plt

import tight_subplot

#clear all

fdir = '../../../simulationRuns/single_vessel_morphology/';

dep = np.loadtxt(fdir + 'dep_00000')

[n,m] = np.shape(dep)
N = 2 * n - 1
M = m

dx = 1.0
dy = 1.0
x = np.arange(0, M) * dx
y = np.arange(0, N) * dy

nfile = [   40,     80,      120    ]

min =   [  '80',   '160',   '240'   ]

figure_w = 8
figure_l = 8
fig = plt.figure(0, (figure_w, figure_l))
#set(gcf,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);
#clf

ETA = np.zeros((N, M))
CH = np.zeros((N, M))

[ha, pos] = tight_subplot.execute(6, 1, np.array([.05, 0.5]), np.array([.1, .05]), np.array([.1, .1])) 
ax = [0, 4500, 0, 120]

for num in range(0, len(nfile)):
        
    fnum = '%.5d' % nfile(num)
    eta = np.loadtxt(fdir + 'eta_' + fnum)
    mask = np.loadtxt(fdir + 'mask_' + fnum)
    ch = np.loadtxt(fdir + 'C_' + fnum)

    eta[mask < 1] = np.nan
    ch[mask < 1] = np.nan

    ETA[0:n, :] = eta[:, :]
    ETA[n+1:len(ETA), :] = eta[n-1:0:-1, :]
    CH[0:n, :] = ch[:, :]
    CH[n+1:len(CH), :] = ch[n-1:0:-1, :]

    plt.subplot(1, len(nfile), num)
    #%subplot(6,1,2*(num-1)+1)

    plt.axes(ha[2 * (num - 1) + 1])

    plt.pcolormesh(x, y, ETA) #,shading flat
    #hold on
    
    plt.title(' Time = ' + min[num] + ' sec ')
    plt.axis(ax)

    cbar = plt.colorbar()
    cbar.ax.set_ylabel("eta (m)") #set(get(cbar,'ylabel'),'String',' \eta (m) ')
    cbar.ax.axis([-0.3, 1.0, 0, 1])

    plt.ylabel('y (m)')

    #%subplot(6,1,2*(num-1)+2)
    plt.axes(ha(2 * (num - 1) + 2))

    plt.pcolormesh(x, y, np.log10(CH * 2680 * 1000.0)) #,shading flat
   

    #%title([' Time = ' min{num} ' sec '])
    cbar = plt.colorbar()
    cbar.ax.set_ylabel("log10(C) (mg/L)") #set(get(cbar,'ylabel'),'String',' log10(C) (mg/L) ')
    cbar.ax.axis([0, 2.999, 0, 1])
    
    plt.axis(ax)

    if num == len(nfile):
        plt.xlabel('x (m)')

    plt.ylabel(' y (m) ')

    cbar = plt.colorbar()
    cbar.ax.set_ylabel('eta (m)') #%set(get(cbar,'ylabel'),'String','\eta (m) ')

plt.savefig("eta_inlet_shoal_irr.png") #%print -djpeg eta_inlet_shoal_irr.jpg