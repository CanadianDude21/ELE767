import random
import numpy as np
def apprentissage(reseau,datasetInput,codeOutput,nbrEpoques):
	i = 0
	while i<nbrEpoques:
		for iteration in range(0,len(datasetInput)):

			indiceInput = random.randrange(0,len(datasetInput))
			inputChoisie = np.asarray(datasetInput[indiceInput].data)
			outputDesire = codeOutput[datasetInput[indiceInput].resultat]

			bestReseau.train(inputChoisie, outputDesire)
		print("Époque {} terminer\n".format(i))
		i+=1
	print("Sauvegarde des poids")
	configPoids.sauvegardePoids(reseau)

def VC(reseau,datasetInput,codeOutput):
	print("Validation croisée commencée\n")
	nbrReussite = 0
	for iteration in range(0,len(datasetInput)):
		indiceInput = random.randrange(0,len(datasetInput))
		inputChoisie = np.asarray(datasetInput[indiceInput].data)

		resultatObtenu = reseau.test(inputChoisie)

		if(np.argmax(codeOutput[datasetInput[indiceInput].resultat])==np.argmax(resultatObtenu)):
			nbrReussite+=1

	pourcentageReussite = (nbrReussite/len(datasetInput))*100
	print(pourcentageReussite)

def test(reseau,datasetInput,codeOutput):
	print("Test commencé\n")
	nbrReussite = 0
	for iteration in range(0,len(datasetInput)):
		indiceInput = random.randrange(0,len(datasetInput))
		inputChoisie = np.asarray(datasetInput[indiceInput].data)

		resultatObtenu = reseau.test(inputChoisie)

		if(np.argmax(codeOutput[datasetInput[indiceInput].resultat])==np.argmax(resultatObtenu)):
			nbrReussite+=1

	pourcentageReussite = (nbrReussite/len(datasetInput))*100