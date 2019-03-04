
import sys
sys.path.insert(0, "function/")
import FuncActivation as act
import re


class classEpoque():

	def __init__(self,rawData):
		self.resultat=0
		self.data=[]
		self.rawDataLine=rawData

def getEpoque(nombreTrame=60):

	listEpoque=[]
	line_number=0
	tmplist=[]
	tmpStr=""
	modulo=1

	f=open("DATA/data_train.txt","r")
	for text_line in f:
		index=0
		listEpoque.append(classEpoque(text_line))
		index=listEpoque[line_number].rawDataLine.index(' ')
		tmpStr=listEpoque[line_number].rawDataLine[0:index+1] #permet de recuperer le chiffre a predire
		listEpoque[line_number].rawDataLine = listEpoque[line_number].rawDataLine[index+1:] #retire la prediction de la chaine de donner

		if tmpStr[:1]=="o":
			listEpoque[line_number].resultat=0
		else:
			listEpoque[line_number].resultat=int(tmpStr[:1])

		tmplist=listEpoque[line_number].rawDataLine.split(" ") #transforme la string en une list
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
				listEpoque[line_number].data.append(float(data))



		line_number=line_number+1;
	f.close()
	print("done")
	return listEpoque

def getConfig():
	f=open("config/config.txt","r")
	answer = {}
	for line in f:
	    k, v = line.strip().split(':')
	    answer[k.strip()] = v.strip()
	f.close()

	for keys in answer:
		if re.search(r'^[-+]?[0-9]+$',answer[keys]):
			answer[keys]=int(answer[keys])
		else:
			if re.search(r'^[-+]?\d+\.\d+$',answer[keys]):
				answer[keys]=float(answer[keys])
			else:
				if answer[keys]=="sigmoid":
					answer[keys]=act.sigmoid
				elif answer[keys]=="tanh":
					answer[keys]=act.tanh
				else:
					print("nope")
	return answer


def getConfigSortie(nombre):
	f=open("config/configSortie"+str(nombre)+".txt","r")
	answer = []
	for line in f:
	    k, v = line.strip().split(':')
	    answer.append([])
	    for char in v:
	    	answer[int(k)].append(int(char))
	f.close()
	return answer