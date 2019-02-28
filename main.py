from classe import classe
import random
import apprentissage as app
from function import fetch

dataset = fetch.getEpoque() 
config = fetch.getConfig()
configSortie=fetch.getConfigSortie(config["FichierConfigSortie"])
#print (len(dataset[0].data))
bestReseau = classe.reseaux(config,dataset,configSortie)


bestReseau.train()

print("done")