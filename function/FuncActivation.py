import numpy as np

def sigmoid(x,deriv=False): 
	if deriv==False:		
		return (1/(1+np.exp(-x))) # pas deriver
	else:
		return x*(1-x)	#deriver

def tanh(x,deriv=False):
	if deriv==False:
		return np.tanh(x) #pas deriver
	else:
		return 1.0-np.tanh(x)**2 #deriver
		
def relu(x,deriv=False):
	if deriv==False:
		return np.maximum(x,0,x)
	else:
		x[x<=0] = 0
		x[x>0] = 1
		return x