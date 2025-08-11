import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#clear all

#% folder of results
fdir_results='/Volumes/BigSur_2022/FRF_TIDE/Case_15deg_longrun/';

#% dimensions
m = 660
n = 800
DimsX = [m, n]

#% depth
#fname = 
#fileID=fopen(fname);
dep = np.loadtxt(fdir_results + 'dep.out') #dep=fread(fileID,DimsX{1},'*single');
#fclose(fileID);
dep = np.transpose(dep)
dep = np.flipud(dep)
dep = np.fliplr(dep)


#% image from google earth, not the frf bathy has a rotation, cannot use google_map
RGB = plt.imread('frf_03.jpg')

#% match (x,y) and image approximately
x = np.arange(1, m) * 1 + 105
y = np.arange(n, 1, -1) * 1.0 + 220
[X, Y] = np.meshgrid(x, y)




#% file range
files = [1, 158]

fig = plt.figure(0)
#colormap jet
figure_w = 15
figure_l = 8
fig = plt.figure(0, (figure_w, figure_l)) #set(fig,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);

def createFrame(k): #for k = 1:length(files) 
    numb = files[k]

    fnum = '%.5d' % numb

    #% read files -----------------------
    eta= np.loadtxt(fdir_results + 'eta_' + fnum) #(fileID,DimsX{1},'*single');
    #fclose(fileID);

    eta = np.transpose(eta)
    eta = np.flipud(eta)
    eta = np.fliplr(eta)

    #fname = 
    #fileID=fopen(fname);
    mask= np.loadtxt(fdir_results + 'mask_' + fnum) #fread(fileID,DimsX{1},'*single');
    #fclose(fileID);
    mask = np.transpose(mask)
    mask = np.flipud(mask)
    mask = np.fliplr(mask)

    #fname = 
    #fileID = fopen(fname)
    age = np.loadtxt(fdir_results + 'age_' + fnum) #fread(fileID,DimsX{1},'*single')
    #fclose(fileID);
    age = np.transpose(age)
    age = np.flipud(age)
    age = np.fliplr(age)

    #% read over -------

    #% make up breaker and foam for visualization 

    #% bubbles
    breaker = age
    breaker[breaker > 10] = 0.0;  #% bubble last 10 sec

    bubble = breaker
    bubble[bubble == 0.0] = 9000.0
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

    #clf

    plt.subplot(121)
    B = np.rot90(RGB) #imrotate(RGB,1)
    plt.imshow(B) #A = imagesc(B)
    #hold on
    plt.pcolormesh(X, Y, eta, vmin = -1, vmax = 3.5) #,shading flat
    plt.pcolormesh(X, Y, bubble, vmin = -1, vmax = 3.5) #,shading flat

    #caxis([-1 3.5])
    plt.plot([110, 500], [620, 620], 'w:', linewidth = 2)
    plt.axis([30, 600, 250, 950])

    tim = str(numb * 600.0/3600.0, '%.2f')

    plt.title('time = ' + tim + ' hr')

    plt.subplot(122)
    B = np.rot90(RGB) #imrotate(RGB,1)
    plt.imshow(B) #A = imagesc(B)
    #hold on
    plt.pcolormesh(X, Y, foam, vmin = 0, vmax = 2) #,shading flat
    plt.plot([110, 500], [620, 620], 'w:', linewidth = 2)
    plt.axis([30, 600, 250, 950])
    #caxis([0 2])
    plt.title('time = ' + tim + ' hr')

    #pause(0.1)


    #% save image
    #F = print('-RGBImage','-r300');
    #J = imresize(F, [vidHeight vidWidth]);
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
myVideo.save("videoOutII.mp4", "ffmpeg", framerate = 10)
#close(myVideo)