
import classe, random, fetch
from tkinter import *
from tkinter.filedialog import askopenfilename
import FuncActivation as act
import numpy as np
import algo
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
		self.baseConfigName="SeqConfig/"
		self.currentConfigPathName=""
		self.configui={}
		self.config = fetch.getConfig(pathToConfig=self.config_path.get())
		self.update_config_for_gui(self.config)
		self.configSortie=fetch.getConfigSortie(self.config["FichierConfigSortie"])

		

		#dataset
		self.datasetTrain = fetch.getEpoque(nombreTrame=self.config["nbTrames"],pathToDataSet=self.datasetTrain_path.get())
		self.datasetVC = fetch.getEpoque(nombreTrame=self.config["nbTrames"],pathToDataSet=self.datasetVC_path.get())
		self.datasetTest = fetch.getEpoque(nombreTrame=self.config["nbTrames"],pathToDataSet=self.datasetTrain_path.get())
		

		self.output = np.asarray(self.configSortie)


		self.meanPourcentVC =0
		self.meanPourcentTEST=0
		self.epoqueNumber =0 
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

	def browse_load_poids(self):
		load_poids_path.set(askdirectory ())


	def browse_datasetVC_path(self):
		self.datasetVC_path.set(askopenfilename())

	def browse_datasetTest_path(self):
		self.datasetTest_path.set(askopenfilename())

	def browse_config(self):
		self.config_path.set(askopenfilename())



	def update_config_for_gui(self,config):

		if config["fonctionActivation"]==act.sigmoid:
			config["foncActi"]=act.sigmoid
			config["fonctionActivation"]="sigmoid"
		elif config["fonctionActivation"]==act.tanh:
			config["fonctionActivation"]="tanh"
			config["foncActi"]=act.tanh
		else:
			print("nope")



	def updateCurrentConfig(self,configkeys,configlist):
		for keys,conf in zip(configkeys, configlist) :
			if keys !="foncActi":
				self.configui[keys] = conf.get()
				print (conf.get())

		if self.configui["fonctionActivation"]=="sigmoid":
			self.configui["foncActi"]=act.sigmoid
		elif self.configui["fonctionActivation"]=="tanh":
			self.configui["foncActi"]=act.tanh
		else:
			print("nope")

	def save_config (self):

		baseConfigName=self.baseConfigName
		configLine=""
		configFileString=""

		for keys in self.configui.keys():
			if keys != "foncActi":
				configLine=configLine+str(self.configui[keys])+"_"
		if not os.path.exists(baseConfigName+configLine):
			os.makedirs(baseConfigName+configLine)

		self.currentConfigPathName=baseConfigName+configLine

		currentConfigPathName=self.currentConfigPathName+"/config.txt"
		savePathForConfigRM=baseConfigName+"ConfigRM.txt"

		if not os.path.exists(savePathForConfigRM):
			with open(savePathForConfigRM, 'w') as outfile:
				tmpstr=""
				for keys in self.configui.keys():
					if keys != "foncActi":
						tmpstr+=keys+"_"

				outfile.write(configLine+"\n")
				outfile.write(tmpstr+"\n")
				outfile.write("la postion du premier chiffre correspond a nombreCoucheCachees et ainsi de suite...")

			outfile.close()

		#if not os.path.exists(self.currentConfigPathName):
		with open(self.currentConfigPathName, 'w') as outfile:

			for keys in self.configui.keys():
				if keys != "foncActi":
					configFileString=configFileString+keys+":"+str(self.configui[keys])+"\n"
			outfile.write(configFileString)
		outfile.close()

		#conf.sauvegardPoids(self.bestReseau,self.currentConfigPathName)