
import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")
sys.path.insert(0, "UI/")

from ui import *
import classe, fetch, algo, configPoids
import numpy as np

config = fetch.getConfig("config/config.txt")
configSortie = fetch.getConfigSortie(10)
donneTrain = fetch.getEpoque(40,"DATA/data_train.txt")
donneVC = fetch.getEpoque(40,"DATA/data_vc.txt")
#inputChoisie = np.asarray(donne[0].data)
output = np.asarray(configSortie)
#outputDesire = output[donne[0].resultat]

######test validation croisée
# reseau0Epoque = classe.reseaux(config)
# configPoids.chargerPoids(reseau0Epoque,"config/avant")
# reseau1Epoque = classe.reseaux(config)
# configPoids.chargerPoids(reseau1Epoque,"config/apres")
# print("reseau 0 époques")
# algo.VC(reseau0Epoque,donneVC,output)
# print("reseau 1 époques")
# algo.VC(reseau1Epoque,donneVC,output)

###########test apprentissage
bestReseau = classe.reseaux(config)
#configPoids.sauvegardePoids(bestReseau,"config/avant")
configPoids.chargerPoids(bestReseau,"config/avant")
algo.apprentissage(bestReseau,donneTrain,output,1)
configPoids.sauvegardePoids(bestReseau,"config/apres")

