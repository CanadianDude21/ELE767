
import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")

import classe, random, fetch, configPoids
import numpy as np



#dataset = fetch.getEpoque(40,"DATA/data_train.txt")
#dataset = fetch.getEpoque(40,"DATA/data_vc.txt")
dataset = fetch.getEpoque(40,"DATA/data_test.txt")
indiceInput = random.randrange(0,len(dataset))
inputChoisie = np.asarray(dataset[indiceInput].data)
#inputChoisie = np.asarray(dataset[0].data)

config = fetch.getConfig("config/config.txt")
configSortie=fetch.getConfigSortie(config["FichierConfigSortie"])

output = np.asarray(configSortie)
outputDesire = output[dataset[indiceInput].resultat]

bestReseau = classe.reseaux(config)
#configPoids.sauvegardePoids(bestReseau)
configPoids.chargerPoids(bestReseau)

print("Test commencer\n")
nbrReussite = 0
for iteration in range(0,len(dataset)):
#for iteration in range(0,1):
	indiceInput = random.randrange(0,len(dataset))
	inputChoisie = np.asarray(dataset[indiceInput].data)

	resultatObtenu = bestReseau.test(inputChoisie)
	#print(resultatObtenu.shape)
	#print(output.shape)
	if(np.argmax(output[dataset[indiceInput].resultat])==np.argmax(resultatObtenu)):
		nbrReussite+=1

pourcentageReussite = (nbrReussite/len(dataset))*100
print("Nombre de réussite {}\nNombre de données testées {}\nPourcentage de réussite {}".format(nbrReussite,len(dataset),pourcentageReussite))
	

# i = 0
# while i<1:
# 	print("Époque {} commencer\n".format(i))
# 	for iteration in range(0,len(dataset)):
# 	#for iteration in range(0,1):
# 		indiceInput = random.randrange(0,len(dataset))
# 		inputChoisie = np.asarray(dataset[indiceInput].data)
# 		#inputChoisie = np.asarray(dataset[0].data)
# 		outputDesire = output[dataset[indiceInput].resultat]
# 		#outputDesire = output[dataset[0].resultat]

# 		bestReseau.train(inputChoisie, outputDesire)
# 	print("Époque {} terminer\n".format(i))
# 	i+=1


# #print(bestReseau.lay1.shape)
#configPoids.sauvegardePoids(bestReseau)
# print(bestReseau.test(inputChoisie))
# print("\nsortie desiree:\n{}".format(dataset[indiceInput].resultat))
