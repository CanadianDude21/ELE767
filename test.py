import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")
sys.path.insert(0, "UI/")
import fetch, lvq

config = fetch.getConfig("config/testconfig.txt")
donne = fetch.getEpoque(int(config["nbrPrototype"]/26),"DATA/data_train.txt")

bestReseau = lvq.lvq(donne,config)

print(bestReseau.Classes[9])
bestReseau.train()
print(bestReseau.Classes[9])

