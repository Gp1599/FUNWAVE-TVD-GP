### Plot vessel_island wave  ###

# import necessary modules
import numpy as np               
import matplotlib.pyplot as plt

# compute bathymetry
m = 500   # x dimension points
n = 500   # y dimension points
dx = 2.0
dy = 2.0

# Initialize 2D coordinates via discretization
x = np.asarray([(float(xa) * dx) - m / 2 * dx for xa in range(m)])
y = np.asarray([(float(ya) * dy) - n / 2 * dy for ya in range(n)])

# Initialize the meshgrid out of the initialized x and y coordinates
X, Y = np.meshgrid(x, y)

# Initialize the input hyperparameters
R1 = 450
R2 = 100
Slope = 0.24
Slope_is = 0.24

# Initializing the depth matrix
dep = np.zeros((n, m)) + 10.0

# Process every grid cell
for j in range(n):
    for i in range(m):
        # Initializing R as the distance between 
        r = np.sqrt(X[j, i] ** 2 + Y[j, i] ** 2)
        # If the distance is greater than R1, then set the current grid point's depth ...
        if r > R1:
            dep[j, i] = 10.0 - (r - R1) * Slope
        # If the distance is less than R2, then set the current grid point's depth ...
        elif r < R2:
            dep[j, i] = 10.0 - (R2 - r) * Slope_is

# Set the depths of the grid points to -2.0 if they are less than -2.0
loc = np.where(dep < -2.0)  # locate indexes where dep < -2.0
dep[loc] = -2.0           # sustitute those values by -2.0

# Initialize Figure Size Hyperparameters 
figure_w = 8   # width
figure_l = 6  # length

# Initialize the main figure with the initialized hyperparameters
fig = plt.figure(figsize = (figure_w, figure_l), dpi = 200)

# Apply the terrain colormap to the figure based on the depth matrix
plt.pcolormesh(x, y, -1 * dep, cmap = 'terrain')         #plot depth in figure

# Add the vertical colorbar to measure Bathymetry in meters into the figure
cbar = plt.colorbar()
cbar.set_label('Bathymetry (m)', rotation = 90)

# Label and tighten the axis
plt.ylabel('Y (m)')
plt.xlabel('X (m)')
plt.axis('tight')

# Initialize constants
Rs = R2 - 40.0
x0 = Rs
y0 = 0.0
speed0 = 10.0

# Adding the x coordinate of the ship
xship = []
xship.append(x0)

# Adding the y coordinate of the ship
yship = []
yship.append(y0)

# Adding the sp of the ship
actsp = []
actsp.append(0.0)

#
t0 = 50
Rship = 250

# Computing the path of the ship
t = range(0,301)
for it in range(1,len(t)):
    # 
    if t[it] < t0:
        rship = Rs + (Rship - Rs) * t[it] / t0
    #
    else:
        rship = Rship

    #
    omega = speed0 / Rship
    angle = t[it] * omega

    #
    xship.append(rship * np.cos(angle))
    yship.append(rship * np.sin(angle))

    #
    ACTSP = np.sqrt((xship[it] - xship[it - 1]) ** 2 + (yship[it] - yship[it-1]) ** 2) / (t[it] - t[it - 1])
    actsp.append(ACTSP)

#plt.hold(True)
# Plotting the computed ship path
plt.plot(xship, yship, 'w--', linewidth = 2)  # plot ship in figure

# save figure
fig.savefig('mk_depth.png', dpi = fig.dpi)

# create vessel file 
vessel = np.zeros((len(t), 4))
vessel[:, 0] = t
vessel[:, 1] = np.asarray(xship) + m / 2 * dx
vessel[:, 2] = np.asarray(yship) + n / 2 * dy
vessel[:, 3] = np.asarray(actsp)

# Saving the depth and vessel data as txt files
np.savetxt('depth.txt', dep)  
np.savetxt('vessel_001.txt', vessel)