
# -----------------------
# ----- User Input ------
# -----------------------

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import jet
from matplotlib import ticker

#HOME = os.environ['HOME']
#fdir = os.path.join(HOME,'FUNWAVE-TVD','simple_cases','rip_2D','work','output')
fdir = "../../../../simulationRuns/rip_2d/output/"

# -----------------------
# -- End of user input --
# -----------------------

# Load depth file
depFile = os.path.join(fdir, 'dep.out')
#print(depFile)
dep = np.loadtxt(depFile)

# Initialize discretization parameters
[n, m] = dep.shape
dx = 1.0
dy = 2.0

# Compute x and y coordinates via initialized discretization parameters
x = np.arange(0, m * dx, dx)
y = np.arange(0, n * dy, dy)

# Generate 2D grid with x and y points
[xx, yy] = np.meshgrid(x, y)

# Initialize test file number hyperparamaters
#nstart = input('enter nstart: ')
#nend = input('enter nend: ')
nfile = [1, 2, 3, 4]

# Initialize the EVERYWHICH constant
EVERYWHICH = 6 # plot every nth arrow (scales with image)

# previous version (2nd revision) nstart=280
def executeSubplot(num):
        # Padding integer values with zeros
        # to be 5 letters long e.g. 1 -> 00001
        fnum = '{0:0>5}'.format(num)

        # Load data from files
        u = np.loadtxt(os.path.join(fdir, 'umean_' + fnum))
        v = np.loadtxt(os.path.join(fdir, 'vmean_' + fnum))
        eta = np.loadtxt(os.path.join(fdir, 'eta_' + fnum))
        mask = np.loadtxt(os.path.join(fdir, 'mask_' + fnum))

        # Remove masked regions from plot
        eta[np.where(mask < 1)] = np.nan
        dep[np.where(mask < 1)] = np.nan
        u[np.where(mask < 1)] = np.nan
        v[np.where(mask < 1)] = np.nan

        
        # ------------------
        plt.subplot(1, 2, 1)

        plt.title("Rip 2D data for ETA #" + fnum)

        # plot eta (surface elevation)
        # Apply the jet colormap to the first subplot
        hp = plt.pcolormesh(xx, yy, eta, cmap = jet)

        # Limit the axes to Mglob and Nglob
        plt.axis([0, m * dx / 2, 0, n * dy])

        # Add the horizontal colorbar to the first subplot and apply the MaxNLocator ticker and x-axis measuring label to it
        h_bar = plt.colorbar(hp, orientation = "horizontal")
        tick_locator = ticker.MaxNLocator(nbins = 5)
        h_bar.locator = tick_locator
        h_bar.update_ticks()
        h_bar.ax.set_xlabel(r'$\eta (m)$')

        # Labeling the first subplot's axes to measure its dimensions in meters
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')

        # ----------------
        # Initializing the second subplot
        plt.subplot(1, 2, 2)

        # Adding the contour colormap to the second subplot
        cf = plt.contourf(xx, yy, -dep, 10)

        # Add a colorbar to the subplot and labeling its x-axis to measure depth in meters
        c_bar = plt.colorbar(cf, orientation = 'horizontal')
        #tick_locator_c = ticker.MaxNLocator(nbins = 5)
        #c_bar.locator = tick_locator_c
        #c_bar.update_ticks()
        c_bar.ax.set_xlabel('depth (m)')

        # Add quivers detailing <FIXME> to the subplot
        q = plt.quiver( xx[     ::EVERYWHICH, ::EVERYWHICH],
                        yy[     ::EVERYWHICH, ::EVERYWHICH],
                        u[      ::EVERYWHICH, ::EVERYWHICH],
                        v[      ::EVERYWHICH, ::EVERYWHICH])
        
        # Label the x-axis to measure the subplot's x dimension in meters
        plt.xlabel('x (m)')

        # Framing the subplot's axes to visualize the colormap of the whole water body
        plt.axis([0, m * dx / 2, 0, n * dy])
        
        # Saving the subplot as a png file
        plt.savefig('rip_2d_2subplot_num_' + str(num) + '.png', dpi = 400)                                            
        plt.show()

#for num=nstart:nend
#for num in range(int(nstart), int(nend) + 1):
for num in nfile:
        executeSubplot(num)
        # Padding integer values with zeros
        # to be 5 letters long e.g. 1 -> 00001
        #icount = icount + 1
        #fnum = '{0:0>5}'.format(num)

        # Loading data from files
        #u = np.loadtxt(os.path.join(fdir,'umean_'+fnum))
        #v = np.loadtxt(os.path.join(fdir,'vmean_'+fnum))
        #eta = np.loadtxt(os.path.join(fdir,'eta_'+fnum))
        #mask = np.loadtxt(os.path.join(fdir,'mask_'+fnum))

        # Removing masked regions from plot
        #eta[np.where( mask < 1)] = np.nan
        #dep[np.where( mask < 1)] = np.nan
        #u[np.where( mask < 1)] = np.nan
        #v[np.where( mask < 1)] = np.nan

        # ------------------
        #plt.subplot(1,2,1)

        # plot eta (surface elevation)
        #hp = plt.pcolor(xx,yy,eta, cmap=jet)
        #plt.axis([0,m*dx/2,0,n*dy])
        #h_bar = plt.colorbar(hp,orientation="horizontal")
        #tick_locator = ticker.MaxNLocator(nbins=5)
        #h_bar.locator = tick_locator
        #h_bar.update_ticks()

        #h_bar.ax.set_xlabel(r'$\eta (m)$')
        #plt.xlabel('x (m)')
        #plt.ylabel('y (m)')

        # ----------------
        #plt.subplot(1,2,2)

        #cf = plt.contourf(xx,yy,-dep,10);
        #c_bar = plt.colorbar(cf, orientation='horizontal')
        #c_bar.ax.set_xlabel('depth (m)')

        #everyWhich=6 # plot every nth arrow (scales with image)
        #q = plt.quiver(xx[::everyWhich, ::everyWhich],
        #               yy[::everyWhich, ::everyWhich],
        #               u[::everyWhich, ::everyWhich],
        #               v[::everyWhich, ::everyWhich])
        #plt.xlabel('x (m)')
        #plt.axis([0,m*dx/2,0,n*dy])

        #plt.savefig('rip_2d_2subplot_num_'+str(num)+'.png', dpi=400)                                                            
        #plt.show()                                                                                                              