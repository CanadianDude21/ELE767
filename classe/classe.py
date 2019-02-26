import numpy as np
import random

class reseaux():

	def __init__(self,configOriginal,donnee, donneeSortie):

		self.config = configOriginal
		self.tabEpoque = donnee
		self.tabSortie = donneeSortie

		self.input = np.asarray(self.tabEpoque[random.randrange(0,len(self.tabEpoque))].data)
		self.lay1 = np.random.uniform(-0.1,0.1,(self.config["nbDonneeEntrant"], self.config["neuroneEntree"]))
		self.lay2 = np.random.uniform(-0.1,0.1,(self.config["neuroneEntree"], self.config["neuroneCacher"]))
		self.lay3 = np.random.uniform(-0.1,0.1,(self.config["neuroneCacher"], self.config["neuroneSortie"]))
		self.output = np.asarray(tabSortie)


	def activation(self,inputs,arrayPoids):

		return self.config["delta"](np.dot(inputs,arrayPoids))

	def correction(self,inputs,deltas):

		return np.poids = self.config["tauxApprentissage"]

	def train(self):
		#Activation
		l1 = self.activation(self.input,self.lay1)
		l2 = self.activation(l1,self.lay2)
		l3 = self.activation(l2,self.lay3)

		#Signal d'erreur (Calcul des deltas d'erreur)
		l3_error = self.output - l3
		l3_delta = l3_error * self.config["delta"](l3,deriv=True)

		l2_error = l3_delta.dot(self.lay3.T)
		l2_delta = l2_error	* self.config["delta"](l2,deriv=True)

		l1_error = l2_delta.dot(self.lay2.T)
		l1_delta = l1_error	* self.config["delta"](l1,deriv=True)

		#Correction (calcul deltas des poids)

