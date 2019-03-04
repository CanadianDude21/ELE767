
import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")

import classe, random, fetch, configPoids
import numpy as np


dataset = fetch.getEpoque()
indiceInput = random.randrange(0,len(dataset))
inputChoisie = np.asarray(dataset[indiceInput].data)

config = fetch.getConfig()
configSortie=fetch.getConfigSortie(config["FichierConfigSortie"])

output = np.asarray(configSortie)
outputDesire = output[dataset[indiceInput].resultat]

bestReseau = classe.reseaux(config)
#configPoids.sauvegardePoids(bestReseau)
configPoids.chargerPoids(bestReseau)
"""for iteration in range(0,len(dataset)):
	indiceInput = random.randrange(0,len(dataset))
	inputChoisie = np.asarray(dataset[indiceInput].data)
	outputDesire = output[dataset[indiceInput].resultat]

	bestReseau.train(inputChoisie, outputDesire)
#print(bestReseau.lay1.shape)"""



print("done")