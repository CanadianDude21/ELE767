import random
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
def VC():

def test():