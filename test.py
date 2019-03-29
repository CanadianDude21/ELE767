import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")
sys.path.insert(0, "UI/")
import fetch, lvq, random

config = fetch.getConfig("config/testconfig.txt")
donneTrain = fetch.getEpoque(int(config["nbrPrototype"]/26),"DATA/data_train.txt")
donneVC = fetch.getEpoque(int(config["nbrPrototype"]/26),"DATA/data_vc.txt")
donneTest = fetch.getEpoque(int(config["nbrPrototype"]/26),"DATA/data_test.txt")

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
while(j<1):
	result = 0
	for i in range(len(bestReseau.Epoque)):
 		result += bestReseau.train()
	j+=1
print("train is done\n {}/{}".format(result, i))
print(bestReseau.Classes)
result = 0
for i in range(len(donneVC)):
	indiceInput = random.randrange(0,len(donneVC))
	result += bestReseau.test(donneVC[indiceInput])
print("VC: "+str(result)+"/"+str(len(donneVC)))

result = 0
for i in range(len(donneTest)):
	indiceInput = random.randrange(0,len(donneTest))
	result += bestReseau.test(donneTest[indiceInput])
print("\nTest: "+str(result)+"/"+str(len(donneTest)))