
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
fdir = os.path.join(HOME,'FUNWAVE-TVD','simple_cases','rip_2D','work','output')

# -----------------------
# -- End of user input --
# -----------------------

# Getting depth file and determining domain dimensions

depFile = os.path.join(fdir,'dep.out')
dep = np.loadtxt(depFile)
[n,m] = dep.shape

# discretization
dx = 1.0
dy = 2.0

# x and y field vectors 
x = np.arange(0,m*dx,dx)
y = np.arange(0,n*dy,dy)

# Generating 2D grid with x and y points
[xx,yy] = np.meshgrid(x,y)

nstart = input('enter nstart: ')
nend = input('enter nend: ')

# previous version (2nd revision) nstart=280

icount = 0
#for num=nstart:nend
for num in range(int(nstart),int(nend)+1):
              # Padding integer values with zeros
              # to be 5 letters long e.g. 1 -> 00001
              icount = icount + 1
              fnum = '{0:0>5}'.format(num)

              # Loading data from files
              u = np.loadtxt(os.path.join(fdir,'umean_'+fnum))
              v = np.loadtxt(os.path.join(fdir,'vmean_'+fnum))
              eta = np.loadtxt(os.path.join(fdir,'eta_'+fnum))
              mask = np.loadtxt(os.path.join(fdir,'mask_'+fnum))

              # Removing masked regions from plot
              eta[np.where( mask < 1)] = np.nan
              dep[np.where( mask < 1)] = np.nan
              u[np.where( mask < 1)] = np.nan
              v[np.where( mask < 1)] = np.nan

              # ------------------
              plt.subplot(1,2,1)

              # plot eta (surface elevation)
              hp = plt.pcolor(xx,yy,eta, cmap=jet)
              plt.axis([0,m*dx/2,0,n*dy])
              h_bar = plt.colorbar(hp,orientation="horizontal")
              tick_locator = ticker.MaxNLocator(nbins=5)
              h_bar.locator = tick_locator
              h_bar.update_ticks()

              h_bar.ax.set_xlabel(r'$\eta (m)$')
              plt.xlabel('x (m)')
              plt.ylabel('y (m)')

              # ----------------
              plt.subplot(1,2,2)

              cf = plt.contourf(xx,yy,-dep,10);
              c_bar = plt.colorbar(cf, orientation='horizontal')
              c_bar.ax.set_xlabel('depth (m)')

              everyWhich=6 # plot every nth arrow (scales with image)
              q = plt.quiver(xx[::everyWhich, ::everyWhich],
                             yy[::everyWhich, ::everyWhich],
                             u[::everyWhich, ::everyWhich],
                             v[::everyWhich, ::everyWhich])
              plt.xlabel('x (m)')
              plt.axis([0,m*dx/2,0,n*dy])

              plt.savefig('rip_2d_2subplot_num_'+str(num)+'.png', dpi=400)                                                            
              plt.show()                                                                                                              
