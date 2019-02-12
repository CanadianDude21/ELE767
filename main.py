from classe import classe
import random
import apprentissage as app
from function import fetch


config = fetch.getConfig()
bestReseau = app.creerReseau(config)

for couche in bestReseau.tabCouche:
	print('nbNeurones = {}'.format(couche.nbNeurones))
#	print(type(couche))
	for neurone in couche.tabNeurone:
		print('nbLiens = {}'.format(neurone.nbLiens))
		for lien in neurone.tabLiens:
			#print(type(lien))
			print('poids = {}'.format(lien.poids))
			print('source = {}'.format(lien.source))
print("done")