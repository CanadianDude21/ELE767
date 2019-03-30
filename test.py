import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")
sys.path.insert(0, "UI/")

import fetch, classe	

config = fetch.getConfig("config/testconfig.txt")
donne = fetch.getEpoque(int(config["nbTrames"]),"DATA/data_train.txt")

donneVC = fetch.getEpoque(int(config["nbTrames"]),"DATA/data_vc.txt")
donneTest = fetch.getEpoque(int(config["nbTrames"]),"DATA/data_test.txt")

bestReseau = classe.lvq(donne,config,DVQ=True)

for x in range(2*len(donne)):
	bestReseau.train()


# for z in range(len(donneTest)):
# 	#for y in range(len(donneVC[x].data)):
# 		acc += bestReseau.test(donneTest[z])
# print("VC")
# print (accVC)
# print (accVC/len(donneVC))
# print("Test")
# print (acc)
# print (acc/len(donneTest))

