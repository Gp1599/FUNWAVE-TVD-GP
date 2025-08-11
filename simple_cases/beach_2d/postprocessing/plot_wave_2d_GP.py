### PLOT WAVE for 2D CASE ###

# import necessary modules
import numpy as np               
import matplotlib.pyplot as plt
import os

# write your OWN PC folder path for fdir
# Remember that we use for Mac & Linux machines '/', while on windows '\'
#fdir = r'C:\Users\User\Documents\USACE_WORK\Funwave_Seminar\results\beach_2d\work\output'
fdir = "../../../../simulationRuns/beach2D/output/"
multipleResults = True

# upload eta file
eta = np.loadtxt(os.path.join(fdir,'eta_00001'))

# Initialize discretization hyperparameters.
n, m = np.shape(eta)
dx = 2.0
dy = 2.0

# Initialize x and y coordinates via initialize discretization.
x = np.asarray([float(xa) * dx for xa in range(m)])
y = np.asarray([float(ya) * dy for ya in range(n)])

# define the sponge's coordinates 
x_sponge =      [   0,         100,        100,            0,              0  ]
y_sponge =      [   0,         0,          y[-1],          y[-1],          0  ]

# define the wavemaker's coordinates
x_wavemaker =   [   155,       155      ]
y_wavemaker =   [   0,         y[-1]    ]

# Initializing the nfile and min parallel array parameters
nfile =         range(0, 50) #[   10,        25      ]    # range of eta files you want to plot
min =           [str(5 * t) for t in nfile] #[   '20',      '50'    ]    # time you want to plot

# figure size option 
figure_w = 10   # width
figure_l = 5    # length

# plot figure
fig = plt.figure(figsize = (figure_w, figure_l), dpi = 200)

#Gabriel's
#The class to represent a plot to be used for this file
def executeSubplot(num):
    global fig
    global nfile
    global min 
    global x, y
    global x_sponge, y_sponge
    global x_wavemaker, y_wavemaker

    # Initializes the eta and mask matrices
    fnum = '%.5d' % nfile[num]
    eta = np.loadtxt(os.path.join(fdir, "eta_" + fnum))
    mask = np.loadtxt(os.path.join(fdir, "mask_" + fnum))

    # Create the masked copy of the eta matrix 
    eta_masked = np.ma.masked_where(mask == 0, eta)

    # Add a new subplot
    ax = None
    if not multipleResults:
        ax = fig.add_subplot(1, len(nfile), num + 1)
    fig.subplots_adjust(hspace = 1, wspace = .25)

    # Apply the jet colormap background to the subplot
    plt.pcolormesh(x, y, eta_masked, cmap = 'coolwarm')

    # Add the title to the subplot
    title = "Time = " + min[num] + " sec"
    plt.title(title)

    # plot sponge and wavemaker + legend
    plt.plot(x_sponge, y_sponge, "g--", linewidth = 3, label = "Sponge") 
    plt.plot(x_wavemaker, y_wavemaker, 'k-', linewidth = 3, label = "Wavemaker")
    plt.legend()

    #Setting the subplot's axes
    if multipleResults:
        plt.ylabel('Y (m)')
        plt.xlabel('X (m)')
        cbar = plt.colorbar()
        cbar.set_label(r'$\eta$' + ' (m)', rotation = 90)
    else:
        if num == 0:
            plt.ylabel('Y (m)')
            plt.xlabel('X (m)')
        else:
            plt.xlabel('X (m)')
            cbar = plt.colorbar()
            cbar.set_label(r'$\eta$' + ' (m)', rotation = 90)
    
    if multipleResults:
        fig.savefig("results/eta_2d_wave_" + str(nfile[num]) + ".png")
        fig.clf()

#for num in range(len(nfile)):
#    fnum= '%.5d' % nfile[num]
#    eta = np.loadtxt(os.path.join(fdir,'eta_'+fnum))
#    mask = np.loadtxt(os.path.join(fdir,'mask_'+fnum))
#
#    eta_masked = np.ma.masked_where(mask==0,eta) # do nt plot where mask = 0
#
#    ax = fig.add_subplot(1,len(nfile),num+1)
#    fig.subplots_adjust(hspace=1,wspace=.25)
#    plt.pcolor(x, y, eta_masked,cmap='coolwarm')
#
#    title = 'Time = '+min[num]+ ' sec'
#    plt.title(title)
#    plt.hold(True)
#
#    # plot sponge and wavemaker
#    plt.plot(x_sponge,y_sponge,'g--',linewidth=3)
#    plt.text(50,500,'Sponge',color='g',rotation=90)
#    
#    plt.plot(x_wavemaker,y_wavemaker,'k-',linewidth=3)
#    plt.text(180,700,'Wavemaker',color='k',rotation=90)
#    
#    if num == 0:
#        plt.ylabel('Y (m)')
#        plt.xlabel('X (m)')
#    else:
#        plt.xlabel('X (m)')
#        cbar=plt.colorbar()
#        cbar.set_label(r'$\eta$'+' (m)', rotation=90)  

# Execute every test file number
for num in range(len(nfile)):
    executeSubplot(num)

# save figure  
if not multipleResults:
    fig.savefig('eta_2d_wave.png', dpi = fig.dpi)