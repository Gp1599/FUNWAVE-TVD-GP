### PLOT WAVE for 2D CASE ###

# import necessary modules
import numpy as np               
import matplotlib.pyplot as plt
import os

# write your OWN PC folder path for fdir
# Remember that we use for Mac & Linux machines '/', while on windows '\', the r denotes raw string
#fdir = r'/Users/Gaby/Desktop/Postprocessing-Workshop/simple_cases_output/beach_2D/beach_2D/'

# Initialize path to the directory that has output files for beach_2d
fdir = "../../../../simulationRuns/beach2D/output/"

# Load the ETA matrix
eta = np.loadtxt(os.path.join(fdir,'eta_00001'))

# Initialize discretization hyperparamaters
n, m = np.shape(eta)
dx = 2.0
dy = 2.0

# Initialize x and y coordinates via initialized discretization hyperparameters
x = np.asarray([float(xa) * dx for xa in range(m)]) #numpy shape
y = np.asarray([float(ya) * dy for ya in range(n)]) #numpy shape

# Define sponge and wavemaker location
x_sponge =      [   0,         100,         100,          0,        0    ]
y_sponge =      [   0,          0,         y[-1],       y[-1],      0    ]

x_wavemaker =   [   155,        155     ]
y_wavemaker =   [    0,        y[-1]    ]

# Initialize the test file and minimum time parallel array hyperparameters
nfile =         [     1     ]       # range of eta files you want to plot
min =           [   '200'   ]       # time  you want to plot

# figure size option 
figure_w = 8    # width
figure_l = 5    # length

# plot figure
fig = plt.figure(figsize = (figure_w, figure_l), dpi = 200)
SK = 8

# Helper function for each subplot
def executeSubplot(num):
    global fig
    global nfile
    global min
    global x, y
    global x_sponge, y_sponge
    global x_wavemaker, y_wavemaker
    
    # Initializes the u, v, ht, and mask matrices
    fnum = '%.5d' % nfile[num]
    u = np.loadtxt(os.path.join(fdir, 'umean_' + fnum))
    v = np.loadtxt(os.path.join(fdir, 'vmean_' + fnum))
    ht = np.loadtxt(os.path.join(fdir, 'Hsig_' + fnum))
    mask = np.loadtxt(os.path.join(fdir, 'mask_' + fnum))

    # Create respective, masked copies of u v and ht
    u_masked = np.ma.masked_where(mask == 0, u)
    v_masked = np.ma.masked_where(mask == 0, v)
    ht_masked = np.ma.masked_where(mask == 0, ht)

    # Add a new subplot
    ax = fig.add_subplot(1, len(nfile), num + 1)
    fig.subplots_adjust(hspace = 1,wspace = .25)

    # Apply a jet colormap background, based on the masked ht matrix duplicate, to the subplot
    plt.pcolormesh(x, y, ht_masked, cmap = 'coolwarm')

    # titling the plot
    title = 'Time = ' + min[num] + ' sec'
    plt.title(title)

    # plot current vectors
    Q = plt.quiver(x[::SK], y[::SK], u[::SK, ::SK], v[::SK, ::SK], color = 'w')
    qk = plt.quiverkey(Q, 0.91, 0.91, 0.1, r'$0.1 \frac{m}{s}$', labelpos = 'E', coordinates = 'figure', color = 'k')

    # plot wavemaker and sponge
    plt.plot(x_sponge, y_sponge, 'g--', linewidth = 3, label = "Sponge")
    plt.plot(x_wavemaker, y_wavemaker, 'k-', linewidth = 3, label = "Wavemaker")
    plt.legend()

    # Sets the subplot's axes
    if num == 0:
        plt.ylabel('Y (m)')
        plt.xlabel('X (m)')
    else:
        plt.xlabel('X (m)')
        cbar = plt.colorbar()
        cbar.set_label('Hsig (m)', rotation = 90)

# execute every test file number
for num in range(len(nfile)):   
    executeSubplot(num)

# save figure        
fig.savefig('curr_2d_wave.png', dpi = fig.dpi)

#for num in range(len(nfile)):
    #fnum= '%.5d' % nfile[num]
    #u = np.loadtxt(os.path.join(fdir,'umean_'+fnum))
    #v = np.loadtxt(os.path.join(fdir,'vmean_'+fnum))
    #ht = np.loadtxt(os.path.join(fdir,'Hsig_'+fnum))
    #mask = np.loadtxt(os.path.join(fdir, 'mask_'+fnum))
    
    # do not plot values where mask = 0
    #u_masked = np.ma.masked_where(mask==0,u)
    #v_masked = np.ma.masked_where(mask==0,v)
    #ht_masked = np.ma.masked_where(mask==0,ht)

    #ax = fig.add_subplot(1,len(nfile),num+1)
    #fig.subplots_adjust(hspace=1,wspace=.25)
    #plt.pcolor(x, y, ht_masked,cmap='coolwarm')
    
    #title = 'Time = '+min[num]+ ' sec'
    #plt.title(title)
    #plt.hold(True)

    #sk=8

    # plot current vectors
    #Q = plt.quiver(x[0:len(x)-1:sk],y[0:len(y)-1:sk],u[0:len(u)-1:sk,0:len(u)-1:sk],v[0:len(v)-1:sk,0:len(v)-1:sk],color='w')
    #qk = plt.quiverkey(Q, 0.91, 0.91, 0.1, r'$0.1 \frac{m}{s}$', labelpos='E',
    #                   coordinates='figure',color='k')

    
    # plot wavemaker and sponge
    #plt.plot(x_sponge,y_sponge,'g--',linewidth=3)
    #plt.text(50,500,'Sponge',color='g',rotation=90);
    
    #plt.plot(x_wavemaker,y_wavemaker,'k-',linewidth=3)
    #plt.text(180,700,'Wavemaker',color='k',rotation=90);
    
    #if num == 0:
    #    plt.ylabel('Y (m)')
    #    plt.xlabel('X (m)')
    #else:
    #    plt.xlabel('X (m)')
    #    cbar = plt.colorbar()
    #    cbar.set_label('Hsig (m)', rotation=90)

# save figure        
#fig.savefig('curr_2d_wave.png', dpi=fig.dpi)