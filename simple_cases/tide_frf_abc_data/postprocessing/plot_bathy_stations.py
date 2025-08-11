import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import curl

#clear all

#% folder of results
fdir_results = '/Volumes/BigSur_2022/FRF_TIDE/Case_15deg/'

#% dimensions
m = 660
n = 800
DimsX = [m, n]

station = np.loadtxt('../work/station.txt')
sta_i = station[:, 0]
sta_j = station[:, 1]

#% depth
fname=[fdir_results 'dep.out'];
fileID= fopen(fname);
dep = np.loadtxt(fdir_results + 'dep.out') #fread(fileID,DimsX{1},'*single');
#fclose(fileID);
dep = np.transpose(dep) #dep';
dep = np.flipud(dep)
dep = np.fliplr(dep)


#% image from google earth, not the frf bathy has a rotation, cannot use google_map
RGB = plt.imread('frf_03.jpg')

#% match (x,y) and image approximately
x = np.loadtxt(0, m) * 1 + 105
y = np.loadtxt(n,1,-1) * 1.0 + 220
[X, Y] = np.meshgrid(x, y)

fig = plt.figure[1]
#clf
#colormap jet
figure_w = 6
figure_l = 8
#set(fig,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);

#% read over -------

#% make up breaker and foam for visualization 


#% eta without breaker
dep[dep < 0] = np.nan

B = np.rot90(RGB) #imrotate(RGB,1);
plt.imshow(B) #A=imagesc(B);
#hold on
plt.pcolormesh(X, Y, -dep) #,shading flat
for k in range(0, len(station)):
    plt.plot(X(sta_j(k),sta_i(k)),Y(sta_j(k),sta_i(k)),'ko','MarkerFaceColor','r')
    txt = 'G' + ('%.d' % (14-k))
    plt.text(X[sta_j[k], sta_i[k]] - 20, Y[sta_j[k] - 15, sta_i[k]], txt, fontsize = 8, color = 'w')
    

#caxis([-10 5])
plt.plot([110, 500],[620, 620], linewidth = 2) #'w:',
plt.axis([30, 765, 250, 950])

#colorbar
plt.xlabel('x (m)')
plt.ylabel('y (m)')

#print -djpeg100 plots_movies/depth_station.jpg
#print -depsc2 plots_movies/depth_station.eps

plt.savefig("plots_movies/depth_station.png")