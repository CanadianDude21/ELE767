from classe import classe
import random
from function import fetch

dataset = fetch.getEpoque() 
config = fetch.getConfig()
configSortie=fetch.getConfigSortie(config["FichierConfigSortie"])
#print (len(dataset[0].data))
bestReseau = classe.reseaux(config,dataset,configSortie)
bestReseau.train()
#print(bestReseau.lay1.shape)



print("done")