
# -----------------------
# ----- User Input ------
# -----------------------

import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.cm import jet
from matplotlib import ticker

HOME = os.environ['HOME']
#fdir = os.path.join(HOME,'FUNWAVE-TVD','simple_cases','sediment_rip','work','output')
fdir = "../../../../simulationRuns/rip_sediment/output/"

# -----------------------
# -- End of user input --
# -----------------------

# Getting depth file and determining domain dimensions

depFile = os.path.join(fdir,'dep.out')
dep = np.loadtxt(depFile)
[n, m] = dep.shape

# discretization
dx = 1.0
dy = 2.0

# x and y field vectors 
x = np.arange(0, m * dx, dx)
y = np.arange(0, n * dy, dy)

# Generating 2D grid with x and y points
[xx, yy] = np.meshgrid(x, y)

#nstart = input('enter nstart: ')
#nend = input('enter nend: ')
nfile = [1, 2]

EVERYWHICH = 4 # plot every nth arrow (scales with image)

def executeFile(i):
    # Padding integer values with zeros
    # to be 5 letters long e.g. 1 -> 00001
    fnum = '{0:0>5}'.format(i)

    # Loading data from files
    u = np.loadtxt(os.path.join(fdir, 'umean_' + fnum))
    v = np.loadtxt(os.path.join(fdir, 'vmean_' + fnum))
    eta = np.loadtxt(os.path.join(fdir, 'eta_' + fnum))
    mask = np.loadtxt(os.path.join(fdir, 'mask_' + fnum))
    ch = np.loadtxt(os.path.join(fdir, 'C_' + fnum))
    dep1 = np.loadtxt(os.path.join(fdir, 'dep_' + fnum))
    depp = dep1 - dep

    # Removing masked regions from plot
    eta[np.where(mask < 1)] = np.nan
    dep[np.where(mask < 1)] = np.nan
    u[np.where(mask < 1)] = np.nan
    v[np.where(mask < 1)] = np.nan
    
    # Create the first subplot
    plot1 = plt.subplot(1, 3, 1)
    plot1.tick_params(axis = 'both', which = 'major', labelsize = 6)
    plot1.tick_params(axis = 'both', which = 'minor', labelsize = 6)

    # plot eta (surface elevation)

    # Apply 
    hp = plt.pcolormesh(xx, yy, eta, cmap = jet)
    
    #
    plot1.axis([0, 7 * m * dx / 9,0, (n - 1) * dy])

    #
    h_bar = plt.colorbar(hp,orientation = "horizontal")
    h_bar.ax.tick_params(labelsize = 6)

    #
    plt.clim(-0.5, 1.0)

    #
    tick_locator = ticker.MaxNLocator(nbins = 5)
    h_bar.locator = tick_locator
    h_bar.update_ticks()

    #
    h_bar.ax.set_xlabel(r'$\eta (m)$')

    #
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')

    # Create the second subplot
    plot2 = plt.subplot(1, 3, 2)
    plot2.tick_params(axis = 'both', which = 'major', labelsize = 6)
    plot2.tick_params(axis = 'both', which = 'minor', labelsize = 6)

    # 
    cf = plt.pcolor(xx, yy, np.log10(ch))

    # 
    c_bar = plt.colorbar(cf, orientation = 'horizontal')
    c_bar.ax.tick_params(labelsize = 6)

    # 
    plt.clim(-1.0, 1.0)

    # 
    tick_locator = ticker.MaxNLocator(nbins = 5)
    c_bar.locator = tick_locator
    c_bar.update_ticks()

    # 
    c_bar.ax.set_xlabel('log10(C) (g/l)')

    # 
    q = plt.quiver(
                    xx[::EVERYWHICH, ::EVERYWHICH], 
                    yy[::EVERYWHICH, ::EVERYWHICH], 
                    u[::EVERYWHICH, ::EVERYWHICH], 
                    v[::EVERYWHICH, ::EVERYWHICH])

    # 
    plot2.axis([0, 7 * m * dx / 9, 0, (n - 1) * dy])

    # 
    plt.xlabel('x (m)')


    # Creating the third subplot
    plot3 = plt.subplot(1, 3, 3)
    plot3.tick_params(axis = 'both', which = 'major', labelsize = 6)
    plot3.tick_params(axis = 'both', which = 'minor', labelsize = 6)

    db = plt.contourf(xx, yy, depp, 10)
    few_contours = plt.contour(xx, yy, depp, 10)
    plot3.axis([0,7 * m * dx / 9, 0, (n - 1) * dy])
    d_bar = plt.colorbar(db, orientation = "horizontal")
    d_bar.ax.tick_params(labelsize = 6)
    plt.clim(-0.05, 0.05)
    tick_locator = ticker.MaxNLocator(nbins = 5)
    d_bar.locator = tick_locator
    d_bar.update_ticks()

    d_bar.ax.set_xlabel('depth change (m)')
    plt.xlabel('x (m)')
              
    plt.savefig('sediment_rip_num_' + str(i) + '.png', dpi = 400)                                                            
    plt.show() 

#for num in range(int(nstart), int(nend) + 1):
for num in nfile:
    executeFile(num)
              # Padding integer values with zeros
              # to be 5 letters long e.g. 1 -> 00001
              #fnum = '{0:0>5}'.format(num)

              # Loading data from files
              #u = np.loadtxt(os.path.join(fdir,'umean_'+fnum))
              #v = np.loadtxt(os.path.join(fdir,'vmean_'+fnum))
              #eta = np.loadtxt(os.path.join(fdir,'eta_'+fnum))
              #mask = np.loadtxt(os.path.join(fdir,'mask_'+fnum))
              #ch = np.loadtxt(os.path.join(fdir,'C_'+fnum))
              #dep1 = np.loadtxt(os.path.join(fdir,'dep_'+fnum))
              #depp = dep1-dep

              # Removing masked regions from plot
              #eta[np.where( mask < 1)] = np.nan
              #dep[np.where( mask < 1)] = np.nan
              #u[np.where( mask < 1)] = np.nan
              #v[np.where( mask < 1)] = np.nan

              # ------------------
              #plot1 = plt.subplot(1,3,1)
              #plot1.tick_params(axis='both', which='major', labelsize=6)
              #plot1.tick_params(axis='both', which='minor', labelsize=6)

              # plot eta (surface elevation)
              #hp = plt.pcolor(xx,yy,eta, cmap=jet)
              #plot1.axis([0,7*m*dx/9,0,(n-1)*dy])
              #h_bar = plt.colorbar(hp,orientation="horizontal")
              #h_bar.ax.tick_params(labelsize=6)
              #plt.clim(-0.5, 1.0)
              #tick_locator = ticker.MaxNLocator(nbins=5)
              #h_bar.locator = tick_locator
              #h_bar.update_ticks()

              #h_bar.ax.set_xlabel(r'$\eta (m)$')
              #plt.xlabel('x (m)')
              #plt.ylabel('y (m)')

              # ----------------
              #plot2 = plt.subplot(1,3,2)
              #plot2.tick_params(axis='both', which='major', labelsize=6)
              #plot2.tick_params(axis='both', which='minor', labelsize=6)

              #cf = plt.pcolor(xx,yy,np.log10(ch));

              #c_bar = plt.colorbar(cf, orientation='horizontal')
              #c_bar.ax.tick_params(labelsize=6)
              #plt.clim(-1.0,1.0)
              #tick_locator = ticker.MaxNLocator(nbins=5)
              #c_bar.locator = tick_locator
              #c_bar.update_ticks()

              #c_bar.ax.set_xlabel('log10(C) (g/l)')

              #everyWhich=4 # plot every nth arrow (scales with image)
              #q = plt.quiver(xx[::everyWhich, ::everyWhich],
              #               yy[::everyWhich, ::everyWhich],
              #               u[::everyWhich, ::everyWhich],
              #               v[::everyWhich, ::everyWhich])

              #plot2.axis([0,7*m*dx/9,0,(n-1)*dy])
              #plt.xlabel('x (m)')


              # ---------------
              #plot3 = plt.subplot(1,3,3)
              #plot3.tick_params(axis='both', which='major', labelsize=6)
              #plot3.tick_params(axis='both', which='minor', labelsize=6)

              #db = plt.contourf(xx,yy,depp,10)
              #few_contours = plt.contour(xx,yy,depp,10)
              #plot3.axis([0,7*m*dx/9,0,(n-1)*dy])
              #d_bar = plt.colorbar(db, orientation="horizontal")
              #d_bar.ax.tick_params(labelsize=6)
              #plt.clim(-0.05, 0.05)
              #tick_locator = ticker.MaxNLocator(nbins=5)
              #d_bar.locator = tick_locator
              #d_bar.update_ticks()

              #d_bar.ax.set_xlabel('depth change (m)')
              #plt.xlabel('x (m)')
              
              #plt.savefig('sediment_rip_num_'+str(num)+'.png', dpi=400)                                                            
              #plt.show()