import numpy as np
import matplotlib.pyplot as plt

import tight_subplot

#clear all
fdir = '../../../simulationRuns/single_vessel_cohesive/output/'

dep = np.loadtxt(fdir + 'dep_00000')

[n, m] = np.shape(dep)
N = 2 * n - 1
M = m

dx = 1.0
dy = 1.0
x = np.arange(0, M) * dx
y = np.arange(0, N) * dy

nfile = [ 40,    80,     120 ]

min =   ['200', '400',  '600']

figure_w = 8
figure_l = 12
figure_s = 0.5
fig = plt.figure(0, (figure_w, figure_l)) #set(gcf,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);
#clf

ETA = np.zeros((N, M))
CH = np.zeros((N, M))

[ha, pos] = tight_subplot.execute(6, 1, [.05, 0.5], [.1, .05], [.1, .1]) 
ax = [0, 4500, 0, 120]

for num in range(0, len(nfile)):
    
    fnum = '%.5d' % nfile[num]

    eta = np.loadtxt(fdir + 'eta_' + fnum)
    mask = np.loadtxt(fdir + 'mask_' + fnum)
    ch = np.loadtxt(fdir + 'C_' + fnum)

    eta[mask < 1] = np.nan
    ch[mask < 1] = np.nan

    ETA[0:n, :] = eta[:, :]
    ETA[n:len(ETA), :] = eta[n - 1:0:-1, :]
    CH[0:n, :] = ch[:, :]
    CH[n:len(CH), :]= ch[n - 1:0:-1, :]

    plt.subplot(len(nfile) * 2, 1, num * 2 + 1)
    plt.subplots_adjust(hspace = figure_s)
    #plt.axes(ha[int(2 * (num - 1) + 1)])
    plt.pcolormesh(x, y, ETA, vmin = -0.3, vmax = 1.0, cmap = 'viridis') #,shading flat
    #hold on

    plt.title('Time = ' + min[num] + ' sec ')
    plt.axis(ax)

    cbar = plt.colorbar()
    cbar.ax.set_ylabel("eta (m)") #set(get(cbar,'ylabel'),'String',' \eta (m) ')
    #cbar.ax.axis([-0.3, 1.0, 0, 1]) #caxis([-0.3, 1.0])

    plt.ylabel('y (m)')

    plt.subplot(len(nfile) * 2, 1, num * 2 + 2)
    plt.subplots_adjust(hspace = figure_s)
    #plt.axes(ha[int(2 * (num - 1) + 2)])

    plt.pcolormesh(x, y, CH, vmin = 0, vmax = 1.2, cmap = 'viridis') #,shading flat
    
    #%title([' Time = ' min{num} ' sec '])
    cbar = plt.colorbar()
    cbar.ax.set_ylabel("C (g/L)") #set(get(cbar,'ylabel'),'String',' C (g/L) ')
    #cbar.ax.axis([0, 1.2]) #caxis([0 1.2])
    plt.axis(ax)

    if num == len(nfile) - 1:
        plt.xlabel(' x (m) ')
    plt.ylabel('y (m)')

#plt.ylabel(' y (m) ')

plt.savefig("wakes_cohesive_sed.png") #print -djpeg100 wakes_cohesive_sed.jpg