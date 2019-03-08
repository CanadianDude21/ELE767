
import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")

import classe, fetch, algo
import numpy as np

config = fetch.getConfig("config/config.txt")
configSortie = fetch.getConfigSortie(10)
donne = fetch.getEpoque(40,"DATA/data_vc.txt")
inputChoisie = np.asarray(donne[0].data)
output = np.asarray(configSortie)
outputDesire = output[donne[0].resultat]
bestReseau = classe.reseaux(config)

algo.VC(bestReseau,donne,output)