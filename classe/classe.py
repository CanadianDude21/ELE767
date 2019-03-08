import numpy as np
import random

class reseaux():

	def __init__(self,configOriginal):

		self.config = configOriginal

		i=0
		self.lay = []
		self.lay.append(np.random.uniform(-0.1,0.1,(self.config["nbTrames"]*26, self.config["neuroneEntree"])))
		self.lay.append(np.random.uniform(-0.1,0.1,(self.config["neuroneEntree"], self.config["neuroneCacher"][i])))
		i+=1
		while i <= self.config["nombreCoucheCachees"]-1:	
			self.lay.append(np.random.uniform(-0.1,0.1,(self.config["neuroneCacher"][i-1], self.config["neuroneCacher"][i])))
			i+=1
		self.lay.append(np.random.uniform(-0.1,0.1,(self.config["neuroneCacher"][i-1], self.config["neuroneSortie"])))

	def activation(self,inputs,arrayPoids):
		return self.config["fonctionActivation"](np.dot(inputs,arrayPoids))

	def correction(self,inputs,deltas):
		w_delta = np.zeros((inputs.shape[0],deltas.shape[0]))
		i = 0
		j = 0
		while i < inputs.size:
			j = 0
			while j < deltas.size:
				w_delta[i][j] = self.config["tauxApprentissage"]*deltas[j]*inputs[i]
				j+=1
			i+=1
		return w_delta 

	def test(self, input):
		activations=[]
		activations.append(self.activation(input,self.lay[0]))
		for i in range(self.config["nombreCoucheCachees"]+1):
			activations.append(self.activation(activations[i],self.lay[i+1]))
		return activations[-1] #output obtenue

	def train(self, input, outputDesire):

		
		#Activation
		l1 = self.activation(input,self.lay1)
		l2 = self.activation(l1,self.lay2)
		l3 = self.activation(l2,self.lay3)


		#Signal d'erreur (Calcul des deltas d'erreur)
		l3_delta = (outputDesire - l3)*self.config["foncActi"](l3,deriv=True)
		l2_delta = np.matmul(l3_delta,self.lay3.T)*self.config["foncActi"](l2,deriv=True)
		l1_delta = np.matmul(l2_delta,self.lay2.T)* self.config["fonctionActivation"](l1,deriv=True)

		w1_delta_M = self.correction(input,l1_delta)
		w2_delta_M = self.correction(l1,l2_delta)
		w3_delta_M = self.correction(l2,l3_delta)


		w1_delta = self.config["tauxApprentissage"]*np.outer(input, l1_delta)
		w2_delta = self.config["tauxApprentissage"]*np.outer(l1, l2_delta)
		w3_delta = self.config["tauxApprentissage"]*np.outer(l2, l3_delta)

		#actualisation
		self.lay1 += w1_delta
		self.lay2 += w2_delta
		self.lay3 += w3_delta