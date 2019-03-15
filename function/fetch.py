
import sys
sys.path.insert(0, "function/")
import FuncActivation as act
import re
from collections import OrderedDict


class classSample():

	def __init__(self,rawData):
		self.resultat=0
		self.data=[]
		self.rawDataLine=rawData


def getEpoque(nombreTrame=60,pathToDataSet=""):

	listSamples=[]
	line_number=0
	tmplist=[]
	tmpStr=""

	f=open(pathToDataSet,"r")
	for text_line in f:
		index=0
		listSamples.append(classSample(text_line))
		index=listSamples[line_number].rawDataLine.index(' ')
		tmpStr= listSamples[line_number].rawDataLine[0:index + 1] #permet de recuperer le chiffre a predire
		listSamples[line_number].rawDataLine = listSamples[line_number].rawDataLine[index + 1:] #retire la prediction de la chaine de donner

		if tmpStr[:1]=="o":
			listSamples[line_number].resultat=0
		else:
			listSamples[line_number].resultat=int(tmpStr[:1])

		tmplist=listSamples[line_number].rawDataLine.split(" ") #transforme la string en une list
		tmplist.pop() # retire le dernier element de la list (\n)
		tmplistlen=len(tmplist)
		newtmplist=[]

		for x in range(0,tmplistlen,60):	#crée une list de list de 60 elements
			newtmplist.append(tmplist[x:x+60])	

		for templist60 in newtmplist:	# retire des elements a chaque list de 60 elements si necessaire
			for x in range(0, (60-nombreTrame)):
				templist60.pop()

		flat_list=[]	
		for sublist in newtmplist:	# forme la list de list sous forme de list de donner
			for item in sublist:
				flat_list.append(item)

		for data in flat_list:
				listSamples[line_number].data.append(float(data))



		line_number=line_number+1;
	f.close()
	return listSamples

def getConfig(pathToConfig=""):
	f=open(pathToConfig,"r")
	answer = OrderedDict()

	#converti le fichier config en dictionnaire
	for line in f:
	    k, v = line.strip().split(':')
	    answer[k.strip()] = v.strip()
	f.close()
	
	for keys in answer:
		if re.search(r'^[-+]?[0-9]+$',answer[keys]):#trouve les nombres dans les info de la config
			answer[keys]=int(answer[keys])
		else:
			if re.search(r'^[-+]?\d+\.\d+$',answer[keys]):#trouve les nombres a virgule dans les info de la config
				answer[keys]=float(answer[keys])
			else:
				#leger changement pour la fonction d'activation
				if answer[keys]=="sigmoid":
					answer[keys]=act.sigmoid
				elif answer[keys]=="tanh":
					answer[keys]=act.tanh
				elif answer[keys]=="relu":
					answer[keys]=act.relu
				else:
					print("nope")
	#l'entree neurone cacher est mise en list puis sauvegarder dans un element du dictionnaire
	answer["neuroneCacher"] = answer["neuroneCacher"].split(" ")
	for element in range(len(answer["neuroneCacher"])):
		answer["neuroneCacher"][element] = int(answer["neuroneCacher"][element])
	return answer


def getConfigSortie(nombre):
	f=open("config/configSortie"+str(nombre)+".txt","r")
	answer = []
	#creer une list de list. Chacune des listes correspond a la reponse de sorti des nombre 1 a 9 et o
	for line in f:
	    k, v = line.strip().split(':')
	    answer.append([])
	    for char in v:
	    	answer[int(k)].append(int(char))
	f.close()
	return answer