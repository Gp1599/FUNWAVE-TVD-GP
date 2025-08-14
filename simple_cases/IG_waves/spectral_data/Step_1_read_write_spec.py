import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# Read and generate frequency components of wind waves for IG generation
#    and FUNWAVE for wind wave only
#    Fengyan Shi 04/06/2021
#
# input file: input_data_case1.txt
# output files: 
#  SPC_dep_pf.txt; contains depth and peak frequency
#  SPC_frq.txt;    contains frequency components
#  SPC_angle.txt;  contains wave angle (single angle)
#  SPC_HMO.txt;    contains Hmo of wave components (note: not amplitude)
#  spectrum_windwave_only.txt; this is for windwave only, no IG components
#
# ---------------------------------------------------------------------
#
#clear all

#
hs = np.loadtxt('input_data_case1.txt').astype(type(float))
depth = 13.0
peak_freq = 0.158

#
f = hs[:, 0]
Ed = hs[:, 1]

#
f_IG_data = hs[0:100, 0]
E_IG_data = hs[0:100, 2]

#
E = np.zeros((len(f)))
for i in range(0, len(f)):
    E[i] = Ed[i] * (f[i + 1] - f[i])

#
E_total = np.sum(E)
Hrms = np.sqrt(8 * E_total)
Hsig = Hrms * np.sqrt(2)

#
df = f[1] - f[0]  # for equal increment

#
sk = 30     # average every 30 points
trun = 1601 # T=3.4s truncated
count = 0

#
EE = np.zeros((trun / sk))
ff = np.zeros((trun / sk))
for ii in np.arange(0, trun, sk):
    EE[count] = sum(E[ii:ii + sk - 1])
    ff[count] = f[ii + np.floor(sk / 2)]
    count = count + 1

#
ff[count + 1] = f[trun + np.floor(sk + sk / 2)]
EE[count + 1] = sum(E[trun + sk:len(E)])  # rest of energy
dff = ff[1] - ff[0]

#
E_t = sum(EE)
Hrms1 = np.sqrt(8 * E_t)
Hsig1 = Hrms1 * np.sqrt(2)

#
Hsig_resolved = 4 * np.sqrt(np.sum(EE[1:len(EE)]))

#
Amp = np.sqrt(2.0 * EE[2:len(EE)])
fff = ff[1:len(ff)]

#
fig = plt.figure(1)
plt.clf()

#
plt.plot(f[1:len(f)], E / df, linewidth = 1.0, color = 'k')
plt.grid()
plt.plot(ff[2:len(ff)], EE[2:len(EE)] / dff, linewidth = 2.0, color = 'r')
plt.plot(f_IG_data, E_IG_data, 'k', linewidth = 2.0)
plt.axis([0.0, 0.4, 0, 8.0])

#
plt.xlabel('f (Hz)')
plt.ylabel('WSD (m^2/Hz)')
plt.legend('Data','Filtered for model input')


#print -djpeg100 plots/spc_input.jpg
#print -depsc2 plots/spc_input.eps

# 

# output for IG wave generation
otherp = np.zeros((2, 1))
f_writeout = np.transpose(fff)
angle_writeout = 0
hmo_writeout= Amp * 2.0 * np.sqrt(2)
otherp[1, 1] = depth
otherp[2, 1] = peak_freq

#
np.savetxt("SPC_dep_pf.txt", otherp)
np.savetxt("SPC_frq.txt", f_writeout)
np.savetxt("SPC_angle.txt", angle_writeout)
np.savetxt("SPC_HMO.txt", hmo_writeout)

# write data for funwave with wind wave only
fname = 'spectrum_windwave_only.txt'

#
PeakPeriod = 1 / peak_freq
NumFreq = len(Amp)
NumDir = 1
Freq = fff
Dire = 0
Amp1 = Amp

# write data
fid = open(fname,'w')
fid.write(str.format('%5i %5i   - NumFreq NumDir \n', NumFreq, NumDir))
fid.write(str.format('%10.3f   - PeakPeriod  \n', PeakPeriod))
fid.write(str.format('%10.3f   - Freq \n', Freq))
fid.write(str.format('%10.3f   - Dire \n', Dire))

#dlmwrite(fname,Amp1,'delimiter','\t','-append','precision',5);
fid.close()