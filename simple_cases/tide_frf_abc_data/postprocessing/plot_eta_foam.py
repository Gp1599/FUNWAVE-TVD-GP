import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import curl

#clear all

#% folder of results
fdir_results = '/Volumes/BigSur_2022/FRF_TIDE/Case_15deg_longrun/';

#% dimensions
m = 660
n = 800
DimsX = [m, n]

dep = np.loadtxt(fdir_results + 'dep.out')
# fclose(fileID);

dep = np.transpose(dep)
dep = np.flipud(dep)
dep = np.fliplr(dep)


#% image from google earth, not the frf bathy has a rotation, cannot use google_map
RGB = plt.imread('frf_03.jpg')

#% match (x,y) and image approximately
x = np.arange(0, m) * 1 + 105
y = np.arange(n, 1, -1) * 1.0 + 220
[X, Y] = np.meshgrid(x, y)

#% file range
files=[1, 20, 57]


#clf
#colormap jet
figure_w = 10
figure_l = 12
fig = plt.figure(0, (figure_w, figure_l)) #set(fig,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);


for k in range(0, len(files)): 

    numb = files[k]

    fnum = '%.5d' % numb

    #% read files -----------------------
    #fname = [];
    #fileID=fopen(fname);
    eta = np.loadtxt(fdir_results + 'eta_' + fnum) #fread(fileID,DimsX{1},'*single');
    #fclose(fileID);

    eta = np.transpose(eta)
    eta = np.flipud(eta)
    eta = np.fliplr(eta)

    #fname = [fdir_results 'mask_' fnum];
    #fileID=fopen(fname);
    mask = np.loadtxt(fname) #fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    mask = np.transpose(mask)
    mask = np.flipud(mask)
    mask = np.fliplr(mask)

    #fname=[fdir_results 'age_' fnum];
    #fileID=fopen(fname);
    age = np.loadtxt(fdir_results + 'age_' + fnum) #fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    age = np.transpose(age)
    age = np.flipud(age)
    age = np.fliplr(age)

    #% read over -------

    #% make up breaker and foam for visualization 

    #% bubbles
    breaker = age
    breaker[breaker>10] = 0.0 #;  % bubble last 10 sec

    bubble = breaker
    bubble[bubble==0.0] = 9000.0
    bubble = 1.5 * np.exp(-bubble / 10)
    bubble[bubble < 0.1] = np.nan

    #% foam
    age[age > 600.0] = 0.0
    age[mask < 1] = np.nan
    foam = age
    foam[foam == 0.0] = 9000.0
    foam = 1.0 * np.exp(-foam/50)

    #% eta without breaker
    eta[mask < 1] = np.nan
    eta[breaker > 0] = np.nan

    plt.subplot(3, 2, (k - 1) * 2 + 1)
    B = np.rot90(RGB)
    plt.imshow(B)
    #hold on
    plt.pcolormesh(X, Y, eta) #,shading flat
    plt.pcolormesh(X, Y, bubble) #,shading flat

    #caxis([-1 3.5])
    plt.plot([110, 500], [620, 620], linewidth = 2) #'w:',
    plt.axis([30, 600, 250, 950])
    #colorbar
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')

    tim = '%.2f' % numb*600.0/3600.0

    plt.title('surface elevation, t = ' + tim + ' hr')

    plt.subplot(3, 2, (k - 1) * 2 + 2)
    B = np.rot90(RGB,1)
    plt.imshow(B) #A=imagesc(B);
    #hold on
    plt.pcolormesh(X, Y, foam) #,shading flat
    plt.plot([110, 500],[620, 620], linewidth = 2) #'w:',
    plt.axis([30, 600, 250, 950])
    #caxis([0 2])
    plt.title(['breaking signature'])
    #colorbar
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')

#print -djpeg100 plots_movies/frame6_breaking.jpg
#print -depsc2 plots_movies/frame6_breaking.eps
fig.savefig("plots_movies/frame6_breaking.jpg")




