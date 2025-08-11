import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#clear all
fdir = 'output/'
fdir1 = 'output_nopropeller/'

dep = np.loadtxt(fdir + 'dep_00000')


[n, m] = np.shape(dep)

dx = 2.0
dy = 2.0
x = np.arange(0, m) * dx
y = np.arange(0, n) * dy



nfile = np.arange(1, 75)




figure_w = 8
figure_l = 6
fig = plt.figure(0, (figure_w, figure_l)) #set(gcf,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);
#clf
#colormap jet

def createFrame(num): #for num in range(0, len(nfile)): 
    fnum = '%.5d' % nfile[num]
    eta = np.loadtxt(fdir + 'eta_' + fnum)
    ch = np.loadtxt(fdir + 'C_' + fnum)
    ds = np.loadtxt(fdir + 'DchgS_' + fnum)
    db = np.loadtxt(fdir + 'DchgB_' + fnum)

    eta1 = np.loadtxt(fdir1 + 'eta_' + fnum)
    ch1 = np.loadtxt(fdir1 + 'C_' + fnum)
    ds1 = np.loadtxt(fdir1 + 'DchgS_' + fnum)
    db1 = np.loadtxt(fdir1 + 'DchgB_' + fnum)

    plt.subplot(311)
    plt.pcolormesh(x, y, eta, cmap = 'jet', vmin = -0.3, vmax = 1.5) #caxis([-0.3 1.5]),shading flat
    #hold on

    plt.title(' Time = ' + str(nfile(num) * 1.0) + ' sec ')

    cbar = plt.colorbar()
    cbar.ax.set_ylabel("eta (m)") #set(get(cbar,'ylabel'),'String',' \eta (m) ')


    #%xlabel(' x (m) ')
    plt.ylabel(' y (m) ')

    plt.subplot(312)
    plt.pcolormesh(x, y, ch1 * 100, cmap = 'jet', vmin = 0.0, vmax = 0.01) #caxis([0.0 0.01]),shading flat
    #hold on

    cbar = plt.colorbar()
    cbar.ax.set_ylabel(" c ") #set(get(cbar,'ylabel'),'String',' c ')
    plt.title('Sediment concentration without propeller')

    #%xlabel(' x (m) ')
    plt.ylabel(' y (m) ')


    plt.subplot(313)
    plt.pcolormesh(x, y, ch * 100, cmap = 'jet', vmin = 0.0, vmax = 0.01) #,shading flat
    #hold on
    #caxis([0.0 0.01])
    cbar = plt.colorbar()
    cbar.ax.set_ylabel(" c ") #set(get(cbar,'ylabel'),'String',' c ')
    plt.title('Sediment concentration with propeller')


    #pause(0.1)

    #F = print('-RGBImage','-r300');
    #mov(num).cdata = F;

    #writeVideo(myVideo,mov(num).cdata);

#myVideo = VideoWriter('videoOut.mp4','MPEG-4');
#myVideo.FrameRate = 10;  
#myVideo.Quality = 100;
#%vidHeight = 576; %this is the value in which it should reproduce
#%vidWidth = 1024; %this is the value in which it should reproduce
#open(myVideo);
animation = anim.FuncAnimation(fig = fig, func = createFrame, frames = len(nfile))
animation.save("videoOutII.mp4", "ffmpeg", 10)
#close(myVideo)
