
import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")

import classe
import fetch

dataset = fetch.getEpoque() 
config = fetch.getConfig()
configSortie=fetch.getConfigSortie(config["FichierConfigSortie"])
#print (len(dataset[0].data))
bestReseau = classe.reseaux(config,dataset,configSortie)
bestReseau.train()
#print(bestReseau.lay1.shape)



print("done")