
import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")

import classe, random, fetch, configPoids
import numpy as np



dataset = fetch.getEpoque(40)
indiceInput = random.randrange(0,len(dataset))
inputChoisie = np.asarray(dataset[indiceInput].data)
#inputChoisie = np.asarray(dataset[0].data)

config = fetch.getConfig()
configSortie=fetch.getConfigSortie(config["FichierConfigSortie"])

output = np.asarray(configSortie)
outputDesire = output[dataset[indiceInput].resultat]

bestReseau = classe.reseaux(config)
configPoids.sauvegardePoids(bestReseau)
configPoids.chargerPoids(bestReseau)
resultat = bestReseau.test(inputChoisie)

i = 0
while i<2:
	for iteration in range(0,len(dataset)):
	#for iteration in range(0,1):
		indiceInput = random.randrange(0,len(dataset))
		inputChoisie = np.asarray(dataset[indiceInput].data)
		#inputChoisie = np.asarray(dataset[0].data)
		outputDesire = output[dataset[indiceInput].resultat]
		#outputDesire = output[dataset[0].resultat]

		bestReseau.train(inputChoisie, outputDesire)
	i+=1


# #print(bestReseau.lay1.shape)
configPoids.sauvegardePoids(bestReseau)
# print(bestReseau.test(inputChoisie))
# print("\nsortie desiree:\n{}".format(dataset[indiceInput].resultat))
