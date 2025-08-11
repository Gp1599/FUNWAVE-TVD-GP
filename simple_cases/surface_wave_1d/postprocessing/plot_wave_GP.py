### PLOT WAVE 1D CASE ###

# import necessary modules
import numpy as np               
import matplotlib.pyplot as plt
import os 
# write your OWN PC folder path for fdir
# Remember that we use for Mac & Linux machines '/', while on windows '\', adding r before the string helps with windows machines
#fdir = r'/Users/Gaby/Desktop/Postprocessing-Workshop/simple_cases_output/surface_wave_1d/surface_wave_1D/' 
fdir = "../../../../simulationRuns/surface_wave_1d/output/"

# Initialize the input hyperparameters
m = 1024
dx = 1.0
SLP = 0.05
Xslp = 800.0

# Bathymetry computation
x = np.asarray([float(xa)*dx for xa in range(m)])
dep = np.zeros((m,m))+10.0

# Calculate the coordinates of the slope
for i in range(len(x)):
     if i < Xslp:
         dep[i, 0]= dep[i, 0]
     else:
         dep[i, 0]= 10 - (x[i] - Xslp) * SLP

DEP = dep *- 1

# Locate wavemaker and sponge
wd = 10
x_wm = [250 - wd, 250 + wd, 250 + wd, 250 - wd, 250 - wd]
x_sponge = [0, 180, 180, 0, 0]
yy = [-10, -10, 10, 10, -10]

# Figure size options
width = 8       # width
length = 4      # length


# Plot Figure
fig = plt.figure(figsize = (width, length), dpi = 600)

# Load the eta file
eta = np.loadtxt(os.path.join(fdir,'eta_00014'))

# Create the subplot
ax = fig.add_subplot(1, 1, 1)
fig.subplots_adjust(hspace = 1, wspace = .5)
plt.plot(x, DEP[:,0], 'k', x, eta[0, :], 'b', linewidth = 2)
plt.plot(x_wm, yy, 'r')
plt.plot(x_sponge, yy, 'k')

# Show the grid
plt.grid()

# Show the Wavemaker and Sponge Layer
plt.text(x_wm[1], 0.6, 'Wavemaker', color = 'red', fontsize = 12, style = 'oblique')
plt.text(x_sponge[0] + 20, 0.6, 'Sponge Layer', color = 'black', fontsize = 12, style = 'oblique')

# Frame and label the axes and show their tickmarks
ax.axis([0, 1024, -1, 1])
plt.minorticks_on()
plt.xlabel('X (m)')
plt.ylabel(r'$\eta$'+' (m)')

# Save the main figure as a PNG file
fig.savefig('eta_1d_wave.png', dpi = fig.dpi) # save figure
