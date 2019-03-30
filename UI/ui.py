import tkinter as tk
import topWrapper as topW
import FuncActivation as act


class ui:

	def __init__ (self):
		self.wrapper=topW.topWrapper()

		self.configkeys=[]
		self.configlist=[]


		#montre les differents fichiers necessaires ainsi que ceux qui sont actuellement utiliser par le programme
		configPathLabel = tk.Label(self.wrapper.root,justify="left", anchor='nw',text="configPath:")
		configPathLabel.grid(row=1,column=0)
		configPathLabelVar = tk.Label(self.wrapper.root, textvariable=self.wrapper.gui_config_path,justify="left", anchor='nw')
		configPathLabelVar.grid(row=1,column=1)
		tk.Label(self.wrapper.root,justify="left", anchor='nw',text="datasetTrainPath:").grid(row=2,column=0)
		tk.Label(self.wrapper.root, textvariable=self.wrapper.gui_datasetTrain_path,justify="left", anchor='nw').grid(row=2,column=1,columnspan=3)
		tk.Label(self.wrapper.root,justify="left", anchor='nw',text="datasetVC_path:").grid(row=3,column=0)
		tk.Label(self.wrapper.root, textvariable=self.wrapper.gui_datasetVC_path,justify="left", anchor='nw').grid(row=3,column=1,columnspan=3)
		tk.Label(self.wrapper.root,justify="left", anchor='nw',text="datasetTest_path:").grid(row=4,column=0)
		tk.Label(self.wrapper.root, textvariable=self.wrapper.gui_datasetTest_path,justify="left", anchor='nw').grid(row=4,column=1,columnspan=3)
		tk.Label(self.wrapper.root,justify="left", anchor='nw',text="datasetVC_path:").grid(row=3,column=0)


		#cree les boutons principaux sur l'interface graphique
		tk.Button(self.wrapper.root, text="Train", command=self.wrapper.train).grid(row=30 ,column=2)
		tk.Label(self.wrapper.root, anchor='nw',textvariable=self.wrapper.gui_meanPourcentAPP).grid(row=30,column=3,columnspan=3)
		tk.Button(self.wrapper.root, text="generalisation", command=self.wrapper.generalisation).grid(row=32 ,column=2)
		tk.Label(self.wrapper.root, anchor='nw',textvariable=self.wrapper.gui_meanPourcentTEST).grid(row=32,column=4,columnspan=3)
		tk.Button(self.wrapper.root, text="Quit", command=self.wrapper.root.destroy).grid(row=33 ,column=2)


		tk.Checkbutton(self.wrapper.root, text="gui_lvq2", variable=self.wrapper.gui_lvq2).grid(row=30, column=1)


		#boutons de sauvegarde pour la configuration du reseaux de neurones
		tk.Button(self.wrapper.root, text="update Current Config", height = 5, width = 20, command=lambda:self.wrapper.updateCurrentConfig(self.configkeys,self.configlist)).grid(columnspan=3,row=33,column=30)
		tk.Button(self.wrapper.root, text="Save Config et poid", height = 5, width = 20, command=self.wrapper.save_config).grid(columnspan=3,row=33,column=33)



		tk.Label(self.wrapper.root,justify="left", anchor='nw',text="EpoquesCourante").grid(row=28,column=2)
		tk.Label(self.wrapper.root, justify="center",textvariable=self.wrapper.gui_epoqueNumber).grid(row=28,column=3)
		tk.Label(self.wrapper.root,justify="left", anchor='nw',text="nbrEpoques").grid(row=29,column=2)
		tk.Entry(self.wrapper.root, justify="center",textvariable=self.wrapper.gui_nbrEpoquestr).grid(row=29,column=3)

		#genere les entres pouvant etre modifier par l'utilisateur
		x=0
		for keys in self.wrapper.config.keys():
			self.configkeys.append(keys)
			if keys != "foncActi" :
				tk.Label(self.wrapper.root,justify="left", anchor='nw',text=keys).grid(row=2+x,column=6)
				self.configlist.append(tk.Entry(self.wrapper.root, justify="center",textvariable=tk.StringVar(value=self.wrapper.config[keys])))
				self.configlist[x].grid(row=2+x,column=7)
				x+=1


		self.wrapper.entrys = self.configlist


		#gere le menu defillant
		menubar = tk.Menu(self.wrapper.root)
		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="load dataset Train", command=self.wrapper.browse_datasetTrain_path)
		filemenu.add_command(label="load dataset VC", command=self.wrapper.browse_datasetVC_path)
		filemenu.add_command(label="load dataset Test", command=self.wrapper.browse_datasetTest_path)
		filemenu.add_command(label="load poids neurones", command=self.wrapper.browse_load_poids)
		filemenu.add_command(label="Open config", command=self.wrapper.browse_config)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.wrapper.root.quit)
		menubar.add_cascade(label="File", menu=filemenu)

		self.wrapper.root.config(menu=menubar)



