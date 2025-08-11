import numpy as np
import matplotlib.pyplot as plt

# Initialize the path to the directory that has output files for beach_2d_radiation
fdir ='../../../simulationRuns/beach2D_radiation/output/'

# Initialize discretization hyperparameters
n = 50
m = 250
dx = 2.0
dy = 2.0

# Initialize x and y coordinates via initialized discretization hyperparameters
x = np.arange(0, m) * dx
y = np.arange(0, n) * dy

# Initialize the test file number hyperparamater
#% x direction
num = 21

# Load the necessary matrices: ETA, BX, and FX
fnum = '%.5d' % num
eta = np.loadtxt(fdir + 'eta_' + fnum)
bx = np.loadtxt(fdir + 'BrkSrcX_' + fnum)
fx = np.loadtxt(fdir + 'FrcInsX_' + fnum)

# Initialize figure hyperparameters
figure_w = 11
figure_h = 5
figure_s = 0.5

# Initialize the figure with initialized hyperparameters
plt.figure(1, (figure_w, figure_h))
plt.subplots_adjust(wspace = figure_s)
#clf
#plt.pcolormesh(x, y, eta, cmap = 'jet') #colormap jet

# Initialize the first subplot
plt.subplot(131)

# Applying the jet colormap to the subplot based on the ETA matrix
plt.pcolormesh(x, y, eta, cmap = 'jet') #,shading flat

# Applying the axis frame to the subplot
plt.axis([300, 500, 0, 90])

# Giving the subplot labels to measure their respective dimensions in meters
plt.xlabel('x (m)')
plt.ylabel('y (m)')

# Giving the subplot the colorbar to measure ETA in meters
cbar = plt.colorbar()
cbar.ax.set_ylabel("eta (m)") #set(get(cbar,'ylabel'),'String','\eta (m)  ')

# Giving the subplot the title 'inst eta'
plt.title('inst eta')

# Initialize the second subplot
plt.subplot(132)

# applying the colormap to the subplot based on the BX matrix
plt.pcolormesh(x, y, bx, cmap = 'jet') #,shading flat

# Applying the axis frame to the subplot
plt.axis([300, 500, 0, 90])

# Giving the subplot's x-axis the label to measure a dimension in meters
plt.xlabel('x (m)')
#%ylabel('y(m)')

# Giving the subplot the colorbar to measure h/MU in square meters per square second
cbar = plt.colorbar()
cbar.ax.set_ylabel(r'$(h+\eta)R_{bx} (m^2/s^2)  $') #set(get(cbar,'ylabel'),'String','(h+\eta)R_{bx} (m^2/s^2)  ')
plt.title('inst brk stress in x')

# Initializing the third subplot
plt.subplot(133)

# Applying the colormap to the subplot based on the FX matrix
plt.pcolormesh(x, y, fx, cmap = 'jet') #,shading flat

# Applying the axis frame to the subplot
plt.axis([300, 500, 0, 90])

# Giving the subplot's x-axis a label to measure its respective dimension in meters
plt.xlabel('x (m)')
#%ylabel('y(m)')

# Giving the subplot the colorbar to measure -C^d uU in square meters per square second
cbar = plt.colorbar()
cbar.ax.set_ylabel(r'$-C_d uU (m^2/s^2)$')
#set(get(cbar,'ylabel'),'String','-C_d uU (m^2/s^2)  ')

# Giving the subplot the title to measure instant friction stress
plt.title('inst fric stress in x')

# Saving the main figure into a png file
plt.savefig("break_frc_inst.png") #print -djpeg100 break_frc_inst.jpg

#% averaged stuff
# Initializing the test file hyperparameter for average values
num = 4

# Loading the necessary matrices: FRDX and BRKDX
fnum = '%.5d' % num
FRCX = np.loadtxt(fdir + 'FRCX_' + fnum)
BrkDX = np.loadtxt(fdir + 'BrkDissX_' + fnum)

# Initializing the figure with the same hyperparameters as the last one
plt.figure(2, (figure_w, figure_h))
plt.subplots_adjust(wspace = figure_s)

# Initialize the first subplot
plt.subplot(131)

# Apply the jet colormap, based on the ETA matrix, to the subplot 
plt.pcolormesh(x, y, eta, cmap = 'jet') #,shading flat

# Apply the axis frame to the subplot
plt.axis([300, 500, 0, 90])

# Give the subplot the axis labels to measure their respective dimensions in meters
plt.xlabel('x (m)')
plt.ylabel('y (m)')

# Give the subplot the colorbar to measure ETA in meters
cbar = plt.colorbar()
cbar.ax.set_ylabel("eta (m)") #set(get(cbar,'ylabel'),'String','\eta (m)  ')

# Give the subplot the title indicating that the subplot is measuring inst eta
plt.title('inst eta')

# Create the second subplot 
plt.subplot(132)

# Apply the color
plt.pcolormesh(x, y, BrkDX, cmap = 'jet') #,shading flat
plt.axis([300, 500, 0, 90])
plt.xlabel('x(m)')
#plt.ylabel('y(m)')

# Give the subplot the colorbar 
cbar = plt.colorbar()
cbar.ax.set_ylabel(r'$(h+\eta)R_{bx} (m^2/s^2)$') #("#set(get(cbar,'ylabel'),'String','(h+\eta)R_{bx} (m^2/s^2)')
plt.title('avg brk stress')

#
plt.subplot(133)
plt.pcolormesh(x, y, FRCX, cmap = 'jet') #,shading flat
plt.axis([300, 500, 0, 90])
plt.xlabel('x(m)')
#plt.ylabel('y(m)')
cbar = plt.colorbar()
cbar.ax.set_ylabel(r'$-C_d uU (m^2/s^2)$') #set(get(cbar,'ylabel'),'String','-C_d uU (m^2/s^2)')
plt.title('avg fric stress')

#
plt.savefig("break_frc_avg.png") #print -djpeg100 break_frc_avg.jpg