### PLOT WAVE for 2D CASE ###

# import necessary modules
import numpy as np               
import matplotlib.pyplot as plt

import os

# write your OWN PC folder path for fdir
# Remember that we use for Mac & Linux machines '/', while on windows '\', the r denotes raw string
#fdir = r'/Users/Gaby/Desktop/Postprocessing-Workshop/simple_cases_output/beach_2D/beach_2D/'
fdir = "../../../../simulationRuns/beach2D/output/"

# upload eta file
eta = np.loadtxt(os.path.join(fdir,'eta_00001'))
# define plot location
n,m = np.shape(eta)
dx = 2.0
dy = 2.0

# define sponge and wavemaker location
x = np.asarray([float(xa)*dx for xa in range(m)])
y = np.asarray([float(ya)*dy for ya in range(n)])

x_sponge = [0,100,100,0,0]
y_sponge = [0,0,y[len(y)-1],y[len(y)-1],0]

x_wavemaker = [150, 160, 160, 150, 150]
y_wavemaker = [0, 0, y[len(y)-1],y[len(y)-1],0]

nfile = [1]     # range of eta files you want to plot
min = ['200']   # time  you want to plot

# figure size option 
wid=8    # width
length=5 # length

# plot figure
fig = plt.figure(figsize = (wid,length),dpi=200)

#Gabriel's class blueprint to represent a plot to be used for beach 2D
class Beach2DPlot:

    def __init__(self, fileNumber):
        self.fileNumber = fileNumber
        # Referring to Gabriela's code
        fileNumberStr = str('%0.5d' % fileNumber)
        self.u = np.loadtxt(os.path.join(fdir,'umean_' + fileNumberStr))
        self.v = np.loadtxt(os.path.join(fdir,'vmean_' + fileNumberStr))
        self.ht = np.loadtxt(os.path.join(fdir,'Hsig_' + fileNumberStr))
        self.mask = np.loadtxt(os.path.join(fdir, 'mask_' + fileNumberStr))

        # do not plot values where mask = 0
        self.u_masked = np.ma.masked_where(self.mask==0,self.u)
        self.v_masked = np.ma.masked_where(self.mask==0,self.v)
        self.ht_masked = np.ma.masked_where(self.mask==0,self.ht)

    def putIn(self, fig, testFileQuantity, i):
        global x
        global y
        global x_sponge
        global y_sponge
        global min
        global wid
        global length

        ax = fig.add_subplot(1, testFileQuantity, i + 1)
        fig.subplots_adjust(hspace=1,wspace=.25)
        plt.pcolor(x, y, self.ht_masked, cmap='coolwarm')

        title = 'Time = ' + min[i] + ' sec'
        plt.title(title)
        #plt.hold(True)

        sk=8

        # plot current vectors
        Q = plt.quiver(x[0:len(x)-1:sk],y[0:len(y)-1:sk],self.u[0:len(self.u)-1:sk,0:len(self.u)-1:sk],self.v[0:len(self.v)-1:sk,0:len(self.v)-1:sk],color='w')
        qk = plt.quiverkey(Q, 0.91, 0.91, 0.1, r'$0.1 \frac{m}{s}$', labelpos='E',
                            coordinates='figure',color='k')

        # plot wavemaker and sponge
        plt.plot(x_sponge,y_sponge,'g--',linewidth=3)
        plt.text(50,500,'Sponge',color='g',rotation=90)#;

        plt.plot(x_wavemaker,y_wavemaker,'k-',linewidth=3)
        plt.text(180,700,'Wavemaker',color='k',rotation=90)#;

        if i == 0:
            plt.ylabel('Y (m)')
            plt.xlabel('X (m)')
        else:
            plt.xlabel('X (m)')
            cbar = plt.colorbar()
            cbar.set_label('Hsig (m)', rotation=90)

i = 0
testFileQuantity = len(nfile)
for p in [Beach2DPlot(num) for num in nfile]:
    p.putIn(fig, testFileQuantity, i)
    i += 1

# save figure        
fig.savefig('curr_2d_wave.png', dpi=fig.dpi)

#for num in range(len(nfile)):
    #fnum= '%.5d' % nfile[num]
    #u = np.loadtxt(os.path.join(fdir,'umean_'+fnum))
    #v = np.loadtxt(os.path.join(fdir,'vmean_'+fnum))
    #ht = np.loadtxt(os.path.join(fdir,'Hsig_'+fnum))
    #mask = np.loadtxt(os.path.join(fdir, 'mask_'+fnum))
    
    # do not plot values where mask = 0
    #u_masked = np.ma.masked_where(mask==0,u)
    #v_masked = np.ma.masked_where(mask==0,v)
    #ht_masked = np.ma.masked_where(mask==0,ht)

    #ax = fig.add_subplot(1,len(nfile),num+1)
    #fig.subplots_adjust(hspace=1,wspace=.25)
    #plt.pcolor(x, y, ht_masked,cmap='coolwarm')
    
    #title = 'Time = '+min[num]+ ' sec'
    #plt.title(title)
    #plt.hold(True)

    #sk=8

    # plot current vectors
    #Q = plt.quiver(x[0:len(x)-1:sk],y[0:len(y)-1:sk],u[0:len(u)-1:sk,0:len(u)-1:sk],v[0:len(v)-1:sk,0:len(v)-1:sk],color='w')
    #qk = plt.quiverkey(Q, 0.91, 0.91, 0.1, r'$0.1 \frac{m}{s}$', labelpos='E',
    #                   coordinates='figure',color='k')

    
    # plot wavemaker and sponge
    #plt.plot(x_sponge,y_sponge,'g--',linewidth=3)
    #plt.text(50,500,'Sponge',color='g',rotation=90);
    
    #plt.plot(x_wavemaker,y_wavemaker,'k-',linewidth=3)
    #plt.text(180,700,'Wavemaker',color='k',rotation=90);
    
    #if num == 0:
    #    plt.ylabel('Y (m)')
    #    plt.xlabel('X (m)')
    #else:
    #    plt.xlabel('X (m)')
    #    cbar = plt.colorbar()
    #    cbar.set_label('Hsig (m)', rotation=90)

# save figure        
#fig.savefig('curr_2d_wave.png', dpi=fig.dpi)