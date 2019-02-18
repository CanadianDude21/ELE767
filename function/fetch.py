from function import FuncActivation as act
import re


class classEpoque():

	def __init__(self,rawData):
		self.resultat=0
		self.data=[]
		self.rawDataLine=rawData

def getEpoque():

	listEpoque=[]
	line_number=0
	tmplist=[]
	tmpStr=""

	f=open("DATA/data_test.txt","r")
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
		for x in tmplist:
				listEpoque[line_number].data.append(float(x))
			
		line_number=line_number+1;
	f.close()	
	return listEpoque

def getConfig():
	f=open("config.txt","r")
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
