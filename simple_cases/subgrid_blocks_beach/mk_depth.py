import numpy as np
import matplotlib.pyplot as plt

#clear all
#% beach
nx_total = 500
ny_total = 30
dx = 2.0
dy = 2.0
dep_offshore = 10.0
slope = 0.025
X_toe = 560.0
x = np.arange(0, nx_total) * dx
y = np.arange(0, ny_total) * dy 
dep = np.zeros((ny_total, nx_total)) + dep_offshore
for j in range(0, ny_total):
  for i in range(0, nx_total):
    if x[i] > X_toe:
      dep[j, i] = dep_offshore - slope * (x[i] - X_toe)

#% cell info
cell_m = 4
cell_n = 4
obs_m = 3
obs_n = 3
dep_bottom = 9999.0
dep_top = -2.5

#% grid info
m = nx_total * cell_m
n = ny_total * cell_n
m_start = 400
n_start = 1
nx_blocks = 100
ny_blocks = 30

m_obs1 = int(1 + np.floor((cell_m - obs_m) / 2))
m_obs2 = int(1 + np.floor((cell_m - obs_m) / 2) + obs_m - 1)
n_obs1 = int(1 + np.floor((cell_n - obs_n) / 2))
n_obs2 = int(1 + np.floor((cell_n - obs_n) / 2) + obs_n - 1)

dep_cell = np.zeros((cell_n, cell_m))
dep_cell[n_obs1:n_obs2, m_obs1:m_obs2] = dep_top

dep_full = np.zeros((n, m))
for j in range(0, n):
  for i in range(0, m):
    jj = int(np.floor((j - 1) / cell_n))
    ii = int(np.floor((i - 1) / cell_m))
    dep_full[j, i] = dep[jj, ii]

dep_sub_writeout = np.zeros((ny_blocks * nx_blocks, cell_n * cell_m))
icount = 0
dep_cell_add = np.zeros((cell_n, cell_m))
for j in range(0, ny_blocks):
  for i in range(0, nx_blocks):
    m1 = (m_start - 1) * cell_m + (i) * cell_m
    m2 = m1 + cell_m
    n1 = (n_start - 1) * cell_n + (j) * cell_n
    n2 = n1 + cell_n

    j_coarse = n_start + (j - 1)
    i_coarse = m_start + (i - 1)
    dep_cell_add[:, :] = dep[j_coarse, i_coarse] + dep_cell[:, :]
    #print(dep_full.shape)
    #print(dep_cell.shape)
    dep_full[n1:n2, m1:m2] = dep_cell_add[:, :]

    for jj in range(0, cell_n):
      for ii in range(0, cell_m):
        dep_sub_writeout[icount, 0] = i + m_start - 1
        dep_sub_writeout[icount, 1] = j + n_start - 1
        dep_sub_writeout[icount, 1 + (jj - 1) * cell_n + ii] = dep_cell_add[jj, ii]
    icount = icount + 1

dep_level = dep_full
dep_level[dep_full < 0.0] = 0.0

#% output subgrid
dep_sub = np.zeros((ny_total, nx_total))

for j in range(0, ny_total):
  for i in range(0, nx_total):
    n1 = (j - 1) * cell_n + 1
    n2 = n1 + cell_n - 1
    m1 = (i - 1) * cell_m + 1
    m2 = m1 + cell_m - 1
    dep_sub[j, i] = np.sum(np.sum(dep_level[n1:n2, m1:m2])) / cell_m / cell_m

fig1 = plt.figure(1)
#clf
plt.pcolormesh(-dep_full) #,shading flat
plt.colorbar()
tit = 'm x n = ' + str(m) + 'x' + str(n)
plt.title(tit)
plt.savefig("plots/full_grid_2d.png") #print('-djpeg',['plots/full_grid_2d.jpg'])

fig2 = plt.figure(2)
#clf
plt.pcolormesh(-dep_sub)
plt.colorbar()
tit = 'sub m x n = ' + str(nx_total) + 'x' + str(ny_total)
plt.title(tit)
plt.savefig("plots/sub_grid_2d.png") #print('-djpeg',['plots/sub_grid_2d.jpg'])

np.savetxt("dep_sub_500x30.txt", dep_sub) #save -ASCII dep_sub_500x30.txt dep_sub FIXME
np.savetxt("dep_full_2000x120.txt", dep_full) #save -ASCII dep_full_2000x120.txt dep_full FIXME
#fopen('dep_sub_info.txt', 'wt')
np.savetxt("dep_sub_info.txt", dep_sub_writeout) #fprintf(fid, ['%5d','%5d', repmat('%6.1f',1,cell_m*cell_n),'\n'], dep_sub_writeout'); FIXME
#fclose(fid);