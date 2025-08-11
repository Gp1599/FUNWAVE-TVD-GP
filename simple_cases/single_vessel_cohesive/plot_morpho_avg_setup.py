import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as cols

import tight_subplot

#clear all

fdir = '../../../simulationRuns/single_vessel_cohesive/output/'

dep = np.loadtxt(fdir + 'dep_00000')

[n, m] = np.shape(dep)
N = 2 * n - 1
M = m

dx = 1.0
dy = 1.0
x = np.arange(0, M) * dx
y = np.arange(0, N) * dy


nfile = [40, 80, 120]
#nfile = [40, 20]
mint = ['80', '160', '240']

figure_w = 8
figure_l = 4

fig = plt.figure(0, (figure_w, figure_l))
#set(gcf,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);
#clf

ETA = np.zeros((N, M))
CH = np.zeros((N, M))
BEDS = np.zeros((N, M))
BEDB = np.zeros((N, M))
BB = np.zeros((N, M))
DEP = np.zeros((N, M))

DEP[0:n, :] = dep[:, :]
DEP[n:len(DEP), :] = dep[n-1:0:-1, :]

[ha, pos] = tight_subplot.execute(2, 1, np.array([.05, 0.5]), np.array([.1, .05]), np.array([.1, .1])) 
ax = [0, 4500, 0, 120]

for num in range(0, len(nfile)):

    fnum = '%.5d' % nfile[num]
    eta = np.loadtxt(fdir + 'eta_' + fnum)
    mask = np.loadtxt(fdir + 'mask_' + fnum)
    ch = np.loadtxt(fdir + 'C_' + fnum)
    beds = np.loadtxt(fdir + 'DchgS_' + fnum)

    eta[mask < 1] = np.nan
    ch[mask < 1] = np.nan

    ETA[0:n, :] = eta[:, :]
    ETA[n:len(ETA), :] = eta[n - 1:0:-1, :]
    CH[0:n, :] = ch[:, :]
    CH[n:len(CH), :] = ch[n - 1:0:-1, :]

    BEDS[0:n, :] = beds[:, :]
    BEDS[n:len(BEDS), :] = beds[n - 1:0:-1, :]

    BB = BEDS

    plt.axes(ha[0])

    cmsh = plt.pcolormesh(x, y, CH, cmap = 'jet', norm = cols.BoundaryNorm(np.linspace(0, 1.2, 6), 12)) #, vmin = 0, vmax = 1.2) #,shading flat
    #plt.caxis([0 1.2])

    cbar = plt.colorbar(cmsh)
    cbar.ax.set_ylabel('C (g/L)') #set(get(cbar,'ylabel'),'String',' C (g/L) ')
    plt.axis(ax)

    plt.ylabel('y (m)')

    plt.axes(ha[1])

    cont = plt.contourf(x, y, BEDS, 10, vmin = -.0005, vmax = .0005, norm = cols.BoundaryNorm(np.arange(-.0005, .0005, 0.001/12), 12), cmap = 'jet')

    cbar = plt.colorbar(cont)
    cbar.ax.set_ylabel(r'$dZ_{sus} (m)$') #set(get(cbar,'ylabel'),'String',' dZ_{sus}  (m) ')
    plt.axis(ax)

    #caxis([-0.0005 0.0005])
    plt.ylabel('y (m)')

    plt.xlabel('x (m)')

    #colormap(jet(12))

plt.savefig("wakes_cohesive_morpho.png") #print -djpeg100 wakes_cohesive_morpho.jpg

#figure
plt.clf()
[nn, mm] = np.shape(BB)
B = np.zeros((nn, mm))
for j in range(0, nn):
    B[j] = np.mean(BB[j, :])

def createVector(matrix, t):
    result = np.zeros(len(matrix))
    for r in range(len(matrix)):
        chosen = 0
        if t == 'max':
            chosen = -999999999
        else:
            chosen = 999999999
        
        for c in range(len(matrix[0])):
            element = matrix[r, c]
            if t == 'max':
                if element > chosen:
                    chosen = element
            else:
                if element < chosen:
                    chosen = element
        result[r] = chosen
    return result

MaxH = np.max(ETA, 1) #createVector(ETA, 'max') #np.max(ETA, [], keepdims = 2)
MinH = np.min(ETA, 1) #createVector(ETA, 'min') #np.min(ETA, [], keepdims = 2)

print(MaxH)
print(MinH)

plt.subplot(211)
plt.plot(y, B, linewidth = 2)
plt.grid()
plt.xlabel('y (m)')
plt.ylabel('Averaged Bed Change (m)')
plt.axis([0, 120, -0.004, 0.002])

plt.subplot(212)
plt.plot(y, -DEP[:,0], linewidth = 2)
#hold on

plt.plot([15.7, 102.32], [0, 0], 'b--', linewidth = 1.5)
plt.plot(y, MaxH, 'r--', linewidth = 1.5)
plt.plot(y, MinH, 'r--', linewidth = 1.5)
plt.grid()
plt.xlabel('y (m)')
plt.ylabel('Initial Depth(m)')
plt.axis([0, 120, -3.2, 2])

plt.savefig("section_mean_wave_morpho.png") #print -djpeg100 section_mean_wave_morpho.jpg