from classe import classe
import random

def creerReseau(config):
	nbCouches = int(config["nombreCoucheCacheEntree"])+2
	nbNeuronesEntree = int(config["neuroneEntree"])
	nbNeuronesCache = int(config["neuroneCacher"])
	nbNeuronesSortie = int(config["neuroneSortie"])
	nbDonneeEntrant = int(config["nbDonneeEntrant"])


	bestReseau = classe.reseaux(nbCouches)
	for i in range(nbCouches):
		if i == 0:
			bestCouche = classe.couche(nbNeuronesEntree)
		elif i == 1:
			bestCouche = classe.couche(nbNeuronesCache)
		elif i == 2:
			bestCouche = classe.couche(nbNeuronesSortie)
		bestReseau.tabCouche.append(bestCouche)

		for j in range(bestReseau.tabCouche[i].nbNeurones):
			if i == 0:
				bestNeurone = classe.neurone(random.randrange(0,10),nbDonneeEntrant) #TODO savoir quel poids mettre pour chaque neurone
			else:
				bestNeurone = classe.neurone(random.randrange(0,10),bestReseau.tabCouche[i-1].nbNeurones) #TODO savoir quel poids mettre pour chaque neurone
			bestReseau.tabCouche[i].tabNeurone.append(bestNeurone)

			for k in range(bestReseau.tabCouche[i-1].nbNeurones):
				if i == 0:
					bestLiens = classe.liens(random.uniform(-0.1, 0.1))
				else:
					bestLiens = classe.liens(random.uniform(-0.1, 0.1),bestReseau.tabCouche[i-1].tabNeurone[k])
				bestReseau.tabCouche[i].tabNeurone[j].tabLiens.append(bestLiens)
	return bestReseau

#def activation():

#def sigErreur():

#def correction():

#def actualisation():

