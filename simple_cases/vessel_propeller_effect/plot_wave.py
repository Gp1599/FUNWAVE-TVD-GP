import numpy as np
import matplotlib.pyplot as plt

#clear all
fdir = 'output/'
fdir1 = 'output_nopropeller/'


dep = np.loadtxt(fdir + 'dep_00000')

[n, m] = np.shape(dep)

dx = 2.0
dy = 2.0
x = np.arange(0, m) * dx
y = np.arange(0, n) * dy

nfile = [35]


figure_w = 16
figure_l = 8
fig = plt.figure(0, (figure_w, figure_l))
#set(gcf,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);
#clf
#colormap jet

for num in np.arange(0, len(nfile)):
    
    fnum = '%.5d' % nfile[num]
    eta = np.loadtxt(fdir + 'eta_' + fnum)
    ch = np.loadtxt(fdir + 'C_' + fnum)
    ds = np.loadtxt(fdir + 'DchgS_' + fnum)
    db = np.loadtxt(fdir + 'DchgB_' + fnum)

    eta1 = np.loadtxt(fdir1 + 'eta_' + fnum)
    ch1 = np.loadtxt(fdir1 + 'C_' + fnum)
    ds1 = np.loadtxt(fdir1 + 'DchgS_' + fnum)
    db1 = np.loadtxt(fdir1 + 'DchgB_' + fnum)

    plt.subplot(421)
    plt.pcolormesh(x, y, eta1, vmin = -0.3, vmax = 1.5) #caxis([-0.3 1.5]),shading flat
    #hold on
    
    plt.title(' without propeller, Time = ' + str(nfile(num) * 1.0) + ' sec ')

    cbar = plt.colorbar()
    cbar.ax.set_ylabel = "eta (m)" #set(get(cbar,'ylabel'),'String',' \eta (m) ')


    #%xlabel(' x (m) ')
    plt.ylabel(' y (m) ')

    plt.subplot(423)
    plt.pcolormesh(x, y, ch1 * 100) #,shading flat
    #hold on

    plt.caxis([0.0, 0.01])
    cbar = plt.colorbar()
    cbar.ax.set_ylabel(" c (%) ") #set(get(cbar,'ylabel'),'String',' c (%) ')


    #%xlabel(' x (m) ')
    plt.ylabel(' y (m) ')


    plt.subplot(425)
    plt.pcolormesh(x, y, ds1, vmin = -0.002, vmax = 0.002) #caxis([-0.002 0.002]),shading flat
    #hold on
    
    cbar = plt.colorbar()
    cbar.ax.set_ylabel(" S-load-induced (m) ") #set(get(cbar,'ylabel'),'String',' S-load-induced (m) ')
    #%xlabel(' x (m) ')
    plt.ylabel(' y (m) ')

    plt.subplot(427)
    plt.pcolormesh(x, y, db1, vmin = -0.002, vmax = 0.002) #caxis([-0.002 0.002]),shading flat
    #hold on
    
    cbar = plt.colorbar()
    cbar.ax.set_ylabel(" B-load-induced (m) ") #set(get(cbar,'ylabel'),'String',' B-load-induced (m) ')
    plt.xlabel(' x (m) ')
    plt.ylabel(' y (m) ')

    plt.subplot(422)
    plt.pcolormesh(x, y, eta, vmin = -0.3, vmax = 1.5) #caxis([-0.3 1.5]),shading flat
    #hold on
    
    plt.title(' with propeller, Time = ' + str(nfile(num) * 1.0) + ' sec ')

    cbar = plt.colorbar()
    cbar.ax.set_ylabel = "eta (m)" #set(get(cbar,'ylabel'),'String',' \eta (m) ')


    #%xlabel(' x (m) ')
    #%ylabel(' y (m) ')

    plt.subplot(424)
    plt.pcolormesh(x, y, ch * 100, vmin = 0.0, vmax = 0.01) #caxis([0.0 0.01]),shading flat
    #hold on
    
    cbar = plt.colorbar()
    cbar.ax.set_ylabel(" c (%) ") #set(get(cbar,'ylabel'),'String',' c (%) ')


    #%xlabel(' x (m) ')
    #%ylabel(' y (m) ')


    plt.subplot(426)
    plt.pcolor(x, y, ds, vmin = -0.002, vmax = 0.002) #caxis([-0.002 0.002]),shading flat
    #hold on
    cbar = plt.colorbar()
    cbar.ax.set_ylabel(" S-load-induced (m) ") #set(get(cbar,'ylabel'),'String',' S-load-induced (m) ')
    #%xlabel(' x (m) ')
    #%ylabel(' y (m) ')

    plt.subplot(428)
    plt.pcolormesh(x, y, db, vmin = -0.002, vmax = 0.002) #,shading flat
    #hold on
    #caxis([-0.002 0.002])
    cbar = plt.colorbar()
    cbar.ax.set_ylabel(" B-load-induced (m) ") #set(get(cbar,'ylabel'),'String',' B-load-induced (m) ')
    plt.xlabel(' x (m) ')
    #%ylabel(' y (m) ')

#print -djpeg100 compare.jpg
