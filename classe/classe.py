#import numpy as np
class poids():

	def __init__(self,poids,source):
		self.poids = poids
		self.source = source

class neurone():

	def __init__(self, poidsNeurone, nbLiens):
		self.poidsNeurone = poidsNeurone
		self.tabLiens = []
		self.nbLiens = nbLiens

class couche():

	def __init__(self, nbNeurones):
		self.tabNeurone = []
		self.tabNeurone = nbNeurones

class reseaux():

	def __init__(self,nbCouches):
		self.tabCouche = []
		self.nbCouches = nbCouches
		




		