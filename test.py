import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")
sys.path.insert(0, "UI/")
import fetch, lvq, random

config = fetch.getConfig("config/testconfig.txt")
donneTrain = fetch.getEpoque(int(config["nbrPrototype"]/26),"DATA/data_train.txt")
donneVC = fetch.getEpoque(int(config["nbrPrototype"]/26),"DATA/data_vc.txt")

bestReseau = lvq.lvq(donneTrain,config)
# j=0
# while(j<10):
# 	for i in range(len(bestReseau.Epoque)):
# 		bestReseau.train()
# 	print("train{} is done\n".format(j))

# 	result = 0
# 	for i in range(len(donneVC)):
# 		result += bestReseau.test(donneVC[i])
# 	print(str(result)+"/"+str(len(donneVC)))
# 	j+=1
j=0
while(j<3):
	result = 0
	for i in range(len(bestReseau.Epoque)):
 		result += bestReseau.train()
	print("train is done\n {}/{}".format(result, len(bestReseau.Epoque)))
	j+=1

result = 0
for i in range(len(donneVC)):
	indiceInput = random.randrange(0,len(donneVC))
	result += bestReseau.test(donneVC[indiceInput])
print(str(result)+"/"+str(len(donneVC)))