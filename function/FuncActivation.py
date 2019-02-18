import numpy as np

def sigmoid(x,deriv=True):
	if deriv==False:
		return x*(1-x)
	else:
		return (1/(1+np.exp(-x)))

def tanh(x,deriv=True):
	if deriv==False:
		return 1.0-np.tanh(x)**2
	else:
		return np.tanh(x)
