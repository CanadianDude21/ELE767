
import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")

import classe, random, fetch
import tkinter as tk
import numpy as np


#dataset = fetch.getEpoque(nombreTrame=50)
#print("len:",len(dataset[0].data))

#indiceInput = random.randrange(0,len(dataset))
#inputChoisie = np.asarray(dataset[indiceInput].data)
#config = fetch.getConfig()
#configSortie=fetch.getConfigSortie(config["FichierConfigSortie"])
#output = np.asarray(configSortie)
#outputDesire = output[dataset[indiceInput].resultat]

#bestReseau = classe.reseaux(config)
#bestReseau.train(inputChoisie, outputDesire, 1)
#print(bestReseau.lay1.shape)






root = tk.Tk()
root.title('background image')
# pick a .gif image file you have in the working directory
fname = "wf.png"
bg_image = tk.PhotoImage(file=fname)
# get the width and height of the image
w = bg_image.width()
h = bg_image.height()
# size the window so the image will fill it
root.geometry("%dx%d+50+30" % (w, h))
cv = tk.Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=bg_image, anchor='nw')
# add canvas text at coordinates x=15, y=20
# anchor='nw' implies upper left corner coordinates
cv.create_text(15, 20, text="Python Greetings", fill="red", anchor='nw')
# now add some button widgets
btn1 = tk.Button(cv, text="Click")
btn1.pack(side='left', padx=10, pady=5, anchor='sw')
btn2 = tk.Button(cv, text="Quit", command=root.destroy)
btn2.pack(side='left', padx=10, pady=5, anchor='sw')

entry = tk.Entry(cv, justify="center")
entry.pack(side = "right")
entry2 = tk.Entry(cv, justify="center")
entry2.pack(side = "right")
entry3 = tk.Entry(cv, justify="center")
entry3.pack(side = "right")

btn2.pack(side='right', padx=10, pady=5, anchor='sw')
root.mainloop()