
import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")

import classe, random, fetch, configPoids
import numpy as np



dataset = fetch.getEpoque()
indiceInput = random.randrange(0,len(dataset))
inputChoisie = np.asarray(dataset[indiceInput].data)
#inputChoisie = np.asarray(dataset[0].data)

config = fetch.getConfig()
configSortie=fetch.getConfigSortie(config["FichierConfigSortie"])

output = np.asarray(configSortie)
outputDesire = output[dataset[indiceInput].resultat]

bestReseau = classe.reseaux(config)
#configPoids.sauvegardePoids(bestReseau)
configPoids.chargerPoids(bestReseau)
for iteration in range(0,200):
#for iteration in range(0,1):
	indiceInput = random.randrange(0,len(dataset))
	inputChoisie = np.asarray(dataset[indiceInput].data)
	#inputChoisie = np.asarray(dataset[0].data)
	outputDesire = output[dataset[indiceInput].resultat]
	#outputDesire = output[dataset[0].resultat]

	bestReseau.train(inputChoisie, outputDesire)
	print("\nsortie desiree:\n{}".format(dataset[indiceInput].resultat))
#print(bestReseau.lay1.shape)




print("done")