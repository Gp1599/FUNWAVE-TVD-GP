import numpy as np
import matplotlib.pyplot as plt

# Initialize the path to the directory to the rain on hills output files
fdir = '../../../../simulationRuns/rain_on_hills/output/'

# Load the depth matrix
dep = np.loadtxt(fdir + 'dep.out')

# Initialize discretization parameters
dx = 10.0
dy = 10.0
[n, m] = np.shape(dep)

# Create 2D coordinates and the meshgrid via discretization
x = np.arange(0, m) * dx
y = np.arange(0, n) * dy
[xx, yy] = np.meshgrid(x, y)

# Initialize figure dimension hyperparameters
width = 10
length = 8

# Initialize the figure
fig = plt.figure(1, (width, length))
#set(fig,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[1 1 wid len]);

# Initialize the axis limit array
ax = [0, 6550, 0, 1990]

# Initializing the test file number list hyperparameter
files = np.arange(1, 3)

# Process every test file number
for num in range(1, len(files)):
    # Load the U, V, ETA, and mask matrix
    fnum = '%.5d' % files[num]
    u = np.loadtxt(fdir + 'u_' + fnum)
    v = np.loadtxt(fdir + 'v_' + fnum)
    eta = np.loadtxt(fdir + 'eta_' + fnum)
    mask = np.loadtxt(fdir + 'mask_' + fnum)

    # Mask the ETA and dep matrices
    dep1 = dep
    eta[mask < 1] = np.nan
    dep1[mask < 1] = np.nan

    # Mask the U and V matrices
    u[mask < 1] = np.nan
    v[mask < 1] = np.nan

    # Initialize the UU distance matrix
    uu = np.sqrt(np.pow(u, 2) + np.pow(v, 2))
    #[vort, vort1] = plt.curl(xx, yy, u, v)

    # Initialize the time 
    time = '%0.1f' % (files[num] * 20)

    #clf
    
    # Initialize the first subplot
    plt.subplot(211)

    # Apply the jet colormap to the first subplot based on the ETA matrix
    plt.pcolormesh(x, y, eta, cmap = 'jet')

    # Add contours to the first subplot
    plt.contourf(xx, yy, -dep, np.concatenate((np.arange(-12 , 0, 1.0), np.arange(0.1, 8, 0.1))))
    #plt.caxis([-12 12])
    
    #hold on
    # Add k-colored contours to the first plot
    plt.contour(xx, yy, -dep, [0, 0.1], colors = 'k', linewidths = 2)

    # Adding the colorbas to the subplot and labeling it to measure depth in meters
    h_bar = plt.colorbar()
    h_bar.ax.set_xlabel("depth (m)") #set(get(h_bar,'xlabel'),'string','depth (m)' )

    # Labeling the first subplot's axes to measure dimensions in meters
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')

    # Initializing the second subplot
    plt.subplot(212)
    
    # Applying the jet colormap to the second subplot based on the UU matrix
    plt.pcolormesh(xx, yy, uu, cmap = 'jet') #;shading interp
    #caxis([0.0 3.0])
    
    # Adding depth contours to the second subplot
    plt.contour(xx, yy, dep, np.arange(-5, 0, 0.2), colors = 'k')
    
    # Adding quivers to the second subplot
    sc = 50
    sk = 5
    plt.quiver(xx[1:sk:len(xx), 1:sk:len(xx[0])], yy[1:sk:len(yy), 1:sk:len(yy[0])], u[1:sk:len(u),1:sk:len(u[0])] * sc, v[1:sk:len(v), 1:sk:len(v[0])] * sc, 0)

    # Adding the colorbar to the second subplot and labeling it to measure flow speed in meters per second
    h_bar = plt.colorbar()
    h_bar.ax.set_xlabel("flow speed (m/s)")
    #set(get(h_bar,'xlabel'),'string','flow speed (m/s)' )

    # Labeling the second plot's axes to measure dimensions in meters
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')

    # Giving the plot a title to measure its respective time frame that is measured in seconds
    plt.title('time = ' + time + ' s')

    # Limiting the axes via the initialized axis limit array
    plt.axis(ax)
    
# Saving the main figure named "snap" as a PNG image
plt.savefig("snap.png")

#end
#print -djpeg snap.jpg