import numpy as np
import matplotlib.pyplot as plt

# Initialize the path to the directory that had files for the IG_waves case
fdir = "../../../../simulationRuns/IG_waves/"

# Initializing the gravity constant
G = 9.81

# Initialize the H and Peakf variables
otherp = np.loadtxt("SPC_dep_pf.txt")

h = otherp[0]
peakf = otherp[1]

# Load the FRE matrix
fre = np.loadtxt('SPC_frq.txt')
#fre = fre.reshape((1, 2))

# Load the Angle & SPC matrix
angle = np.loadtxt('SPC_angle.txt')
spc = np.loadtxt("SPC_HMO.txt")

# Transpose the SPC matrix
spc = np.transpose(spc)

# Initialize the AMP and PHI rows
Amp_each = np.sqrt(2) / 4.0 * np.transpose(spc)
Phi_each = np.zeros(len(Amp_each))

# Initialize the Omega each 
Omega_each = (2 * np.pi) * fre

# Seeting the random seed to 1
np.random.seed(1)

# Modify PHI 
Phi_each = 2 * np.pi * np.transpose(np.random.rand(len(Phi_each)))

# Initialize m as the length of Amp_each
m = len(Amp_each)

def wvnum_omvec(h, o, g):
    # first guess
    k = (o * o / g) / np.sqrt(np.tanh(o * o * h / g))

    # Newton Raphson
    error = np.transpose(np.ones(1))
    while np.any(np.abs(error) > .000001):
        f = o * o - g * k * (np.tanh(k * h))
        fp = -g * np.tanh(k * h) - g * (k * h) / np.pow(np.cosh(k * h), 2)
        kn = k - f / fp
        error = np.abs(kn - k) / k
        k = kn
    return k

anm = np.zeros((m, 1))
Fnm = np.zeros((m, 1))
Knm = np.zeros((m, 1))
OMEGA_nm = np.zeros((m, 1))
fre_used = np.zeros((m, 1))
spc_used = np.zeros((m, 1))

PHI_nm = np.zeros((m, 1))
icount = 0
for i in range(0, m - 1):
    for j in range(i + 1, m):
        a = np.array([Amp_each[i], Amp_each[j]])
        f = np.array([fre[i], fre[j]])

        # Sort out using low frequency range
        fnm = np.diff(f) 
        
        omega = 2 * np.pi * f
        k = wvnum_omvec(h, omega, G)
        lamb = 2 * np.pi / k
        knm = np.diff(k)
        omega_nm = 2 * np.pi * fnm
        C = (omega[0] - omega[1]) * (np.pow((omega[0] * omega[1]), 2) / np.pow(G, 2) + k[0] * k[1]) - 0.5 * (omega[0] * np.pow(k[1], 2) / np.pow(np.cosh(k[1] * h), 2) - omega[1] * np.pow(k[0], 2) / np.pow(np.cosh(k[0] * h), 2))

        Dnm = G * k[0] * k[1] / (2 * omega[0] * omega[1]) + (np.pow(omega[1], 2) + np.pow(omega[1], 2) - omega[0] * omega[1]) / (2 * G) - (C * G * (omega[0] - omega[1]) / (omega[0] * omega[1] * (G * knm * np.tanh(knm * h) - (omega[0] - np.pow(omega[1], 2)))))

        anm[icount, 0] = Dnm * a[0] * a[1]

        Fnm[icount, 0] = fnm
        Knm[icount, 0] = knm
        OMEGA_nm[icount, 0] = 2 * np.pi * fnm
        PHI_nm[icount, 0] = Phi_each[j] - Phi_each[i]
        fre_used[icount, 0] = fre[i]
        spc_used[icount, 0] = spc[i]
        icount += 1

# arange freq from small to large with resolution
freq_low = Fnm
anm_low = anm
phase_low = PHI_nm
OMEGA_nm_low = 2 * np.pi * freq_low

# write out for funwave-tvd
def concatMatrices(matrix1, matrix2):
    r1, c1 = np.shape(matrix1)
    r2, c2 = np.shape(matrix2)
    r = r1 + r2
    c = max(c1, c2)

    result = np.zeros((r, c))
    result[0:r1, 0:c1] = matrix1
    result[r1:r, 0:c] = matrix2
    return result

fname = "spectrum two components.txt"
NumFreq = len(fre) + len(freq_low)
NumDir = 1
PeakPeriod = 1. / peakf
Freq = concatMatrices(freq_low, np.array([fre]))
Dire = 0.0
Amp1 = concatMatrices(anm_low, np.array([Amp_each]))
Eng1 = concatMatrices(0.5 * np.pow(anm_low, 2), np.array([0.5 * np.pow(Amp_each, 2)]))
Phase1 = concatMatrices(phase_low, np.array([Phi_each]))

fid = open(fname, 'w')
fid.write("%5i" % NumFreq + " " + "%5i" % NumDir + "    - NumFreq NumDir \n")
fid.write("%10.3f" % PeakPeriod + "    - PeakPeriod    \n")
fid.write("%10.3f" % Freq[0, 0] + "    - Freq \n")
fid.write("%10.3f" % Dire + "    - Dire \n")

fid.close()

time = np.transpose(np.arange(0, 500, 0.5))
#print(Omega_each)
#print(time)
Wave_each = Amp_each * np.cos(Omega_each * time + Phi_each)
Wave_total = np.sum(Wave_each)
IGW_each = anm_low * np.cos(OMEGA_nm_low * time + freq_low + phase_low)
IGW_total = IGW_each

WaveIG_each = Amp1 * np.cos(2 * np.pi * Freq * time + Phase1)
WaveIG_total = np.sum(WaveIG_each)

Etotal = np.sum(sum(np.pow(spc, 2))) / 16.0
Hrms = np.sqrt(8 * Etotal)
Hsig = np.sqrt(16 * Etotal)

E = np.pow(spc, 2) / 8.0

fig = plt.figure(1)
plt.plot(time, Wave_total, 'r')
plt.plot(time, IGW_total, 'b')
plt.grid()
plt.xlabel('time(s)')
plt.ylabel('eta')
plt.title('time series of elevation')
plt.legend('wind wave','IG')
fig.savefig("plots/windwave_and_IG_2comp.png") #print -djpeg100 plots/windwave_and_IG_2comp.jpg

fig2 = plt.figure(2)
plt.plot(time, WaveIG_total)
plt.title('time series of elevation')
plt.legend('wind wave + IG')
plt.grid()
fig2.savefig("plots/wave_plus_IG_2comp.png") #print -djpeg100 plots/wave_plus_IG_2comp.jpg