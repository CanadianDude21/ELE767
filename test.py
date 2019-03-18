import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")
sys.path.insert(0, "UI/")
import fetch, lvq

config = fetch.getConfig("config/testconfig.txt")
donne = fetch.getEpoque(config["nbrPrototype"]/26,"DATA/data_train.txt")

bestReseau = lvq.lvq(donne,config)
print(len(bestReseau.Epoque))
print(len(bestReseau.Classes))
for i in range(len(bestReseau.Classes)):
	print(len(bestReseau.Classes[i]))
