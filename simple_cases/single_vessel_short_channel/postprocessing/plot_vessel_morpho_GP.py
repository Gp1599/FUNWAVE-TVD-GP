# import necessary modules
import numpy as np               
import matplotlib.pyplot as plt
from IPython.display import display
import os

pwd = os.getcwd()

# write your OWN PC folder path for fdir (change HOME to your approriate initial directory path)
#HOME = os.environ['HOME']
#FOLDER = os.path.join(HOME,'FUNWAVE-TVD','simple_cases','single_vessel_short_channel','work') # WRITE NAME OF PROJECT FOLDER
#fdir = os.path.join(pwd,FOLDER,'output')
fdir = "../../../../simulationRuns/single_vessel_short_channel/output/"

# Getting depth file and determining domain dimensions
depFile = os.path.join(fdir, 'dep.out')
dep = np.loadtxt(depFile)
[n, m] = dep.shape
print('n =', n, ' m =', m)

# Initialize the M and N constants
N = 2 * n + 1
M = m

# discretization
dx = 1.0
dy = 1.0

# x and y field vectors 
x = np.arange(0, M * dx, dx)
y = np.arange(0, N * dy, dy)

# Test File Hyperparameters
files =  [   20      ]
time =   [   '40'    ]

# Initializing the matrices
ETA =   np.zeros([N, M])
CH =    np.zeros([N, M])
BEDS =  np.zeros([N, M])
BEDB =  np.zeros([N, M])
BB =    np.zeros([N, M])
DEP =   np.zeros([N, M])

## Plot Output
size = 15 # label fontsize

# The helper function for each test file
def executeFile(num):
    # Initialize the 5-digit version of the current test file number
    fnum = '%.5d' % files[num]
    
    # Extract the matrices from the input files of the current test file number
    eta =   np.loadtxt(os.path.join(fdir,'eta_'     + fnum))
    mask =  np.loadtxt(os.path.join(fdir,'mask_'    + fnum))
    ch =    np.loadtxt(os.path.join(fdir,'C_'       + fnum))
    beds =  np.loadtxt(os.path.join(fdir,'DchgS_'   + fnum))
    bedb =  np.loadtxt(os.path.join(fdir,'DchgB_'   + fnum))
    
    # Removing masked regions from plot
    eta[np.where( mask < 1)] = np.nan
    ch[np.where( mask < 1)] = np.nan
    
    # Inserting the values of the eta matrix to the constant ETA vertically and symmetrically
    ETA [    0:n,    :] = eta [   :,      :]
    ETA [    n:-1,   :] = eta [   ::-1,   :]

    # Inserts the values of the ch matrix to the constant CH matrix vertically and symmetrically 
    CH  [    0:n,    :] = ch  [   :,      :]
    CH  [    n:-1,   :] = ch  [   ::-1,   :]
    
    # Inserts the values of the beds matrix to the constant BEDS matrix vertically and symmetrically
    BEDS[    0:n,    :] = beds[   :,      :]
    BEDS[    n:-1,   :] = beds[   ::-1,   :]

    # Inserts the values of the bedb matrix to the constant BEDB matrix vertically and symmetrically
    BEDB[    0:n,    :] = bedb[   :,      :]
    BEDB[    n:-1,   :] = bedb[   ::-1,   :]
    
    # Creating the BB matrix where values in BEDS are added by those in BEDB
    BB = BEDS + BEDB
    
    # plot eta (surface elevation)
    fig = plt.figure(figsize = (16, 12))
    
    # plot U
    ax1 = fig.add_subplot(3, 1, 1)
    ax1.tick_params(axis = 'both', which = 'major', labelsize = size)
    ax1.tick_params(axis = 'both', which = 'minor', labelsize = size)
    plt.pcolormesh(x, y, ETA, cmap = 'jet')
    ax1.axis([0, 400, 0, 120])
    h_bar = plt.colorbar(label = r'$\eta (m)$')
    plt.clim(-2.0, 2.0)
    plt.ylabel('y (m)', fontsize = size)
    
    # plot log10 
    ax2 = fig.add_subplot(3, 1, 2)
    ax2.tick_params(axis = 'both', which = 'major', labelsize = size)
    ax2.tick_params(axis = 'both', which = 'minor', labelsize = size)
    plt.pcolormesh(x, y, np.log10(CH), cmap = 'jet')
    ax2.axis([0, 400, 0, 120])
    l_bar = plt.colorbar(label = 'log10(C) (mg/L)')
    plt.clim(0, 0.5)
    plt.ylabel('y (m)', fontsize = size)
    
    # plot BB 
    ax3 = fig.add_subplot(3, 1, 3)
    ax3.tick_params(axis = 'both', which = 'major', labelsize = size)
    ax3.tick_params(axis = 'both', which = 'minor', labelsize = size)
    plt.contourf(x, y, BB, 10, cmap = 'jet')
    ax3.axis([0, 400, 0, 120])
    bb_bar = plt.colorbar(label = 'dZ (m)')
    plt.clim(-0.002, 0.002)
    plt.ylabel('y (m)', fontsize = size)
    plt.xlabel('x (m)', fontsize = size)
    
    # publishes the figure for the current test file number as a png image
    plt.savefig(os.path.join(pwd, 'vessel_eta_c_dz_%s.png' % (time[num])), dpi = 400)

# Process every test file
for num in range(len(files)):
    executeFile(num)
    #fnum = '%.5d' % files[num]
    #
    #eta = np.loadtxt(os.path.join(fdir,'eta_'+fnum))
    #mask = np.loadtxt(os.path.join(fdir,'mask_'+fnum))
    #ch = np.loadtxt(os.path.join(fdir,'C_'+fnum))
    #beds = np.loadtxt(os.path.join(fdir,'DchgS_'+fnum))
    #bedb = np.loadtxt(os.path.join(fdir,'DchgB_'+fnum))
    #
    ## Removing masked regions from plot
    #eta[np.where( mask < 1)] = np.nan
    #ch[np.where( mask < 1)] = np.nan
    #
    #ETA[0:n,:] = eta[:,:]
    #ETA[n:-1,:] = eta[::-1,:]
    #CH[0:n,:] = ch[:,:]
    #CH[n:-1,:] = ch[::-1,:]
    #
    #BEDS[0:n,:] = beds[:,:]
    #BEDS[n:-1,:] = beds[::-1,:]
    #BEDB[0:n,:] = bedb[:,:]
    #BEDB[n:-1,:] = bedb[::-1,:]
    #
    #BB = BEDS+BEDB
    #
    ## plot eta (surface elevation)
    #fig = plt.figure(figsize=(16, 12))
    #
    #ax1 = fig.add_subplot(3,1,1)
    #ax1.tick_params(axis='both', which='major', labelsize=size)
    #ax1.tick_params(axis='both', which='minor', labelsize=size)
    #plt.pcolor(x,y,ETA, cmap='jet')
    #ax1.axis([0, 400, 0, 120])
    #h_bar = plt.colorbar(label=r'$\eta (m)$')
    #plt.clim(-2.0, 2.0)
    #plt.ylabel('y (m)',fontsize=size)
    #
    # plot log10 
    #ax2 = fig.add_subplot(3,1,2)
    #ax2.tick_params(axis='both', which='major', labelsize=size)
    #ax2.tick_params(axis='both', which='minor', labelsize=size)
    #plt.pcolor(x,y,np.log10(CH), cmap='jet')
    #ax2.axis([0, 400, 0, 120])
    #l_bar = plt.colorbar(label='log10(C) (mg/L)')
    #plt.clim(0, 0.5)
    #plt.ylabel('y (m)',fontsize=size)
    #
    # plot BB 
    #ax3 = fig.add_subplot(3,1,3)
    #ax3.tick_params(axis='both', which='major', labelsize=size)
    #ax3.tick_params(axis='both', which='minor', labelsize=size)
    #plt.contourf(x,y,BB,10, cmap='jet')
    #ax3.axis([0, 400, 0, 120])
    #bb_bar = plt.colorbar(label='dZ (m)')
    #plt.clim(-0.002, 0.002)
    #plt.ylabel('y (m)',fontsize=size)
    #plt.xlabel('x (m)',fontsize=size)
    #
    #plt.savefig(os.path.join(pwd,'vessel_eta_c_dz_%s.png'%(time[num])), dpi=400) 

    
### plot average change in morpho    
[nn, mm] = np.shape(BB)

# Inserts elements of the dep matrix to the constant DEP matrix vertically and symmetrically
DEP[0:n,    :] = dep[:,     :]
DEP[n:-1,   :] = dep[::-1,  :]

# Initializes the B matrix of BB's first row shape with 0's
B = np.zeros(np.shape(BB[0, :]))

# Extracts every row from the BB matrix to the B matrix
for j in range(nn):
    B[j] = np.mean(BB[j, :])

# Initializes the figure for Bed Change and Depth
fig = plt.figure(figsize = (16, 12))

# Creating the subplot that visualizes bed change vs. y
ax1 = fig.add_subplot(2, 1, 1)
plt.plot(x, B, linewidth = 2.0)
ax1.grid(linestyle = '--', linewidth = 1)
plt.xlabel('y (m)')
plt.ylabel('Averaged Bed Change (m)')
ax1.axis([0 , 120, -0.004, 0.002])

# Creating the subplot that visualizes initial depth vs. y
ax2 = fig.add_subplot(2, 1, 2)
plt.plot(y, -1 * DEP[:, 0], linewidth = 2.0)
plt.plot([0, 120], [0, 0], 'b--')
ax2.grid(linestyle = '--', linewidth = 1) 
plt.xlabel('y (m)')
plt.ylabel('Initial Depth (m)')
ax2.axis([0, 120, -5.2, 2])

# Publishes the main figure for bed change and depth plots as a png image
plt.savefig(os.path.join(pwd,'vessel_bedchg_%s.png' % (time[num])), dpi = 400)