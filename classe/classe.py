import numpy as np
import random

class reseaux():

	def __init__(self,config):

		self.tauxApp = config["tauxApprentissage"]
		self.lay0 = np.asarray(donnee)
		self.lay1 = np.random.uniform(-0.1,0.1,(config["nbDonneeEntrant"], config["neuroneEntree"]))
		self.lay2 = np.random.uniform(-0.1,0.1,(config["neuroneEntree"], config["neuroneCacher"]))
		self.lay3 = np.random.uniform(-0.1,0.1,(config["neuroneCacher"], config["neuroneSortie"]))




		