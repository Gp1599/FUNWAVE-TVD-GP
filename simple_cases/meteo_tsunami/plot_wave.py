import numpy as np
import matplotlib.pyplot as plt

#clear all
fdir = '../../../simulationRuns/meteo_tsunami/output/'

# Loading the ETA matrix
eta = np.loadtxt(fdir + 'eta_00001')

# Initializing discretization parameters
[n, m] = np.shape(eta)
dx = 500.0
dy = 500.0

# Initializing the 2D coordinates via discretization
x = np.arange(0, m) * dx
y = np.arange(0, n) * dy

# Initializing input file list hyperparameters
nfile = [    11,     16,     21,     26,     31,     36     ]
min =   [   '1.0',  '1.5',  '2.0',  '2.5',  '3.0',  '3.5'   ]

# Initializing figure dimension hyperparameters
figure_w = 6
figure_h = 11
figure_s = 0.5
#plt.set(gcf,'units','inches','paperunits','inches','papersize', [width length],'position',[1 1 wid len],'paperposition',[0 0 wid len]);
#clf

# Initializing the main figure with the initialized hyperparameters
fig = plt.figure(0, (figure_w, figure_h))
plt.subplots_adjust(hspace = figure_s)

# Helper function for every test file name
def executeFile(num):
    global x, y
    global nfile
    global min

    # Load the ETA file
    fnum = '%0.5d' % nfile[num]
    eta = np.loadtxt(fdir + 'eta_' + fnum)

    # Initialize the subplot
    plt.subplot(len(nfile) - 1, 1, num)
    
    # Plot the state of the wave
    plt.plot(x[:], eta[49, :], label = 'LineWidth')
    
    # Framing the axes
    plt.axis([0, 300000, -0.5, 1])

    # Showing the grid
    plt.grid()

    # Giving the subplot the title to measure its respective time frame meaured in hours
    plt.title(' Time = ' + min[num] + ' hr ', loc = 'center')

    # Labeling the y axis to measure ETA in meters
    plt.ylabel(' eta (m) ')

# Execute every test file number
for num in range(1, len(nfile)):
    executeFile(num)
    #fnum = '%0.5d' % nfile[num]
    #eta = np.loadtxt(fdir + 'eta_' + fnum)
    #
    #
    #plt.subplot(6, 1, num)
    #plt.subplots_adjust(wspace = 0.5, hspace = 1.8)
    #plt.plot(x[:], eta[49, :], label = 'LineWidth')
    #plt.axis([0, 300000, -0.5, 1])
    #plt.grid()
    #
    #
    #plt.title(' Time = ' + min[num] + ' hr ')
    #
    #
    #plt.ylabel(' eta (m) ')
    #
    #
    #if(num == len(nfile)):
    #    plt.xlabel(' x (m) ')

plt.savefig("wave_plt.png")
#set(gcf,'Renderer','zbuffer')