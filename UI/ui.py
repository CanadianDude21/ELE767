import tkinter as tk
import topWrapper as topW
import FuncActivation as act


class ui:

	def __init__ (self):
		self.wrapper=topW.topWrapper()
		self.wrapper.root.title('background image')
# pick a .gif image file you have in the working directory
		self.fname = "wf.png"
		self.bg_image = tk.PhotoImage(file=self.fname)
# get the width and height of the image
		self.w = self.bg_image.width()
		self.h = self.bg_image.height()
# size the window so the image will fill it
		self.wrapper.root.geometry("%dx%d+50+30" % (self.w, self.h))
		self.configkeys=[]
		self.configlist=[]
#cv = tk.Canvas(width=w, height=h)
#cv.pack(side='top', fill='both', expand='yes')
#cv.grid(row=0,column=0)
#cv.create_image(0, 0, image=bg_image, anchor='nw')

# add canvas text at coordinates x=15, y=20
# anchor='nw' implies upper left corner coordinates
#cv.create_text(15, 20, text="Fichier de configuration : "+ wrapper.config_path, fill="red", anchor='nw')
# now add some button widgets
		configPathLabel = tk.Label(self.wrapper.root,justify="left", anchor='nw',text="configPath:")
		configPathLabel.grid(row=1,column=0)
		configPathLabelVar = tk.Label(self.wrapper.root, textvariable=self.wrapper.config_path,justify="left", anchor='nw')
		configPathLabelVar.grid(row=1,column=1)


		tk.Label(self.wrapper.root,justify="left", anchor='nw',text="datasetTrainPath:").grid(row=2,column=0)
		tk.Label(self.wrapper.root, textvariable=self.wrapper.datasetTrain_path,justify="left", anchor='nw').grid(row=2,column=1,columnspan=3)

		 
		tk.Label(self.wrapper.root,justify="left", anchor='nw',text="datasetVC_path:").grid(row=3,column=0)
		tk.Label(self.wrapper.root, textvariable=self.wrapper.datasetVC_path,justify="left", anchor='nw').grid(row=3,column=1,columnspan=3)
		tk.Label(self.wrapper.root,justify="left", anchor='nw',text="datasetTest_path:").grid(row=4,column=0)
		tk.Label(self.wrapper.root, textvariable=self.wrapper.datasetTest_path,justify="left", anchor='nw').grid(row=4,column=1,columnspan=3)




#champ_label.place(height=30, width=600)

		tk.Button(self.wrapper.root, text="Train", command=self.wrapper.train).grid(row=30 ,column=2)
		tk.Button(self.wrapper.root, text="TrainVc", command=self.wrapper.VC).grid(row=31 ,column=2)
		tk.Label(self.wrapper.root, anchor='nw',textvariable=tk.StringVar(value=self.wrapper.meanPourcentVC)).grid(row=31,column=3,columnspan=3)
		tk.Button(self.wrapper.root, text="generalisation", command=self.wrapper.generalisation).grid(row=32 ,column=2)
		tk.Label(self.wrapper.root, anchor='nw',textvariable=tk.StringVar(value=self.wrapper.meanPourcentTEST)).grid(row=32,column=4,columnspan=3)
		tk.Button(self.wrapper.root, text="Quit", command=self.wrapper.root.destroy).grid(row=33 ,column=2)



		tk.Button(self.wrapper.root, text="update Current Config", height = 5, width = 20, command=lambda:self.wrapper.updateCurrentConfig(self.configkeys,self.configlist)).grid(columnspan=3,row=33,column=30)
		tk.Button(self.wrapper.root, text="save Current Config", height = 5, width = 20, command=self.wrapper.save_config).grid(columnspan=3,row=33,column=33)

		for keys,x in zip(self.wrapper.config.keys(),range(len(self.wrapper.config))):
			self.configkeys.append(keys)
			if keys != "foncActi" :
				tk.Label(self.wrapper.root,justify="left", anchor='nw',text=keys).grid(row=2+x,column=6)
				self.configlist.append(tk.Entry(self.wrapper.root, justify="center",textvariable=tk.StringVar(value=self.wrapper.config[keys])))
				self.configlist[x].grid(row=2+x,column=7)





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



