import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an

# Initialize the path to the directory that contains output files for rip_2d_foam
fdir = '../../../simulationRuns/rip_2D_foam/output/'
outputFileName = "videoOutII.mp4"

# Load the depth matrix
dep = np.loadtxt('depth_a15.txt')

# Initialize Nglob and Mglob from the depth matrix's shape and discretization parameters
[n, m] = np.shape(dep)
DX = 1
DY = 2

# Initialize the coordinates and meshgrid via discretization
x = np.arange(0, m) * DX
y = np.arange(0, n) * DY
[xx, yy] = np.meshgrid(x, y)

#% define movie file and parameters
#myVideo = VideoWriter('videoOut.mp4','MPEG-4');
#myVideo.FrameRate = 2;  
#myVideo.Quality = 100;
vidHeight = 576; #%this is the value in which it should reproduce
vidWidth = 1024; #%this is the value in which it should reproduce
#open(myVideo);

# Initialize the figure dimension hyperparameters
figure_w = 15
figure_l = 8

# Create the figure with the initialized dimension hyperparameters
fig = plt.figure(0, (figure_w, figure_l)) #set(gcf,'units','inches','paperunits','inches','papersize', [wid len],'position',[0.5 2.5 wid len],'paperposition',[0 0 wid len]);
#% previous version (2nd revision) nstart=280
dt = 30

#From: https://www.mathworks.com/help/matlab/ref/curl.html#mw_1bfbc405-c17b-403d-ac3f-4398eeb41a8c
def curl(x, y, XX, YY, U, V):
    # 
    dX = np.zeros((np.shape(XX)))
    dY = np.zeros((np.shape(XX)))

    dY[0, :]                = (U[1, :] - U[0, :]) / (y[1] - y[0])
    dY[len(XX) - 1, :]      = (U[len(XX) - 1, :] - U[len(XX) - 2, :]) / (y[len(XX) - 1] - y[len(XX) - 2])

    dX[:, 0]                = (V[:, 1] - V[:, 0]) / (x[1] - x[0])
    dY[:, len(XX[0]) - 1]   = (V[:, len(XX[0]) - 1] - V[:, len(XX[0]) - 2]) / (x[len(XX[0]) - 1] - x[len(XX[0]) - 2])

    for j in range(1, len(XX) - 1):
        for i in range(1, len(XX[0]) - 1):
            dX[:, i] = (V[:, i + 1] - V[:, i + 1]) / (x[i + 1] - x[i - 1])
            dY[j, :] = (U[j + 1, :] - U[j - 1, :]) / (y[j + 1] - y[j - 1])

    return dX - dY

# Function for every frame for the output video 
def update(frame):
    global x, y
    
    time = ((frame + 3) - 1) * dt
    num = ((frame + 3) - 1)
    num_avg = np.floor(time / 50)

    # Load the ETA, MASK, and FoamETA matrices
    fnum = '%.5d' % num
    eta = np.loadtxt(fdir + 'eta_' + fnum)
    mask = np.loadtxt(fdir + 'mask_' + fnum)
    FoamEta = np.loadtxt(fdir + 'FoamEta_' + fnum)

    # Mask the ETA and FoamETA matrices
    eta[mask < 1] = np.nan
    FoamEta[mask < 1] = np.nan

    #% averaged properties
    fnum = '%.5d' % num_avg
    u = np.loadtxt(fdir + 'umean_' + fnum)
    v = np.loadtxt(fdir + 'vmean_' + fnum)

    # Mask the depth file
    dep[mask < 1] = np.nan
    u[mask < 1] = np.nan
    v[mask < 1] = np.nan

    # Initialize the axis limits
    ax = [0, 250, 0, 500]
    #clf

    plt.clf()
    # Initialize the first subplot
    plt.subplot(131)
    # Plot eta
    hp = plt.pcolormesh(xx, yy, eta, vmin = -0.60, vmax = 1.2, cmap = 'jet') #shading interp
    # Initialize the colorbar for the subplot
    h_bar = plt.colorbar(orientation = "horizontal") #('location', 'SouthOutside')
    #h_bar.ax.axis([-0.6, 1.2, 0, 1])
    h_bar.ax.set_xlabel("eta (m)") #set(get(h_bar,'xlabel'),'string','\eta (m)' )

    # Give the axes labels to measure their respective dimensions in meters
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')

    # Apply initialized axis limits to the subplot
    plt.axis(ax)

    #% -------------------
    # Create the second subplot
    plt.subplot(132)

    #[w, w_ang] = np.curl(xx, yy, u, v)
    # Calculate the curl of the meshgrid based on the U and V matrices
    w = curl(x, y, xx, yy, u, v)

    # Apply the colormap to the second subplot
    plt.pcolormesh(xx, yy, w, vmin = -0.055, vmax = .06, cmap = 'jet') #,shading interp;

    # Give the subplot the colorbar to measure vortocity in s^(-1)
    h_bar = plt.colorbar(orientation = "horizontal") #('location', 'SouthOutside')
    #h_bar.ax.axis([-0.055, .06, 0, 1]) #plt.caxis([-.055 .06])
    h_bar.ax.set_xlabel('vorticity (s^{-1})') #(get(h_bar,'xlabel'),'string','vorticity (s^{-1})' )

    # Giving the axes labels to measure their respective dimensions in meters
    plt.xlabel('x (m)')
    #plt.ylabel('y (m)')

    #hold on
    # Create a black-dotted line close to the middle of the subplot
    xm = [140, 140]
    ym = [0, 2000]
    plt.plot(xm, ym, color = 'k', linewidth = 2)

    # Apply the axis limits to the second subplot
    #%axis image,
    plt.axis(ax)

    # Initialize the third subplot
    sp = plt.subplot(133)

    # Apply the jet colormap to the subplot based on the log of the FoamETA matrix
    plt.pcolormesh(xx, yy, np.log(FoamEta), vmin = -10, vmax = 10, cmap = 'jet') #,shading interp;

    # Give the subplot the colorbar to measure foam thickness in log in meters
    h_bar = plt.colorbar(orientation = "horizontal")
    #h_bar.ax.axis([-10, 10, 0, 1]) #plt.caxis([-10 10])
    h_bar.ax.set_xlabel('Foam Thickness (log in meter)') #set(get(h_bar,'xlabel'),'string','Foam Thickness (log in meter)' )
    
    # Apply initialized axis limits to the subplot
    #%axis image, 
    plt.axis(ax)
    
    # Add quivers to the subplot
    #hold on
    s = 20
    sx = 6
    sy = 6
    plt.quiver(xx[0:len(xx):sy, 0:len(xx[0]):sx], yy[0:len(yy):sy, 0:len(yy[0]):sx], s * u[0:len(u):sy, 0:len(u[0]):sx], s * v[0:len(v):sy, 0:len(v[0]):sx]) #, 0)

    # Give the subplot labels to measure respective dimensions in meters
    plt.xlabel('x (m)')
    #plt.ylabel('y (m)')

    #pause(0.1)
    #set(gcf,'PaperPositionMode','auto')

    #% save image
    #F = print('-RGBImage','-r300');
    #%J = imresize(F,[vidHeight vidWidth]);
    #%mov(k).cdata = J;
    #mov(k).cdata = F;

    #writeVideo(myVideo,mov(k).cdata);
    return sp

#for k in range(3, 32):
    #time = (k - 1) * dt
    #num = (k - 1)
    #num_avg = np.floor(time / 50)
    #
    #fnum = '%.5d' %  num
    #eta = np.loadtxt(fdir + 'eta_' + fnum)
    #mask = np.loadtxt(fdir + 'mask_' + fnum)
    #FoamEta = np.loadtxt(fdir + 'FoamEta_' + fnum)
    #eta[mask < 1] = np.nan
    #FoamEta[mask < 1] = np.nan
    #
    #% averaged properties
    #fnum = '%.5d' % num_avg
    #u = np.loadtxt(fdir + 'umean_' + fnum)
    #v = np.loadtxt(fdir + 'vmean_' + fnum)
    #
    #dep[mask < 1] = np.nan
    #u[mask < 1] = np.nan
    #v(mask < 1) = np.nan
    #
    #ax = [0, 250, 0, 500]
    #clf
    #
    #plt.subplot(131)
    ##% plot eta
    #hp = plt.pcolormesh(xx, yy, eta) #shading interp
    ##plt.caxis([-0.6 1.2])
    ##colormap(jet)
    #h_bar = plt.colorbar('location', 'SouthOutside')
    #h_bar.ax.set_xlabel("eta (m)") #set(get(h_bar,'xlabel'),'string','\eta (m)' )
    #
    #plt.xlabel('x (m)')
    #plt.ylabel('y (m)')
    #
    #%axis image, 
    #plt.axis(ax)
    #
    #% -------------------
    #plt.subplot(132)
    #
    #[w, w_ang] = plt.curl(xx,yy,u,v)
    #
    #plt.pcolor(xx,yy,w) #,shading interp;
    #plt.caxis([-.055 .06])
    #h_bar = plt.colorbar('location','SouthOutside');
    #h_bar.ax.set_xlabel('vorticity (s^{-1})') #(get(h_bar,'xlabel'),'string','vorticity (s^{-1})' )
    #
    #plt.xlabel('x (m)')
    #plt.ylabel('y (m)')
    #hold on
    #plt.plot([140, 140], [0, 2000], color = 'k--', linewidth = 2)
    #
    #%axis image, 
    #plt.axis(ax)
    #
    #plt.subplot(133)
    #
    #plt.pcolormesh(xx, yy, np.log(FoamEta)) #,shading interp;
    #h_bar = plt.colorbar('location','SouthOutside')
    #h_bar = 'Foam Thickness (log in meter)' #set(get(h_bar,'xlabel'),'string','Foam Thickness (log in meter)' )
    #%axis image, 
    #plt.axis(ax)
    #plt.caxis([-10 10])
    #hold on
    #s = 20
    #sx = 6
    #sy = 6
    #plt.quiver(xx[0:sy:len(xx), 0:sx:len(xx[0])], yy[1:sy:len(yy), 1:sx:len(yy[0])], s * u[1:sy:len(u), 1:sx:len(u[0])], s * v[1:sy:len(v), 1:sx:len(v[0])], 0, 'w')
    #
    #plt.xlabel('x (m)')
    #plt.ylabel('y (m)')
    #
    #pause(0.1)
    #set(gcf,'PaperPositionMode','auto')
    #
    #% save image
    #F = print('-RGBImage','-r300');
    #%J = imresize(F,[vidHeight vidWidth]);
    #%mov(k).cdata = J;
    #mov(k).cdata = F;
    #
    #writeVideo(myVideo,mov(k).cdata);

#close(myVideo)

# save the video into a video (from: https://www.youtube.com/watch?v=WXv7HQr_8SU)
anim = an.FuncAnimation(fig = fig, func = update, frames = 3)
anim.save(outputFileName, writer = "ffmpeg", fps = 2)

#print -djpeg100 eta_vor_foam.jpg