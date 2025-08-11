### PLOT Tohoku_tsunami WAVE ###

# import necessary modules
import numpy as np               
import matplotlib.pyplot as plt
import matplotlib as mat

# write your OWN PC folder path for fdir and dep
# Remember that we use for Mac & Linux machines '/', while on windows '\'
dir = "../../../../simulationRuns/tohoku_tsunami/"
dep = np.loadtxt(dir + 'external_files/depth_30min.txt')

fdir = dir + "output/"

# define bathy location
n, m = np.shape(dep)
dx = 0.5
dy = 0.5

x = np.asarray([float(xa) * dx + 132.01667 for xa in range(m)])
y = np.asarray([float(ya) * dy - 59.98333 for ya in range(n)])

nfile = [   2,      5,      9   ]    # range of eta files you want to plot
hr =    [   '1',    '4',    '8' ]    # time  you want to plot

# figure size option 
figure_w = 5    # width
figure_l = 7    # length

# Plot figure
fig = plt.figure(figsize = (figure_w, figure_l), dpi = 200)

# The helper function for each test file number
def executeFile(num):
    global nfile
    global hr
    global x, y
    global dep

    # Initializing the eta matrix and it's masked duplicate
    fnum = '%.5d' % nfile[num]
    eta = np.loadtxt(fdir + 'eta_' + fnum)
    eta_masked = np.ma.masked_where(dep < 0, eta) # do nt plot where dep < 0

    # Initializing the subpplot
    ax = fig.add_subplot(len(nfile), 1, num + 1)
    fig.subplots_adjust(hspace = .45)

    # Applying the jet colormap to the subplot
    plt.pcolor(x, y, eta_masked, cmap = 'jet')

    # Giving the suplot the title to indicate its corresponding minimum time measured in hours
    title = 'Time = ' + hr[num] + ' hr'
    plt.title(title)

    # Tightening the subplot's axes
    plt.axis('tight')

    # Giving the x and y axes names to measure longitude and latitude both measured in degrees
    plt.ylabel('Lat (deg)')
    plt.xlabel('Lon (deg)')

    # Adding a colorbar to the subplot and labeling that colorbar to measure U in meters
    cbar = plt.colorbar()
    cbar.set_label(r'$\eta$' + ' (m)', rotation = 90)

    # Setting the image limits of the subplots
    if num == 0:
        plt.clim(-0.5, 0.5)
    else:
        plt.clim(-0.05, 0.05)

    # Updating matplotlib's font size to 10
    mat.rcParams.update({'font.size': 10})

# Create a subplot corresponding to each test file
for num in range(len(nfile)):
    executeFile(num)
    #fnum= '%.5d' % nfile[num]
    #eta = np.loadtxt(fdir+'eta_'+fnum)
    #eta_masked = np.ma.masked_where(dep<0,eta) # do nt plot where dep<0

    #ax = fig.add_subplot(len(nfile),1,num+1)
    #fig.subplots_adjust(hspace=.45)
    #plt.pcolor(x, y, eta_masked,cmap='jet')

    #title = 'Time = '+hr[num]+ ' hr'
    #plt.title(title)
    #plt.axis('tight')

    #plt.ylabel('Lat (deg)')
    #plt.xlabel('Lon (deg)')
    #cbar=plt.colorbar()
    #cbar.set_label(r'$\eta$'+' (m)', rotation=90)

    #if num == 0:
    #    plt.clim(-0.5, 0.5)
    #else:
    #    plt.clim(-0.05, 0.05)

    #mat.rcParams.update({'font.size': 10})

# Finish the main figure by saving it 
fig.savefig('eta_tsunami.png', dpi = fig.dpi)