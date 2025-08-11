### PLOT Tohoku_tsunami bathymetry ###

# import necessary modules
import numpy as np               
import matplotlib.pyplot as plt

# write your OWN PC folder path for fdir and dep.
# Remember that we use for Mac & Linux machines '/', while on windows '\'
dir = "../../../../simulationRuns/tohoku_tsunami/"
dep = np.loadtxt(dir + 'external_files/depth_30min.txt')

# define bathy location
n,m = np.shape(dep)
dx = 0.5
dy = 0.5

x = np.asarray([float(xa) * dx + 132.01667 for xa in range(m)])
y = np.asarray([float(ya) * dy - 59.98333 for ya in range(n)])

# figure size option 
figure_w = 6    # width
figure_h = 4    # length

# Plot figure
fig = plt.figure(figsize = (figure_w, figure_h), dpi = 200)

# Initialize the subplot
ax = fig.add_subplot(1, 1, 1)
fig.subplots_adjust(hspace = 1, wspace = .25)

# apply the terrain colormesh to the subplot
plt.pcolormesh(x, y, -1 * dep, cmap = 'terrain')

# Tightening the subplot's axes
plt.axis('tight')

# Labeling the x and y labels to measure degrees in longitude and latitude respectively
plt.ylabel('Lat (deg)')
plt.xlabel('Lon (deg)')

# figure colorbar
cbar = plt.colorbar()
cbar.set_label('Bathymetry (m)', rotation = 90)

# save figure
fig.savefig('tsunami_bathy.png', dpi = fig.dpi)