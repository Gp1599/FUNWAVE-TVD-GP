### Plot Flat Vessel Waves ###

# import necessary modules
import os
import numpy as np               
import matplotlib.pyplot as plt

# write your OWN PC folder path for fdir
# Remember that we use for Mac & Linux machines '/', while on windows '\'
#HOME = os.environ['HOME']
#fdir = os.path.join(HOME,'FUNWAVE-TVD','simple_cases','vessel_flat_bottom','work', 'output')
fdir = "../../../../simulationRuns/vessel_flat_bottom/output"
fileName = os.path.join(fdir, 'eta_00001')
eta = np.loadtxt(fileName)

# define plot location
n, m = np.shape(eta)
dx = 1.0
dy = 1.0

x = np.asarray([float(xa) * dx for xa in range(m)])
y = np.asarray([float(ya) * dy for ya in range(n)])

# Initialize test file parallel array hyperparamaters for the user to edit
nfile =     [   20,    40   ]   # range of eta files you want to plot
sec =       [   '20',  '40' ]   # time  you want to plot

# figure size option 
figure_w = 8    # width
figure_l = 5    # length

# Plot figure
fig = plt.figure(figsize = (figure_w, figure_l), dpi = 200)

# The helper function for every test file number
def executeFile(num):
    global nfile
    global sec
    global fig
    global x, y

    # Extract eta
    fnum = '%.5d' % nfile[num]
    etaFile = os.path.join(fdir, 'eta_' + fnum)
    eta = np.loadtxt(etaFile)

    # Create new subplot
    ax = fig.add_subplot(len(nfile), 1, num + 1)
    fig.subplots_adjust(hspace = .45)

    # Apply the coolwarm colormap background to the subplot
    plt.pcolormesh(x, y, eta,cmap = 'coolwarm')
    
    # Give the subplot the title to measure its corresponding minimum time
    title = 'Time = ' + sec[num] + ' sec'
    plt.title(title)
    
    # Tighten the subplot's axes
    plt.axis('tight')

    # Give the subplot axes names
    plt.ylabel('Y (m)')
    plt.xlabel('X (m)')
    
    # Give the subplot a colorbar and label that colorbar to measure U in meters
    cbar = plt.colorbar()
    cbar.set_label(r'$\eta$' + ' (m)', rotation = 90)
    plt.clim(-1.5, 1.5)

# Process every test file number
for num in range(len(nfile)):
    executeFile(num)
    #fnum= '%.5d' % nfile[num]
    #etaFile = os.path.join(fdir,'eta_'+fnum)
    #eta = np.loadtxt(etaFile)

    #ax = fig.add_subplot(len(nfile),1,num+1)
    #fig.subplots_adjust(hspace=.45)
    #plt.pcolor(x, y, eta,cmap='coolwarm')
    
    #title = 'Time = '+sec[num]+ ' sec'
    #plt.title(title)
    #plt.axis('tight')

    #plt.ylabel('Y (m)')
    #plt.xlabel('X (m)')
    #cbar=plt.colorbar()
    #cbar.set_label(r'$\eta$'+' (m)', rotation=90)
    #plt.clim(-1.5, 1.5)

# Finishing the figure by saving it as a png image
fig.savefig('eta_flat_vessel.png', dpi = fig.dpi)