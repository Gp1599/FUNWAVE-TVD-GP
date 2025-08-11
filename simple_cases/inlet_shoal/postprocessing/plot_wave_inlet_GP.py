### PLOT WAVE for inlet_shoal CASE ###

# import necessary modules
import numpy as np               
import matplotlib.pyplot as plt

# write your OWN PC folder path for fdir and dep.
# Remember that we use for Mac & Linux machines '/', while on windows '\'
outputdir = '../../../../simulationRuns/inlet_shoal/'
fdir = outputdir + 'output/'

dep = np.loadtxt(outputdir + 'depth/dep_shoal_inlet.txt')

# define bathy location
n,m = np.shape(dep)
dx = 2.0
dy = 2.0

x = np.asarray([float(xa) * dx for xa in range(m)])
y = np.asarray([float(ya) * dy for ya in range(n)])

# define wavemaker and sponge location
x_sponge =      [0,     180,    180,        0,          0]
y_sponge =      [0,     0,      y[-1],      y[-1],      0]

x_wavemaker =   [250,   250     ]
y_wavemaker =   [0,     y[-1]   ]

# Initialize the test file and minimum time parallel array hyperparameters
nfile =         [0,     1,      2,      3,      ]  # range of eta files you want to plot
min =           ['150', '300',  '450',  '600'   ]  # time you want to plot

# figure size option
figure_w = 10   # width
figure_l = 5    # length

# Plot Figure
fig = plt.figure(figsize = (figure_w, figure_l), dpi = 200)

# The helper function for every test file
def executeFile(num):
    # Extract the eta matrix and make the masked copy
    fnum = '%.5d' % nfile[num]
    eta = np.loadtxt(fdir + 'eta_' + fnum)
    mask = np.loadtxt(fdir + 'mask_' + fnum)
    eta_masked = np.ma.masked_where(mask == 0, eta)  # do not plot where mask = 0

    # Initializing the subplot 
    ax = fig.add_subplot(1, len(nfile), num + 1)
    fig.subplots_adjust(hspace = 1, wspace = .25)

    # Applying the coolwarm colormap to the subplot
    plt.pcolormesh(x, y, eta_masked, cmap = 'coolwarm')

    # Tightening the subplot's axes 
    plt.axis('tight')

    # Giving the subplot the title to indicate its corresponding minimum time in seconds
    title = 'Time = ' + min[num] + ' sec'
    plt.title(title)

    # plot sponge and wavemaker
    plt.plot(x_sponge, y_sponge, 'g--', linewidth = 3, label = 'Sponge')
    plt.text(50, 1000, 'Sponge', color = 'g', rotation = 90)
    plt.plot(x_wavemaker, y_wavemaker, 'k-', linewidth = 3, label = 'Wavemaker')
    plt.text(300, 1200, 'Wavemaker', color = 'k', rotation = 90)
   
    # Labeling the subplot's axes and colorbars axis if the subplot is not the first one
    if num == 0:
        plt.ylabel('Y (m)')
        plt.xlabel('X (m)')
    else:
        plt.xlabel('X (m)')
        cbar = plt.colorbar()
        cbar.set_label(r'$\eta$'+' (m)', rotation = 90)

# Execute every test file number
for num in range(len(nfile)):
    executeFile(num)
    #fnum = '%.5d' % nfile[num]
    #eta = np.loadtxt(fdir + 'eta_' + fnum)
    #mask = np.loadtxt(fdir + 'mask_' + fnum)

    #eta_masked = np.ma.masked_where(mask == 0, eta)  # do not plot where mask = 0

    #ax = fig.add_subplot(1, len(nfile), num + 1)
    #fig.subplots_adjust(hspace = 1, wspace = .25)
    #plt.pcolormesh(x, y, eta_masked, cmap = 'coolwarm')
    #plt.axis('tight')
    #title = 'Time = ' + min[num] + ' sec'
    #plt.title(title)
    #plt.hold(True)

    # plot sponge and wavemaker
    #plt.plot(x_sponge, y_sponge, 'g--', linewidth = 3, label = 'Sponge')
    #plt.text(50, 1000, 'Sponge', color = 'g', rotation = 90)
    #plt.plot(x_wavemaker, y_wavemaker, 'k-', linewidth = 3, label = 'Wavemaker')
    #plt.text(300, 1200, 'Wavemaker', color = 'k', rotation = 90)
    #plt.legend()
   
    #if num == 0:
    #    plt.ylabel('Y (m)')
    #    plt.xlabel('X (m)')
    #else:
    #    plt.xlabel('X (m)')
    #    cbar = plt.colorbar()
    #    cbar.set_label(r'$\eta$'+' (m)', rotation = 90)

# save figure        
fig.savefig('inlet__shoal_wave.png', dpi = fig.dpi)