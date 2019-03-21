import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")
sys.path.insert(0, "UI/")
import fetch, classe	

config = fetch.getConfig("config/testconfig.txt")
donne = fetch.getEpoque(int(config["nbTrames"]),"DATA/data_train.txt")

donneVC = fetch.getEpoque(int(config["nbTrames"]),"DATA/data_vc.txt")

bestReseau = classe.lvq(donne,config)
acc=0

for x in range(0,2*len(donne)):
	bestReseau.train()

for x in range(len(donneVC)):
	#for y in range(len(donneVC[x].data)):
		acc += bestReseau.test(donneVC[x])

print (acc)
print (acc/len(donneVC))
