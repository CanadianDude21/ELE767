import numpy as np
import random

class reseaux():

	def __init__(self,configOriginal,donnee, donneeSortie):

		self.config = configOriginal
		self.tabEpoque = donnee
		self.tabSortie = donneeSortie

		self.indiceInput=random.randrange(0,len(self.tabEpoque))
		self.input = np.asarray(self.tabEpoque[self.indiceInput].data)
		self.lay1 = np.random.uniform(-0.1,0.1,(self.config["nbDonneeEntrant"], self.config["neuroneEntree"]))
		self.lay2 = np.random.uniform(-0.1,0.1,(self.config["neuroneEntree"], self.config["neuroneCacher"]))
		self.lay3 = np.random.uniform(-0.1,0.1,(self.config["neuroneCacher"], self.config["neuroneSortie"]))

		self.output = np.asarray(self.tabSortie)
		self.outputDesire = self.output[self.tabEpoque[self.indiceInput].resultat]


	def activation(self,inputs,arrayPoids):
		#print ("input : {}",inputs)
		#print ("arrayPoids : {}",arrayPoids)
		return self.config["fonctionActivation"](np.matmul(inputs,arrayPoids))

	#def correction(self,inputs,deltas):

	#	return np.poids = self.config["tauxApprentissage"]

	def train(self):
		#Activation
		l1 = self.activation(self.input,self.lay1)
		l2 = self.activation(l1,self.lay2)
		l3 = self.activation(l2,self.lay3)
		print ("activation done")
		#Signal d'erreur (Calcul des deltas d'erreur)
		l3_delta = (self.outputDesire - l3)*self.config["fonctionActivation"](l3,deriv=True)
		l2_delta = np.matmul(l3_delta,self.lay3.T)*self.config["fonctionActivation"](l2,deriv=True)
		l1_delta = np.matmul(l2_delta,self.lay2.T)* self.config["fonctionActivation"](l1,deriv=True)
		print(self.input.shape)
		print(l1_delta.shape)
		#Correction (calcul deltas des poids)

		w1_delta = np.zeros(self.lay1.shape)
		i = 0
		j = 0
		while(i < self.input.size): 
			while(j < l1_delta.size):
				w1_delta[i][j] = self.config["tauxApprentissage"]*l1_delta[j]*self.input[i]
				j+=1
			i+=1
		print("w1_delta[0][0]: {}".format(w1_delta[0][0]))
		print("lay1 avant: {}".format(self.lay1))
		#actualisation
		self.lay1 += w1_delta
		print("lay1 apres: {}".format(self.lay1))
	