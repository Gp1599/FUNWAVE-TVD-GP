### Plot Flat Vessel Waves ###

# import necessary modules
import os
import numpy as np               
import matplotlib.pyplot as plt

# write your OWN PC folder path for fdir
# Remember that we use for Mac & Linux machines '/', while on windows '\'
HOME = os.environ['HOME']
#fdir = os.path.join(HOME,'FUNWAVE-TVD','simple_cases','vessel_flat_bottom','work', 'output')
fdir = "../../../../simulationRuns/vessel_types_compare/output/"
fileName = os.path.join(fdir,'eta_00001')
eta = np.loadtxt(fileName)

# Initialize Nglob, Mglob, and discretization parameters
n,m = np.shape(eta)
dx = 1.0
dy = 1.0

# Initialize 2D coordinates via discretization
x = np.asarray([float(xa) * dx for xa in range(m)])
y = np.asarray([float(ya) * dy for ya in range(n)])

# Initialize test file list hyperparameters
nfile = [   20,     40      ]   # range of eta files you want to plot
sec =   [   '20',   '40'    ]   # time  you want to plot

# Initialize figure dimension hyperparameters
width =  8      # width
length = 5      # length

# Plot figure
fig = plt.figure(figsize = (width,length), dpi = 200)

# Process every input file number
for num in range(len(nfile)):
    # Load the ETA file
    fnum = '%.5d' % nfile[num]
    etaFile = os.path.join(fdir, 'eta_' + fnum)
    eta = np.loadtxt(etaFile)

    # Initialize the subplot
    ax = fig.add_subplot(len(nfile), 1, num + 1)
    fig.subplots_adjust(hspace = .45)

    # Apply the coolwarm colormap to the subplot
    plt.pcolormesh(x, y, eta, cmap = 'coolwarm')
    
    # Give the subplot the title to represent its respective time frame to be measured in second
    title = 'Time = ' + sec[num] + ' sec'
    plt.title(title)

    # Tighten the axis
    plt.axis('tight')

    # Label the axes to measure their respective dimensions in meters
    plt.ylabel('Y (m)')
    plt.xlabel('X (m)')

    # Add the colorbar to measure mU in meters
    cbar = plt.colorbar()
    cbar.set_label(r'$\eta$'+' (m)', rotation = 90)

    # Set the subplot's image limits
    plt.clim(-1.5, 1.5)

# Save the ETA flat Vessel figure as a png
fig.savefig('eta_flat_vessel.png', dpi = fig.dpi)
