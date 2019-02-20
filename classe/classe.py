import numpy as np
import random

class reseaux():

	def __init__(self,configOriginal,donnee):

		self.config = configOriginal
		self.tabEpoque = donnee
		self.input = np.asarray(self.tabEpoque[random.randrange(0,len(self.tabEpoque))].data)
		self.lay1 = np.random.uniform(-0.1,0.1,(self.config["nbDonneeEntrant"], self.config["neuroneEntree"]))
		self.lay2 = np.random.uniform(-0.1,0.1,(self.config["neuroneEntree"], self.config["neuroneCacher"]))
		self.lay3 = np.random.uniform(-0.1,0.1,(self.config["neuroneCacher"], self.config["neuroneSortie"]))

	def activation(self,inputs,arrayPoids):

		return self.config["delta"](np.dot(inputs,arrayPoids))

	def train(self):
		l1 = self.activation(self.input,self.lay1)
		l2 = self.activation(l1,self.lay2)
		l3 = self.activation(l2,self.lay3)

		l3_error = output_data - l3