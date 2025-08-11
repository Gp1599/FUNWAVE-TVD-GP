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

#% depth
dep = np.transpose(np.loadtxt(fdir_results + 'dep.out'))
dep = np.transpose(dep) #dep=dep';
dep = np.flipud(dep)
dep = np.fliplr(dep)

#% image from google earth, not the frf bathy has a rotation, cannot use google_map
RGB = plt.imread('frf_03.jpg')

#% match (x,y) and image approximately
x = np.arange(0, m) * 1 + 105
y = np.arange(n, 0, -1) * 1.0 + 180
[X, Y] = np.meshgrid(x, y)

#% file range
files = np.arange(1, 119)

fig = plt.figure(0)
#colormap jet

def createFrame(k): #for k=1:length(files) 

    numb = files[k]

    fnum = '%.5d' % numb

    #% read files -----------------------
    #fname=[];
    #fileID=fopen(fname);
    eta = np.loadtxt(fdir_results + 'etamean_' + fnum) #fread(fileID,DimsX{1},'*single');
    #fclose(fileID);

    eta = np.transpose(eta) #eta';
    eta = np.flipud(eta)
    eta = np.fliplr(eta)

    #fname=[];
    #fileID=fopen(fname);
    um = np.loadtxt(fdir_results + 'umean_' + fnum) #fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    um = np.transpose(um) #um';
    um = np.flipud(um)
    um = -np.fliplr(um)

    #fname=[fdir_results 'vmean_' fnum];
    #fileID=fopen(fname);
    vm = np.loadtxt(fdir_results + 'vmean_' + fnum) #fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    vm = np.transpose(vm) #vm';
    vm = np.flipud(vm)
    vm = np.fliplr(vm)

    [vort, vort1] = curl.execute(X, Y, um, vm)

    #% read over -------


    #clf

    plt.subplot(121)
    B = np.rot90(RGB)#, 1);
    #A = imagesc(B);
    plt.imshow(B)
    #hold on
    plt.pcolormesh(X, Y, eta) #,shading flat

    #caxis([0 1.5])
    plt.plot([110, 500], [620, 620], 'w:', linewidth = 2)
    plt.axis([30, 600, 250, 950])

    tim = '%.1f' % 1000 + numb * 2000.0 

    plt.title('time = ' + tim + ' sec')

    plt.subplot(122)
    B = np.rot90(RGB) #imrotate(RGB,1);
    plt.imshow(B) #A=imagesc(B);
    #hold on
    plt.pcolormesh(X, Y, vort) #,shading flat
    plt.plot([110, 500], [620, 620],'w:', linewidth = 2)
    sk = 16
    sc = 4
    plt.quiver(X[0:len(X):sk, 0:len(X[0]):sk], Y[0:len(Y):sk, 0:len(Y[0]):sk], um[0:len(um):sk, 0:len(um[0]):sk] * sc, vm[1:len(vm):sk, 1:len(vm[0]):sk] * sc, 0, color = 'k')
    plt.axis(30, 600, 250, 950)
    #caxis([-0.5 0.5])
    plt.title('time = ' + tim + ' sec')

    #pause(0.1)


    #% save image
    #F = print('-RGBImage','-r300');
    #J = plt.imresize(F,[vidHeight vidWidth]);
    #mov(k).cdata = J;

    #writeVideo(myVideo,mov(k).cdata);


#% define movie file and parameters
#myVideo = VideoWriter('videoOut.mp4','MPEG-4');
#myVideo.FrameRate = 10;  
#myVideo.Quality = 100;
#vidHeight = 576; %this is the value in which it should reproduce
#vidWidth = 1024; %this is the value in which it should reproduce
#open(myVideo);
myVideo = anim.FuncAnimation(fig = fig, func = createFrame, frames = len(files))
myVideo.save("videoOutIII.mp4", "ffmpeg", fps = 10)
#close(myVideo)