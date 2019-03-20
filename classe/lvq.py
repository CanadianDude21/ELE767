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
		#indiceInput = 0
		inputChoisie = np.asarray(self.Epoque[indiceInput].data)

		# actualisation
		minimumTrouver = 0;
		normMinimal = 999999999
		tempLinRes = 0
		#trouver le minimum
		for classIndex,Prototype in zip(range(0,len(self.Classes)),self.Classes):
			tempLinRes = np.linalg.norm(inputChoisie-Prototype)
			if normMinimal >  tempLinRes:
				normMinimal = tempLinRes
				minimumTrouver = classIndex

		# correction
		print(self.Epoque[indiceInput].resultat)
		print(minimumTrouver)
		if self.Epoque[indiceInput].resultat == minimumTrouver:
			self.Classes[minimumTrouver] += self.config["tauxApprentissage"]*(inputChoisie-self.Classes[minimumTrouver])

		else:
			self.Classes[minimumTrouver] -= self.config["tauxApprentissage"]*(inputChoisie-self.Classes[minimumTrouver])
					

	def test(self,donnee):

		donneData = np.asarray(self.donnee.data)
		for classIndex,Prototype in zip(range(0,len(self.Classes)),self.Classes):
			tempLinRes = np.linalg.norm(donneData-Prototype)
			if normMinimal >  tempLinRes:
				normMinimal = tempLinRes
				minimumTrouver = classIndex

		if donnee.resultat == minimumTrouver:		
			print("Même Classe!")
			return 1
		else:
			print("Pas même Classe!")
			return 0
