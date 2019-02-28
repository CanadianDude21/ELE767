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
		print ("l3_delta: {}".format(l3_delta))
		l2_error = l3_delta.dot(self.lay3.T)
		l2_delta = l2_error	* self.config["fonctionActivation"](l2,deriv=True)

		l1_error = l2_delta.dot(self.lay2.T)
		l1_delta = l1_error	* self.config["fonctionActivation"](l1,deriv=True)

		#Correction (calcul deltas des poids)

