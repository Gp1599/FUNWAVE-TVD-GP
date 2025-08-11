import numpy as np
import matplotlib.pyplot as plt

import wvnum_omvec
#clear all

period = [2.5, 3, 6]

#clf

figure_w = 8
figure_l = 6
fig = plt.figure(0, (figure_w, figure_l)) #set(fig,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);

for kk in range(0, len(period)):

    #cases = 'T' + str(period[kk]) + 's'
    fdir = "../../../simulationRuns/vertical_velocity_structure/output/" #'/Volumes/Solid/Vertical_structures/FUNWAVE/results/' + cases + '/'

    if period[kk] == 2.5:
        m0 = 645

    if period[kk] == 3:
        m0 = 650
 
    if period[kk] == 6:
        m0 = 650


    files = [8]

    if period[kk] == 9:
        m0 = 1148
        files = [5]


    dep = np.load(fdir + 'dep.out')
    [n, m] = np.shape(dep)

    z_num = 10

    #% theory
    amp = 0.5
    g = 9.81
    h = 10.0
    T = period[kk]
    f = 1 / T
    om = f * 2 * np.pi
    K = wvnum_omvec.execute(h, om, g)
    lam = 2 * np.pi / K
    C = lam * f
    kh = K * h
    zt = - np.arange(0, h)
    u_theory = amp * om * np.cosh(kh + K * zt) / np.sinh(kh)

    for k in range(0, len(files)):

        fnum = '%.5d' % files[k]

        eta = np.loadtxt(fdir + 'eta_' + fnum)      #,'-ASCII');
        mask = np.loadtxt(fdir + 'mask_' + fnum)    #,'-ASCII');
        u = np.loadtxt(fdir + 'u_' + fnum)          #,'-ASCII');
        v = np.loadtxt(fdir + 'v_' + fnum)          #,'-ASCII');
        Ax = np.loadtxt(fdir + 'Ax_' + fnum)        #,'-ASCII');
        Ay = np.loadtxt(fdir + 'Ay_' + fnum)        #,'-ASCII');
        Bx = np.loadtxt(fdir + 'Bx_' + fnum)        #,'-ASCII');
        By = np.loadtxt(fdir + 'By_' + fnum)        #,'-ASCII');

        #% ---------------------------------
        #% u(z)=(za-z)Ax+0.5(za^2-z^2)Bx
        #% v(z)=(za-z)Ay+0.5(za^2-z^2)By
        #% ---------------------------------

        #clear z U V
        z = np.zeros((z_num, len(dep), len(dep[0])))
        for l in range(0, z_num):
            z[l, :, :] = -dep[:, :] * (l - 1) / (z_num - 1)

        za = -0.5528 * dep + 0.4472 * eta
        U = np.zeros((z_num, len(u), len(u[0])))
        V = np.zeros((z_num, len(v), len(v[0])))
        for l in range(0, z_num):
            zl = np.squeeze(z[l, :, :])
            U[l, :, :] = u + (za - zl) * Ax + 0.5 * (np.pow(za, 2) - np.pow(zl, 2)) * Bx
            V[l, :, :] = v + (za - zl) * Ay + 0.5 * (np.pow(za, 2) - np.pow(zl, 2)) * By

        n0 = 25

        plt.subplot(1,3,kk)
        plt.plot(U[:, n0, m0], z[:, n0, m0], 'b-', linewidth = 2)
        plt.xlabel('u (m/s)')

        plt.grid()

        #hold on
        plt.plot(u_theory,zt, 'r--', linewidth = 2)

        plt.axis(-0.3, 1.3, -10, 0)

        if kk == 1:
            plt.ylabel('z (m)')

        if kk == 1:
            pass #plt.legend('FUNWAVE', 'Theory', 'LOCATION', 'SouthEast')

        plt.title('kh = ' + str[kh])


#eval('mkdir plots')

fname = 'plots/compare.png'
fig.savefig(fname)

#print('-djpeg', fname)