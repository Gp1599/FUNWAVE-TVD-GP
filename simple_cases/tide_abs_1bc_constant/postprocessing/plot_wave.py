import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#clear all
fdir = '../../../../simulationRuns/tide_abs_1bc_constant/output/'

eta = np.loadtxt(fdir + 'eta_00000')
n = 1
m = 1
etaShape = np.shape(eta)
if len(etaShape) <= 1:
    m = etaShape[0]
else:
    n, m = np.shape(eta)
dx = 2.0

x = np.arange(0, m) * dx

#% wavemaker and sponge
tdw = 30 * dx
wd = 10.0
wc = 150
x_wm = np.array([wc - wd, wc + wd])
xw_sponge = np.array([0, tdw])
xe_sponge = np.array([x[-1] - tdw, x[-1]])

ns = 0
ne = 199

#ns = 100
#ne = ns

figure_w = 8
figure_l = 4

#clf
fig = plt.figure(0, (figure_w, figure_l))
a = plt.subplot()

def createFrame(i): #for num in range(ns, ne):
    fnum = '%.5d' % (ns + i)
    eta = np.loadtxt(fdir + 'eta_' + fnum)

    plt.cla()
    plt.grid(visible = True)
    plt.plot([x_wm[0],      x_wm[0]],       [-10, 10], 'r')
    plt.plot([x_wm[1],      x_wm[1]],       [-10, 10], 'r')
    plt.plot([xw_sponge[0], xw_sponge[0]],  [-10, 10], 'r--')
    plt.plot([xw_sponge[1], xw_sponge[1]],  [-10, 10], 'r--')
    plt.plot([xe_sponge[0], xe_sponge[0]],  [-10, 10], 'r--')
    plt.plot([xe_sponge[1], xe_sponge[1]],  [-10, 10], 'r--')

    plt.xlabel('x(m)')
    plt.ylabel('eta(m)')
    #set(gcf,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);
    #clf
    etaShape = np.shape(eta)
    if len(etaShape) <= 1:
        #print(len(eta))
        #print(len(x))
        plt.plot(x, eta)
    else:
        plt.plot(x, eta[0, :])
    #hold on
    

    #%axis([0 1024 -1 1])
    #     
    #plt.pause(0.1)
    
    #currframe=getframe(gcf);
        #writeVideo(vidObj,currframe);  % Get each recorded frame and write it to filename defined above
    return a
    

#framei = 0
#for i in range(ns, ne):
    #createFrame(framei)
    #framei += 1

a = anim.FuncAnimation(fig = fig, func = createFrame, frames = ne - ns) #vidObj = VideoWriter('movie.avi');  % Set filename to write video file
#vidObj.FrameRate=10;  % Define the playback framerate [frames/sec]
#open(vidObj);
a.save("movieII.mp4", writer = "ffmpeg", fps = 10) #videoCreator.save("movieII.avi") #close(vidObj)