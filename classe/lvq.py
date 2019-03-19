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


