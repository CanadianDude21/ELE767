
import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")


import tkinter as tk
import topWrapper as topW

wrapper=topW.topWrapper()


wrapper.root.title('background image')
# pick a .gif image file you have in the working directory
fname = "wf.png"
bg_image = tk.PhotoImage(file=fname)
# get the width and height of the image
w = bg_image.width()
h = bg_image.height()
# size the window so the image will fill it
wrapper.root.geometry("%dx%d+50+30" % (w, h))
#cv = tk.Canvas(width=w, height=h)
#cv.pack(side='top', fill='both', expand='yes')
#cv.grid(row=0,column=0)
#cv.create_image(0, 0, image=bg_image, anchor='nw')

# add canvas text at coordinates x=15, y=20
# anchor='nw' implies upper left corner coordinates
#cv.create_text(15, 20, text="Fichier de configuration : "+ wrapper.config_path, fill="red", anchor='nw')
# now add some button widgets
configPathLabel = tk.Label(wrapper.root,justify="left", anchor='nw',text="configPath:")
configPathLabel.grid(row=1,column=0)
configPathLabelVar = tk.Label(wrapper.root, textvariable=wrapper.config_path,justify="left", anchor='nw')
configPathLabelVar.grid(row=1,column=1)


datasetPathLabel = tk.Label(wrapper.root,justify="left", anchor='nw',text="datasetPath:")
datasetPathLabel.grid(row=2,column=0)
datasetPathLabelVar = tk.Label(wrapper.root, textvariable=wrapper.dataset_path,justify="left", anchor='nw')
datasetPathLabelVar.grid(row=2,column=1)


#champ_label.place(height=30, width=600)

btn1 = tk.Button(wrapper.root, text="Train", command=wrapper.train)
#btn1.pack(side='left', padx=10, pady=5, anchor='sw')
btn3 = tk.Button(wrapper.root, text="Train", command=wrapper.train)
btn2 = tk.Button(wrapper.root, text="Quit", command=wrapper.root.destroy)
btn1.grid(row=30 ,column=2)
btn2.grid(row=31 ,column=2)
btn2.grid(row=32 ,column=2)


for keys,x in zip(wrapper.config.keys(),range(len(wrapper.config))):
	if keys != "foncActi" :
		tk.Label(wrapper.root,justify="left", anchor='nw',text=keys).grid(row=2+x,column=6)
		tk.Entry(wrapper.root, justify="center",textvariable=tk.StringVar(value=wrapper.config[keys])).grid(row=2+x,column=7)





menubar = tk.Menu(wrapper.root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open dataset", command=wrapper.browse_dataset)
filemenu.add_command(label="Open config", command=wrapper.browse_config)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=wrapper.root.quit)
menubar.add_cascade(label="File", menu=filemenu)

wrapper.root.config(menu=menubar)




wrapper.root.mainloop()
