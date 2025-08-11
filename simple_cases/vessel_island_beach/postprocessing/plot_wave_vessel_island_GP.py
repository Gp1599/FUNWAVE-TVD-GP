### Plot vessel_island wave  ###

# import necessary modules
import os
import numpy as np               
import matplotlib.pyplot as plt

# write your OWN PC folder path for fdir & fdep
# Remember that we use for Mac & Linux machines '/', while on windows '\'
#fdir = os.path.join('Users','Gaby','FUNWAVE-TVD','simple_cases','vessel_island_beach','output')
#fdep = os.path.join('Users','Gaby','FUNWAVE-TVD','simple_cases','vessel_island_beach')
fdir = "../../../../simulationRuns/vessel_island_beach/"

# Load the mask matrix
maskFile = os.path.join(fdir, 'output/eta_00001')
mask = np.loadtxt(maskFile)

# ask user for plot start and end numbers
#ns = int(input("Input plot start number: ns = "))
#ne = int(input("Input plot end number: ne = "))
nfile = range(0, 20)

# Load the depth matrix
dep1 = np.loadtxt(fdir + 'depth.txt')

# Extract Nglob and Mglob
n, m = np.shape(dep1)

# Initialize initial and discretization parameters
x0 = 0.0
y0 = 2.0
dx = 1.0

# Initialize 2D coordinates via discretization
x = np.asarray([(float(xa) * dx) + x0 for xa in range(m)])
y = np.asarray([(float(ya) * dx) + y0 for ya in range(n)])

# Initialize figure size hyperparameters
figure_w = 8   # width
figure_l = 6   # length

# Process every test file number
#for num in range(ns, ne):
for num in nfile:
    # plot figure
    # Initialize the figure
    fig = plt.figure(num, figsize = (figure_w, figure_l), dpi = 200)
    
    # Initialize the 5-digit version of the current test file number
    fnum = '%.5d' % num

    # Load the ETA matrix
    etaFileLoop = os.path.join(fdir, 'output/eta_' + str(fnum))
    eta = np.loadtxt(etaFileLoop)

    # Create the masked copy of the initialized ETA file
    eta_masked = np.ma.masked_where(eta > 10.0, eta) # do nt plot where eta>10. 0

    # Apply the coolwarm colormap to the figure based on the masked ETA matrix duplicate
    plt.pcolormesh(x, y, eta_masked, cmap = 'coolwarm')

    # Add the colorbar and labeling it to measure mU in meters
    cbar = plt.colorbar()
    cbar.set_label(r'$\eta$' + ' (m)', rotation = 90)

    # Setting the image limits of the figure
    plt.clim(-0.5, 0.5)
    
    # Labeling and tightening the axes to measure their respective dimensions in meters
    plt.ylabel('Y (m)')
    plt.xlabel('X (m)')
    plt.axis('tight')

    # Give the subplot the title to measure time in hours
    NUM = num - 1
    hour = '%.4d' % (NUM * 2.5)
    title = 'Time = ' + hour + ' sec'
    plt.title(title)

    # save figure
    name = 'fig_eta_%.4d' % (num)
    fig.savefig(name + '.png', dpi = fig.dpi)