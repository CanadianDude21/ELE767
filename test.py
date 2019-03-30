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

accVC = 0
acc = 0
accTest = 0

for x in range(len(donne)):
	bestReseau.train(True)


for y in range(len(donneVC)):
	accVC += bestReseau.test(donneVC[y])


for z in range(len(donneTest)):
	accTest += bestReseau.test(donneTest[z])
print("VC")
print(accVC)
print (accVC/len(donneVC))
print("Test")
print (accTest)
print (accTest/len(donneTest))

