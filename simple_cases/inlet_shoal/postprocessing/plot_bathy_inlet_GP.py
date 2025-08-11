### PLOT inlet_shoal bathymetry ###

# import necessary modules
import numpy as np               
import matplotlib.pyplot as plt

# write your OWN PC folder path for dep.
# Remember that we use for Mac & Linux machines '/', while on windows '\'
dep = np.loadtxt('../../../../simulationRuns/inlet_shoal/depth/dep_shoal_inlet.txt')

# define bathy location
n,m = np.shape(dep)
dx = 2.0
dy = 2.0

# Initialize the x and y coordinates via discretization
x = np.asarray([float(xa) * dx for xa in range(m)])
y = np.asarray([float(ya) * dy for ya in range(n)])

# define wavemaker and sponge location
x_sponge =      [0,     180,    180,    0,      0]
y_sponge =      [0,     0,      y[-1],  y[-1],  0]

x_wavemaker =   [250,   250     ]
y_wavemaker =   [0,     y[-1]   ]

# figure size option hyperparameters
figure_w = 6    # width
figure_l = 5    # length

# Plot figure
fig = plt.figure(figsize = (figure_w, figure_l), dpi = 200)
ax = fig.add_subplot(1, 1, 1)
fig.subplots_adjust(hspace = 1, wspace = .25)

# Apply the terrain colormap to the subplot
plt.pcolormesh(x, y, -1 * dep, cmap = 'terrain')

# Tighten the subplot's axes
plt.axis('tight')  

# Label the subplot's x and y axes to measure dimensions in meters
plt.ylabel('Y (m)')
plt.xlabel('X (m)')

# plot sponge and wavemaker
plt.plot(x_sponge, y_sponge, 'k--', linewidth = 3)
plt.text(10, 1000, 'Sponge', color = 'w', rotation = 90)
plt.plot(x_wavemaker, y_wavemaker, 'k-', linewidth = 3)
plt.text(270, 1200, 'Wavemaker', color = 'w', rotation = 90)

# figure colorbar
cbar = plt.colorbar()
cbar.set_label('Bathymetry (m)', rotation = 90)

# save figure
fig.savefig('inlet__shoal_bathy.png', dpi = fig.dpi)