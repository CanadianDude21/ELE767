
import classe, random, fetch
from tkinter import *
from tkinter.filedialog import *
import configPoids
import FuncActivation as act
import numpy as np
import algo
import string
import os


class topWrapper():

	def __init__(self):
		self.root=Tk()
		self.entrys=[]
		self.gui_config_path 		= StringVar(value="config/config.txt")
		self.gui_datasetTrain_path 	= StringVar(value="DATA/data_train.txt")
		self.gui_datasetVC_path 	= StringVar(value="DATA/data_vc.txt")
		self.gui_datasetTest_path 	= StringVar(value="DATA/data_test.txt")
		self.gui_nbrEpoquestr 		= StringVar(value="0")
		self.gui_TauAppVar		 	= IntVar()
		self.gui_meanPourcentAPP 	= DoubleVar()
		self.gui_meanPourcentVC 	= DoubleVar()
		self.gui_meanPourcentTEST	= DoubleVar()
		self.gui_epoqueNumber		= IntVar()

		#config
		self.baseConfigName="SeqConfig/"
		self.currentConfigPathName=""
		self.config = fetch.getConfig(pathToConfig=self.gui_config_path.get())
		self.update_config_for_gui(self.config)
		self.configui = self.config 
		self.configSortie=fetch.getConfigSortie(self.config["FichierConfigSortie"])

		

		#dataset
		self.datasetTrain = fetch.getEpoque(nombreTrame=self.config["nbTrames"],pathToDataSet=self.gui_datasetTrain_path.get())
		self.datasetVC = fetch.getEpoque(nombreTrame=self.config["nbTrames"],pathToDataSet=self.gui_datasetVC_path.get())
		self.datasetTest = fetch.getEpoque(nombreTrame=self.config["nbTrames"],pathToDataSet=self.gui_datasetTrain_path.get())
		

		self.output = np.asarray(self.configSortie)

		#
		self.meanPourcentAPP = 0.0
		self.meanPourcentVC = 0.1
		self.meanPourcentTEST= 0.2

		self.nbrReussiteVC = 0
		self.nbrReussiteTEST = 0

		self.totalVC 	= 0
		self.totalTEST 	= 0
		self.TauAppVar 	= False
		self.epoqueNumber =0
		#network
		self.bestReseau = classe.reseaux(self.config)

	# les fonctions ici sont appeler par les boutons

	def train(self):
		self.epoqueNumber =0
		self.gui_meanPourcentTEST.set(self.epoqueNumber)
		self.TauAppVar=bool(self.gui_TauAppVar.get())
		print (len(self.datasetTrain[0].data))
		for nbEpoques in range (int(self.gui_nbrEpoquestr.get())):
			self.meanPourcentAPP = algo.apprentissage(self.bestReseau,self.datasetTrain,self.output,self.TauAppVar)
			for x in range (5):
				nbrReussiteVc, totalVC =algo.VC(self.bestReseau,self.datasetVC,self.output)
				self.totalVC += totalVC
				self.nbrReussiteVC += nbrReussiteVc
			for x in range (5):
				nbrReussiteTEST, totalTEST =algo.test(self.bestReseau,self.datasetTest,self.output)
				self.totalTEST += totalTEST
				self.nbrReussiteTEST += nbrReussiteTEST
			self.meanPourcentVC=self.nbrReussiteVC/self.totalVC
			self.meanPourcentTEST=self.nbrReussiteTEST/self.totalTEST
			self.gui_meanPourcentAPP.set(self.meanPourcentAPP)
			self.gui_meanPourcentVC.set(self.meanPourcentVC)
			self.gui_meanPourcentTEST.set(self.meanPourcentTEST)
			self.epoqueNumber += 1
			self.gui_epoqueNumber.set(self.epoqueNumber)
			self.root.update()
			print("======== epoqueNumber:" + str(self.epoqueNumber) + "========\n")
			print("meanPourcentAPP:" + str(self.meanPourcentAPP) + "\n")
			print("meanPourcentVC:" + str(self.meanPourcentVC) + "\n")
			print("meanPourcentTEST:" + str(self.meanPourcentTEST) + "\n")
			self.nbrReussiteVC = 0
			self.nbrReussiteTEST= 0
			self.totalVC = 0
			self.totalTEST = 0

	def VC(self):
		algo.VC(self.bestReseau,self.datasetVC,self.output)

	def generalisation(self):
		algo.test(self.bestReseau,self.datasetTest,self.output)

	#les fonctions suivantes sont utiliser pour allez chercher des fichiers
	def browse_load_poids(self):
		load_poids_path = askdirectory ()
		configPoids.chargerPoids(self.bestReseau,load_poids_path)

	def browse_datasetTrain_path(self):
		self.gui_datasetTrain_path.set(askopenfilename())
		self.datasetTrain = fetch.getEpoque(nombreTrame=self.config["nbTrames"],pathToDataSet=self.gui_datasetTrain_path.get())


	def browse_datasetVC_path(self):
		self.gui_datasetVC_path.set(askopenfilename())
		self.datasetVC = fetch.getEpoque(nombreTrame=self.config["nbTrames"],pathToDataSet=self.gui_datasetVC_path.get())

	def browse_datasetTest_path(self):
		self.gui_datasetTest_path.set(askopenfilename())
		self.datasetTest = fetch.getEpoque(nombreTrame=self.config["nbTrames"],pathToDataSet=self.gui_datasetTrain_path.get())


	def browse_config(self):
		self.gui_config_path.set(askopenfilename())
		self.config = fetch.getConfig(pathToConfig=self.gui_config_path.get())
		self.update_config_for_gui(self.config)
		self.configui = self.config 
		self.update_gui_entrys()
		print (len(self.datasetTrain[0].data))
		self.datasetTrain = fetch.getEpoque(nombreTrame=self.config["nbTrames"],pathToDataSet=self.gui_datasetTrain_path.get())
		self.datasetVC = fetch.getEpoque(nombreTrame=self.config["nbTrames"],pathToDataSet=self.gui_datasetVC_path.get())
		self.datasetTest = fetch.getEpoque(nombreTrame=self.config["nbTrames"],pathToDataSet=self.gui_datasetTrain_path.get())
		self.bestReseau = classe.reseaux(self.config)
		

	#fonctions de sauvegarde de la config entree par lutilisateur
	# cette fonction est connecter au boutons de l'interface graphique
	def save_config (self):

		baseConfigName=self.baseConfigName
		configLine=""
		configFileString=""

		for keys in self.configui.keys():
			if keys != "foncActi":
				if type(self.configui[keys])!=list:
					configLine=configLine+str(self.configui[keys])+"_"
				else :
					for element in range(len(self.configui[keys])):
						configLine=configLine+str(self.configui[keys][element])+" "	
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
		if not os.path.exists(currentConfigPathName):
			with open(currentConfigPathName, 'w') as outfile:

				for keys in self.configui.keys():
					if keys != "foncActi":
						if keys != "neuroneCacher":
							configFileString=configFileString+keys+":"+str(self.configui[keys])+"\n"
						else :
							configFileString=configFileString+keys+":"
							for element in range(len(self.configui[keys])):
								configFileString=configFileString+str(self.configui[keys][element])+" "	
							configFileString=configFileString+"\n"
				outfile.write(configFileString)
			outfile.close()

		configPoids.sauvegardePoids(self.bestReseau,self.currentConfigPathName)


	#fonctions local utilisees par la classe
	def update_gui_entrys(self):

		for keys, entry in zip(self.config.keys(), self.entrys):
			entry.delete(0, END)
			entry.insert(0, self.config[keys])

	def update_config_for_gui(self, config):

		if config["fonctionActivation"] == act.sigmoid:
			config["foncActi"] = act.sigmoid
			config["fonctionActivation"] = "sigmoid"
		elif config["fonctionActivation"] == act.tanh:
			config["fonctionActivation"] = "tanh"
			config["foncActi"] = act.tanh
		else:
			print("nope")

	def updateCurrentConfig(self, configkeys, configlist):
		for keys, conf in zip(configkeys, configlist):
			if keys != "foncActi":
				if keys != "neuroneCacher":
					self.configui[keys] = conf.get()#
					if re.search(r'^[-+]?[0-9]+$', self.configui[keys]):  # trouve les nombres dans les info de la config
						self.configui[keys] = int(self.configui[keys])
					else:
						if re.search(r'^[-+]?\d+\.\d+$', self.configui[keys]):  # trouve les nombres a virgule dans les info de la config
							self.configui[keys]= float(self.configui[keys])
				else:
					self.configui[keys] = [int(x) for x in (conf.get()).split(" ") ]

		if self.configui["fonctionActivation"] == "sigmoid":
			self.configui["foncActi"] = act.sigmoid
		elif self.configui["fonctionActivation"] == "tanh":
			self.configui["foncActi"] = act.tanh
		else:
			print("nope")

		self.configui = self.config
		self.datasetTrain = fetch.getEpoque(nombreTrame=self.config["nbTrames"],
											pathToDataSet=self.gui_datasetTrain_path.get())
		self.datasetVC = fetch.getEpoque(nombreTrame=self.config["nbTrames"],
										 pathToDataSet=self.gui_datasetVC_path.get())
		self.datasetTest = fetch.getEpoque(nombreTrame=self.config["nbTrames"],
										   pathToDataSet=self.gui_datasetTrain_path.get())
		self.bestReseau = classe.reseaux(self.config)