import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#clear all
fdir = '../../../simulationRuns/tide_time_spectra/output/' #'./output/';

SLP = 0.05
Xslp = 300.0
DEPTH_FLAT = 8.0

eta = np.loadtxt(fdir + 'eta_00001')

[n, m] = np.shape(eta)
dx = 2.0
dy = 2.0
x = np.arange(0, m) * dx
y = np.arange(0, n) * dy
XX, YY = np.meshgrid(x, y)

dep = np.zeros((m))
for i in range(0, m):
    if x[i] < Xslp:
        dep[i] = -DEPTH_FLAT
    else:
        dep[i] = -DEPTH_FLAT + SLP * (x[i] - Xslp)

nfile = np.arange(1, 99, 1)

#colormap jet
figure_w = 8
figure_h = 5
figure = plt.figure(0, (figure_w, figure_h)) #set(gcf,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);

def createFrame(i): #for num in range(0, len(nfile)):
    fnum = '%.5d' % nfile[i]
    eta = np.loadtxt(fdir + 'eta_' + fnum)
    mask = np.loadtxt(fdir + 'mask_' + fnum)

    eta[mask == 0] = np.nan

    plt.clf()

    
    #clf
    left_subplot = plt.subplot(1, 2, 1, projection = "3d")
    left_subplot.plot_surface(XX, YY, eta, cmap = "jet", antialiased = False) #plt.plot(x, eta[int(np.floor(n / 2)), :], zs = 100, zdir = 'y') #plt.mesh(x, y, eta)
    plt.axis([0, x[-1], 0, y[-1], -2, 4])
    #plt.view(17, 16)

    right_subplot = plt.subplot(1, 2, 2)
    plt.grid(visible = True)
    plt.plot(x, eta[int(np.floor(n / 2)), :])
    #hold on
    plt.plot(x, dep, 'k-')
    plt.axis([0, x[-1], -2, 4])

    if i == 0:
        plt.ylabel(' y (m) ')

    plt.xlabel(' x (m) ')
    #cbar = plt.colorbar()
    #cbar.ax.set_ylabel("eta (m)") #%set(get(cbar,'ylabel'),'String','\eta (m) ')
    plt.title('time = ' + str(i * 2) + ' sec')

    #set(gcf,'Renderer','zbuffer')

    #pause(0.1)

    #F = print('-RGBImage','-r300');
    #J = imresize(F,[vidHeight vidWidth]);
    #mov(num).cdata = J;

    #writeVideo(myVideo,mov(num).cdata);

    #end
    return right_subplot
#close(myVideo)

#myVideo = VideoWriter('videoOut.mp4','MPEG-4');
#myVideo.FrameRate = 10;  
#myVideo.Quality = 100;
#vidHeight = 576; %this is the value in which it should reproduce
#vidWidth = 1024; %this is the value in which it should reproduce
#open(myVideo);
output = anim.FuncAnimation(fig = figure, func = createFrame, frames = len(nfile))
output.save("videoOutII.mp4", writer = "ffmpeg", fps = 10)
#%print -djpeg eta_inlet_shoal_irr.jpg