import numpy as np
import random

class mlp():
	#constructeur du réseau
	#on doit lui passer la config
	def __init__(self,configOriginal):

		self.config = configOriginal

		#initialise les matrices de poids de liens entre -0.1 et 0.1
		i=0
		self.lay = []
		self.lay.append(np.random.uniform(-0.1,0.1,(self.config["nbTrames"]*26, self.config["neuroneEntree"])))
		if self.config["nombreCoucheCachees"] > 0:
			self.lay.append(np.random.uniform(-0.1,0.1,(self.config["neuroneEntree"], self.config["neuroneCacher"][i])))
			i+=1
			while i <= self.config["nombreCoucheCachees"]-1:
				self.lay.append(np.random.uniform(-0.1,0.1,(self.config["neuroneCacher"][i-1], self.config["neuroneCacher"][i])))
				i+=1
			self.lay.append(np.random.uniform(-0.1,0.1,(self.config["neuroneCacher"][i-1], self.config["neuroneSortie"])))
		else:
			self.lay.append(np.random.uniform(-0.1, 0.1, (self.config["neuroneEntree"], self.config["neuroneSortie"])))

		#on met la constante de momentum à 0.5
		self.momentum = 0.5
		self.omegasDeltasPrec = []

	#retourne la valeur d'activation des neurones avant d'appliquer la fonction d'activation
	def activation(self,inputs,arrayPoids):
		return np.dot(inputs,arrayPoids)

	#retourne la sortie obtenue d'un set de donnée en entrée
	def test(self, input):
		#Activation
		activations=[]
		sortieFuncActivation = []
		activations.append(self.activation(input,self.lay[0]))
		sortieFuncActivation.append(self.config["foncActi"](activations[0]))
		for i in range(self.config["nombreCoucheCachees"]+1):
			activations.append(self.activation(sortieFuncActivation[i],self.lay[i+1]))
			sortieFuncActivation.append(self.config["foncActi"](activations[i+1]))
		
		return sortieFuncActivation[-1] #output obtenue

	#le réseau apprend selon un set de données d'entrée
	#on peut choisir d'appliquer le momentum ou non
	def train(self, input, outputDesire, momentum=False):
		
		#Activation
		activations=[]
		sortieFuncActivation = []
		activations.append(self.activation(input,self.lay[0]))
		sortieFuncActivation.append(self.config["foncActi"](activations[0]))
		for i in range(self.config["nombreCoucheCachees"]+1):
			activations.append(self.activation(sortieFuncActivation[i],self.lay[i+1]))
			sortieFuncActivation.append(self.config["foncActi"](activations[i+1]))
		
		#Signal d'erreur (Calcul des deltas d'erreur)
		if self.config["fonctionActivation"] == "sigmoid":
			deltas=[]
			deltas.insert(0,(outputDesire - sortieFuncActivation[-1])*self.config["foncActi"](sortieFuncActivation[-1],deriv=True))
			for i in range(self.config["nombreCoucheCachees"]+1):
				deltas.insert(0,np.matmul(deltas[-1-i],self.lay[-1-i].T)*self.config["foncActi"](sortieFuncActivation[-2-i],deriv=True)) 

		else:
			deltas=[]
			deltas.insert(0,(outputDesire - sortieFuncActivation[-1])*self.config["foncActi"](activations[-1],deriv=True))
			for i in range(self.config["nombreCoucheCachees"]+1):
				deltas.insert(0,np.matmul(deltas[-1-i],self.lay[-1-i].T)*self.config["foncActi"](activations[-2-i],deriv=True))

		#Correction sans momentum
		if momentum is False:
			omegasDeltas = []
			omegasDeltas.append(self.config["tauxApprentissage"]*np.outer(input, deltas[0]))
			for i in range(self.config["nombreCoucheCachees"]+1):
				omegasDeltas.append(self.config["tauxApprentissage"]*np.outer(sortieFuncActivation[i], deltas[i+1]))

		#Correction avec momentum
		else:
			if len(self.omegasDeltasPrec) > 0:
				omegasDeltas = []
				omegasDeltas.append(self.config["tauxApprentissage"] * np.outer(input, deltas[0]))
				for i in range(self.config["nombreCoucheCachees"] + 1):
					omegasDeltas.append(self.config["tauxApprentissage"] * np.outer(sortieFuncActivation[i], deltas[i + 1]))
				for i in range(len(omegasDeltas)):
					omegasDeltas[i]+=self.momentum * self.omegasDeltasPrec[i]
			else:
				omegasDeltas = []
				omegasDeltas.append(self.config["tauxApprentissage"] * np.outer(input, deltas[0]))
				for i in range(self.config["nombreCoucheCachees"] + 1):
					omegasDeltas.append(self.config["tauxApprentissage"] * np.outer(sortieFuncActivation[i], deltas[i + 1]))

		#actualisation
		for i in range(self.config["nombreCoucheCachees"]+1):
			self.lay[i] += omegasDeltas[i]


		self.omegasDeltasPrec = omegasDeltas

		return sortieFuncActivation[-1] #output obtenue



class lvq():

	def __init__(self,Epoque, config, DVQ = False):
		#valeur des poids initialiser

		self.config = config
		self.Epoque = Epoque
		self.Classes = self.initClasses()
		if DVQ is True:
			self.varClasses = []
			self.stdClasses = []
			for classe in self.Classes:
				self.stdClasses.append(np.std(classe))
				self.varClasses.append(np.var(classe))
			self.seuilVar = 11*min(self.varClasses)

	def initClasses(self):
		# Retourne une list comme cela :
		# 		[  0  1  2    n      ~~~~ nombre de classes
		# rep 0   [],[],[]...[]
		# rep 1   [],[],[]...[]
		#		  .   .  .    .
		#		  .   .  .    .
		#		  .   .  .    .
		#						]
		classesRef = []
		for Rep in range(self.config["RepParClasses"]):
			classesRef.append([])
			for classe in range(self.config["nbrClasses"]):
				idx, objet = next((idx, obj) for idx, obj in enumerate(self.Epoque) if obj.resultat == classe)
				classesRef[Rep].append(np.asarray(objet.data))
				del self.Epoque[idx]
		return classesRef



	def train(self, lvq2 = False):

		indiceInput = random.randrange(0, len(self.Epoque))
		inputChoisie = np.asarray(self.Epoque[indiceInput].data)

		# actualisation
		prototypeIndexTrouver= 0
		normMinimal = np.linalg.norm(inputChoisie-self.Classes[0][0])
		classeIndexTrouver = 0

		#utile pour LVQ2
		prototypeIndexTrouver2 = 0
		normMinimal2 = np.linalg.norm(inputChoisie-self.Classes[0][0])
		classeIndexTrouver2 = 0

		for classeIndex, classe in zip(range(len(self.Classes)), self.Classes): #pour chaque classe
			for prototypeIndex, prototype in zip((range(len(classe))),classe): #pour chaque prototype de la classe présente
				tempLinRes = np.linalg.norm(inputChoisie-prototype) #calcul de distance euclidienne
				if normMinimal > tempLinRes: #si c'est la plus petite distance
					if lvq2 is True: #bloc de code qui descend l'ancienne plus petite distance à la deuxième plus petite
						normMinimal2 = normMinimal
						classeIndexTrouver2 = classeIndexTrouver
						prototypeIndexTrouver2 = prototypeIndexTrouver

					normMinimal = tempLinRes  # pour prochaines iterations
					classeIndexTrouver = classeIndex
					prototypeIndexTrouver = prototypeIndex

		# algo de LVQ2
		if lvq2 is True:
			if self.Epoque[indiceInput].resultat != prototypeIndexTrouver and self.Epoque[indiceInput].resultat == prototypeIndexTrouver2:
				if normMinimal/normMinimal2 > 1-self.config["epsilon"] and normMinimal2/normMinimal < 1+self.config["epsilon"]:
					self.Classes[classeIndexTrouver][prototypeIndexTrouver] -= self.config["tauxApprentissage"] * (inputChoisie - self.Classes[classeIndexTrouver][prototypeIndexTrouver])
					self.Classes[classeIndexTrouver2][prototypeIndexTrouver2] += self.config["tauxApprentissage"] * (inputChoisie - self.Classes[classeIndexTrouver2][prototypeIndexTrouver2])
					return 1
				else:
					return 0
			elif self.Epoque[indiceInput].resultat != prototypeIndexTrouver2 and self.Epoque[indiceInput].resultat == prototypeIndexTrouver:
				if normMinimal2 / normMinimal > 1 - self.config["epsilon"] and normMinimal / normMinimal2 < 1 +self.config["epsilon"]:
					self.Classes[classeIndexTrouver][prototypeIndexTrouver] += self.config["tauxApprentissage"] * (inputChoisie - self.Classes[classeIndexTrouver][prototypeIndexTrouver])
					self.Classes[classeIndexTrouver2][prototypeIndexTrouver2] -= self.config["tauxApprentissage"] * (inputChoisie - self.Classes[classeIndexTrouver2][prototypeIndexTrouver2])
					return 1
				else:
					return 0
			else:
				return 0

		# algo de LVQ
		else:
			if self.Epoque[indiceInput].resultat == prototypeIndexTrouver:
				self.Classes[classeIndexTrouver][prototypeIndexTrouver] += self.config["tauxApprentissage"]*(inputChoisie-self.Classes[classeIndexTrouver][prototypeIndexTrouver])
				return 1
			else:
				self.Classes[classeIndexTrouver][prototypeIndexTrouver] -= self.config["tauxApprentissage"]*(inputChoisie-self.Classes[classeIndexTrouver][prototypeIndexTrouver])
				return 0


	def test(self,donnee):

		donneData = np.asarray(donnee.data)
		minimumTrouver = 0;
		normMinimal = np.linalg.norm(donneData-self.Classes[0][0])
		tempLinRes = 0
		prototypeIndexTrouver=0
		for repIndex, rep in zip(range(len(self.Classes)), self.Classes):
			for prototypeIndex, prototype in zip((range(len(rep))), rep):
				tempLinRes = np.linalg.norm(donneData - prototype)
				if normMinimal > tempLinRes:
					normMinimal = tempLinRes  # pour prochaines iterations
					repIndexTrouver = repIndex
					prototypeIndexTrouver = prototypeIndex

		if donnee.resultat == prototypeIndexTrouver:
			return 1
		else:
			return 0
