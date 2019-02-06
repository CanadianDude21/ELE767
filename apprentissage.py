from classe import classe
import random

def creerReseau(nbCouches,nbNeurones,nbLiens):
	
	bestReseau = classe.reseaux(nbCouches)
	for i in range(nbCouches):
		bestCouche = classe.couche(nbNeurones)
		bestReseau.tabCouche.append(bestCouche)

		for j in range(nbNeurones):
			bestNeurone = classe.neurone(random.randrange(0,10),nbLiens) #TODO savoir quel poids mettre pour chaque neurone
			bestReseau.tabCouche[i].tabNeurone.append(bestNeurone)

			for k in range(nbLiens):
				if i == 0:
					bestPoids = classe.poids(random.uniform(-0.1, 0.1))
				else:
					bestPoids = classe.poids(random.uniform(-0.1, 0.1),k)
				bestReseau.tabCouche[i].tabNeurone[j].tabLiens.append(bestNeurone)
	return bestReseau

def activation():

def sigErreur():

def correction():

def actualisation():

