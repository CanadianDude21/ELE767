import numpy as np
np.set_printoptions(threshold=1000000)

def sauvegardePoids(reseau):
	f=open("config/configPoids.txt","w")
	f.write("poids de couche 1\n"+np.array2string(reseau.lay1)+"\npoids de couche 2\n"+np.array2string(reseau.lay2)
		+"\npoids de couche 3\n"+np.array2string(reseau.lay3))
	f.close()
	

def chargerPoids(reseau):
	f=open("config/configPoids.txt","r")
	contenu = f.read()
	contenu = contenu.replace("[","")
	contenu = contenu.replace("]","")
	contenu = contenu.replace("\n"," ")
	contenu = contenu.replace("poids de couche 1","")
	contenu = contenu.replace("poids de couche 2","")
	contenu = contenu.replace("poids de couche 3","")
	contenu = contenu.replace("  "," ")
	print(contenu)
	contenu_list = contenu.split(" ")
	"""lay1 = np.fromstring(contenu,count=reseau.lay1.size,sep=' ')
	lay1 = np.reshape(lay1,reseau.lay1.shape)
	lay2 = np.fromstring(contenu,count=reseau.lay2.size,sep=' ')"""
	print(reseau.lay1.shape)
	print(reseau.lay2.shape)
	print(reseau.lay3.shape)
	print(len(contenu_list))
	