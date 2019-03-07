
import classe, random, fetch
from tkinter import *
from tkinter.filedialog import askopenfilename
import numpy as np
import string
import os


class topWrapper():

	def __init__(self):
		self.root=Tk()

		self.config_path_name = "config/config.txt"
		self.dataset_path_name = "DATA/data_train.txt"
		self.config_path = StringVar()#"config/config.txt"
		self.dataset_path = StringVar()#"DATA/data_train.txt"
		self.config_path.set(self.config_path_name)
		self.dataset_path.set(self.dataset_path_name)
		#config
		print(self.config_path.get())
		self.config = fetch.getConfig(pathToConfig=self.config_path.get())
		self.configSortie=fetch.getConfigSortie(self.config["FichierConfigSortie"])
		
		#dataset
		self.dataset = fetch.getEpoque(pathToDataSet=self.dataset_path.get())
		self.indiceInput = random.randrange(0,len(self.dataset))
		self.inputChoisie = np.asarray(self.dataset[self.indiceInput].data)

		self.output = np.asarray(self.configSortie)
		self.outputDesire = self.output[self.dataset[self.indiceInput].resultat]

		#network
		self.bestReseau = classe.reseaux(self.config)

	# les foncitons ici sont des bouttons
	def train(self):
		self.bestReseau.train(self.inputChoisie, self.outputDesire,1)


	def browse_dataset(self):
		self.dataset_path_name = askopenfilename()
		self.dataset_path.set(self.dataset_path_name)
		print(self.dataset_path.get())

	def browse_config(self):
		config_path_name= askopenfilename()

		self.config_path.set(config_path_name)
		print(self.config_path.get())
