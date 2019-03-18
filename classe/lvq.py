import numpy as np
import random

class lvq():

	def __init__(self,Epoque,config):
		#valeur des poids initialiser

		self.config
		self.Epoque
		self.Classes =[]
	def initPoids(self):
	

	def train(self):

		indiceInput = random.randrange(0,len(self.Epoque))
		inputChoisie = np.asarray(self.Epoque[indiceInput].data)
		# actualisation
		minimumTrouver = 0;
		normMinimal = 999999999
		#trouver le minimum
		for classIndex,Protoype in zip(range(0,len(self.Classes)),self.Classes):
			if normMinimal >  np.linalg.norm(inputChoisie-Protoype):
				normMinimal=np.linalg.norm(inputChoisie-Protoype)
				minimumTrouver = classIndex

		if self.Epoque[indiceInput].resultat == classIndex:

		else:

		# correction

	def test(self,donnee):

