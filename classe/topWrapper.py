
import classe, random, fetch
from tkinter import *
from tkinter.filedialog import askopenfilename
import numpy as np
import string
import os


class topWrapper():

	def __init__(self):
		self.root=Tk()

		self.config_path = StringVar()
		self.dataset_path = StringVar()
		self.config_path.set("config/config.txt")
		self.dataset_path.set("DATA/data_train.txt")

		#config
		self.config = fetch.getConfig(pathToConfig=self.config_path.get())
		self.configSortie=fetch.getConfigSortie(self.config["FichierConfigSortie"])

		
		#dataset
		self.datasetTrain = fetch.getEpoque(nombreTrame=self.config["nbrTrames"],"DATA/data_train.txt")
		self.datasetVC = fetch.getEpoque(nombreTrame=self.config["nbrTrames"],"DATA/data_vc.txt")
		self.datasetTest = fetch.getEpoque(nombreTrame=self.config["nbrTrames"],"DATA/data_test.txt")
		

		self.output = np.asarray(self.configSortie)
		self.outputDesire = self.output[self.dataset[self.indiceInput].resultat]

		#network
		self.bestReseau = classe.reseaux(self.config)

	# les foncitons ici sont des bouttons
	def train(self):
		algo.apprentissage(bestReseau,self.data)


	def browse_dataset(self):
		self.dataset_path.set(askopenfilename())
		print(self.dataset_path.get())

	def browse_config(self):
		self.config_path.set(askopenfilename())
		print(self.config_path.get())
