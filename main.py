from classe import classe
import random

nbCouches = 3
nbNeurones = 3
nbLiens = 3

bestReseau = classe.reseaux(nbCouches)

for i in range(nbCouches):
	bestCouche = classe.couche(nbNeurones)
	bestReseau.tabCouche.append(bestCouche)

	"""for j in range(nbNeurones):
		bestNeurone = classe.neurone(random.randrange(0,10),nbLiens)
		bestReseau.tabCouche[i].tabNeurone.append(bestNeurone)

		for k in range(nbLiens):
			bestPoids = classe.poids(random.randrange(0,4),k)
			bestReseau.tabCouche[i].tabNeurone[j].tabLiens.append(bestNeurone)
		"""
for thing in enumerate(bestReseau.tabCouche):
	print(thing)

print("done")
