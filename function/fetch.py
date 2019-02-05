class classEpoque():

	def __init__(self,rawData):
		self.resultat=0
		self.data=[]
		self.rawDataLine=rawData

def epoque():

	listEpoque=[]
	line_number=0
	tmpStr=""

	f=open("DATA/data_test.txt","r")
	for text_line in f:
		index=0
		listEpoque.append(classEpoque(text_line))
		index=listEpoque[line_number].rawDataLine.index(' ')
		tmpStr=listEpoque[line_number].rawDataLine[0:index+1] #permet de recuperer le chiffre a predire
		listEpoque[line_number].rawDataLine = listEpoque[line_number].rawDataLine[index+1:] #retire la prediction de la chaine de donner
		listEpoque[line_number].resultat=int(tmpStr[:1])
		print(listEpoque[line_number].rawDataLine)
		listEpoque[line_number].data = [int(x) for x in listEpoque[line_number].rawDataLine.split(" ")] #pour ligne on extrait les données
		line_number=line_number+1;

	return listEpoque




#test = '8743-12083-15'
