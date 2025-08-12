import numpy as np
import matplotlib.pyplot as plt

# Initializing the path to the output directory for the beach_2d_radiation simple case
fdir = "../../../simulationRuns/beach2D_radiation/output/" #'output/';

# 
#% x direction
# Initializing the test file number hyperparameter
num = 3

# Loading the matrices
fnum = '%.5d' % num
PgrdX = np.loadtxt(fdir + 'PgrdX_' + fnum)
FRCX = np.loadtxt(fdir + 'FRCX_' + fnum)
DxSxx = np.loadtxt(fdir + 'DxSxx_' + fnum)
DySxy = np.loadtxt(fdir + 'DySxy_' + fnum)
DxUUH = np.loadtxt(fdir + 'DxUUH_' + fnum)
DyUVH = np.loadtxt(fdir + 'DyUVH_' + fnum)

PgrdY = np.loadtxt(fdir + 'PgrdY_' + fnum)
FRCY = np.loadtxt(fdir + 'FRCY_' + fnum)
DySyy = np.loadtxt(fdir + 'DySyy_' + fnum)
DxSxy = np.loadtxt(fdir + 'DxSxy_' + fnum)
DyVVH = np.loadtxt(fdir + 'DyVVH_' + fnum)
DxUVH = np.loadtxt(fdir + 'DxUVH_' + fnum)

# Creating the figure
ny = 25
plt.figure(1)

# Create the 1st subplot
#clf
plt.subplot(211)
plt.plot(PgrdX[ny - 1, :], 'r')
#hold on
plt.plot(DxSxx[ny - 1, :], 'b')
plt.plot(DySxy[ny - 1, :], 'b--')
plt.plot(FRCX[ny - 1, :], 'k-')
plt.plot(DxUUH[ny - 1, :], 'c')
plt.plot(DyUVH[ny - 1, :], 'c--')
plt.legend(['PgrdX', 'DxSxx', 'DySxy', 'FRCX', 'DxUUH', 'DyUVH'], loc = 'upper left')
plt.grid()
#plt.xlabel('grid point')
plt.ylabel(r'$m^2/s^2$')

# Create the 2nd subplot
plt.subplot(212)
plt.plot(PgrdY[ny, :], 'r')
#hold on
plt.plot(DySyy[ny, :], 'b--')
plt.plot(DxSxy[ny, :], 'b-')
plt.plot(FRCY[ny, :], 'k-')
plt.plot(DyVVH[ny, :], 'c--')
plt.plot(DxUVH[ny, :],'c-')
plt.legend(['PgrdY', 'DySyy', 'DxSxy', 'FRCY', 'DyVVH', 'DxUVH'], loc = 'upper left')
plt.grid()
plt.xlabel('grid point')
plt.ylabel(r'$m^2/s^2$')

# Saving the main figure for the test file number as a png image
plt.savefig("balance.png") #"#print -djpeg100 balance.jpg