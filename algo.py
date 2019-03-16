import random
import numpy as np
def apprentissage(reseau,datasetInput,codeOutput,tauxAppr):
	nbrReussite = 0
	for iteration in range(0,len(datasetInput)):
		indiceInput = random.randrange(0,len(datasetInput))
		inputChoisie = np.asarray(datasetInput[indiceInput].data)
		outputDesire = codeOutput[datasetInput[indiceInput].resultat]


		resultatObtenu = reseau.train(inputChoisie, outputDesire,tauxAppr)

		if(np.argmax(codeOutput[datasetInput[indiceInput].resultat])==np.argmax(resultatObtenu)):
			nbrReussite+=1
	
	return (nbrReussite/len(datasetInput))

def VC(reseau,datasetInput,codeOutput):

	nbrReussite = 0
	for iteration in range(0,len(datasetInput)):
		indiceInput = random.randrange(0,len(datasetInput))
		inputChoisie = np.asarray(datasetInput[indiceInput].data)

		resultatObtenu = reseau.test(inputChoisie)

		if(np.argmax(codeOutput[datasetInput[indiceInput].resultat])==np.argmax(resultatObtenu)):
			nbrReussite+=1

	return   nbrReussite,len(datasetInput)
	

def test(reseau,datasetInput,codeOutput):
	nbrReussite = 0
	for iteration in range(0,len(datasetInput)):
		indiceInput = random.randrange(0,len(datasetInput))
		inputChoisie = np.asarray(datasetInput[indiceInput].data)

		resultatObtenu = reseau.test(inputChoisie)

		if(np.argmax(codeOutput[datasetInput[indiceInput].resultat])==np.argmax(resultatObtenu)):
			nbrReussite+=1

	return  nbrReussite,len(datasetInput)