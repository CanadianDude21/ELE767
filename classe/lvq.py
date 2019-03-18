import numpy as np
import random

class lvq():

	def __init__(self,Epoque,config):
		#valeur des poids initialiser
		self.config = config
		self.Epoque = Epoque
		self.Classes = self.initClasses()
		

	def initClasses(self):
		classesRef = []
		for classe in range(self.config["nbrClasses"]):
			idx, objet = next((idx, obj) for idx, obj in enumerate(self.Epoque) if obj.resultat == classe)
			classesRef.append(np.asarray(objet.data))
			del self.Epoque[idx]
		return classesRef
	#def train(self):


	#def test(self,donnee):

