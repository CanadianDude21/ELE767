
import classe, random, fetch
from tkinter import *
from tkinter.filedialog import askopenfilename
import FuncActivation as act
import numpy as np
import string
import os


class topWrapper():

	def __init__(self):
		self.root=Tk()

		self.config_path = StringVar(value="config/config.txt")
		self.datasetTrain_path = StringVar(value="DATA/data_train.txt")
		self.datasetVC_path = StringVar(value="DATA/data_vc.txt")
		self.datasetTest_path = StringVar(value="DATA/data_test.txt")

		#config
		self.config = fetch.getConfig(pathToConfig=self.config_path.get())
		self.update_config_for_gui()
		self.configSortie=fetch.getConfigSortie(self.config["FichierConfigSortie"])

		
		#dataset
		self.datasetTrain = fetch.getEpoque(nombreTrame=self.config["nbTrames"],pathToDataSet=self.datasetTrain_path.get())
		self.datasetVC = fetch.getEpoque(nombreTrame=self.config["nbTrames"],pathToDataSet=self.datasetVC_path.get())
		self.datasetTest = fetch.getEpoque(nombreTrame=self.config["nbTrames"],pathToDataSet=self.datasetTrain_path.get())
		

		self.output = np.asarray(self.configSortie)


		#network
		self.bestReseau = classe.reseaux(self.config)

	# les foncitons ici sont des bouttons
	def train(self):
		algo.apprentissage(bestReseau,self.datasetTrain,self.output,nbrEpoques)

	def VC(self):
		algo.VC(bestReseau,datasetVC,output)

	def generalisation(self):
		algo.test(bestReseau,datasetTest,output)

	def browse_datasetTrain_path(self):
		self.datasetTrain_path.set(askopenfilename())


	def browse_datasetVC_path(self):
		self.datasetVC_path.set(askopenfilename())

	def browse_datasetTest_path(self):
		self.datasetTest_path.set(askopenfilename())

	def browse_config(self):
		self.config_path.set(askopenfilename())



	def update_config_for_gui(self):

		if self.config["fonctionActivation"]==act.sigmoid:
			self.config["foncActi"]=act.sigmoid
			self.config["fonctionActivation"]="sigmoid"
		elif self.config["fonctionActivation"]==act.tanh:
			self.config["fonctionActivation"]="tanh"
			self.config["foncActi"]=act.tanh
		else:
			print("nope")