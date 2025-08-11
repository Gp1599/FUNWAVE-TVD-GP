import numpy as np
import matplotlib.pyplot as plt

# Initializing the path to the output files
#clear all
fdir = '../../../simulationRuns/beach2D_radiation/output/'

# Initializing the test file number hyperparameter
files = [24]

# Load the depth file and initialize Nglob and Mglob from its shape
dep = np.loadtxt(fdir + 'dep.out')
[n, m] = np.shape(dep)

# Initialize the z num hyperparameter
z_num = 10

# The helper function for every test file number
def executeFile(k):
    # Load necessary files
    fnum = '%.5d' % files[k]
    eta = np.loadtxt(fdir + 'eta_' + fnum, encoding = 'ASCII')
    mask = np.loadtxt(fdir + 'mask_' + fnum, encoding = 'ASCII')
    u = np.loadtxt(fdir + 'u_' + fnum, encoding = 'ASCII')
    v = np.loadtxt(fdir + 'v_' + fnum, encoding = 'ASCII')
    Ax = np.loadtxt(fdir + 'Ax_' + fnum, encoding = 'ASCII')
    Ay = np.loadtxt(fdir + 'Ay_' + fnum, encoding = 'ASCII')
    Bx = np.loadtxt(fdir + 'Bx_' + fnum, encoding = 'ASCII')
    By = np.loadtxt(fdir + 'By_' + fnum, encoding = 'ASCII')

    #% ---------------------------------
    #% u(z)=(za-z)Ax+0.5(za^2-z^2)Bx
    #% v(z)=(za-z)Ay+0.5(za^2-z^2)By
    #% ---------------------------------

    # Initialize the z matrix
    z = np.ones((z_num, len(dep), len(dep[0]))) # from ChatGPT

    # inserting the altered version of the depth matrix into the lth matrix of z
    for l in range(0, z_num):
        z[l, :, :] = -dep[:, :] * (l - 1) / (z_num - 1)

    # Modifying 0-lth matrices in U and V
    za = -0.5528 * dep + 0.4472 * eta
    for l in range(0, z_num):
        zl = np.squeeze(z[l, :, :])
        u[l, :, :] = u + (za - zl) * Ax + 0.5 * (np.pow(za, 2) - np.pow(zl, 2)) * Bx
        v[l, :, :] = v + (za - zl) * Ay + 0.5 * (np.pow(za, 2) - np.pow(zl, 2)) * By

# Evecute every test file number
for k in range(0, len(files)):
    executeFile(k)