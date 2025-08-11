import numpy as np

def execute(h, omega, g): #function k=wvnum_omvec(h,omega,g);
	#% first guess
	k = (omega * omega / g)/np.sqrt(np.tanh(omega * omega * h / g))
	#%Newton Raphson
	error = np.transpose(np.ones((len(h), 1)))
	while np.any(abs(error) > .000001):
		f = omega * omega - g * k * (np.tanh(k * h))
		fp = -g * np.tanh(k * h) - g * (k * h) / (np.pow(np.cosh(k*h), 2))
		kn= k - f/fp
		error = np.abs(kn-k) / k
		k = kn
		
	return k
