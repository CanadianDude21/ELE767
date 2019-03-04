
import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")

import classe, random, fetch
import numpy as np


dataset = fetch.getEpoque(nombreTrame=50)
print("len:",len(dataset[0].data))
#indiceInput = random.randrange(0,len(dataset))
#inputChoisie = np.asarray(dataset[indiceInput].data)
#config = fetch.getConfig()
#configSortie=fetch.getConfigSortie(config["FichierConfigSortie"])
#output = np.asarray(configSortie)
#outputDesire = output[dataset[indiceInput].resultat]

#bestReseau = classe.reseaux(config)
#bestReseau.train(inputChoisie, outputDesire, 1)
#print(bestReseau.lay1.shape)



print("done")