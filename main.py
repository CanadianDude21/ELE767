
import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")

import tkinter as tk
import topWrapper as topW
wrapper=topW.topWrapper()






#root = tk.Tk()
wrapper.root.title('background image')
# pick a .gif image file you have in the working directory
fname = "wf.png"
bg_image = tk.PhotoImage(file=fname)
# get the width and height of the image
w = bg_image.width()
h = bg_image.height()
# size the window so the image will fill it
wrapper.root.geometry("%dx%d+50+30" % (w, h))
cv = tk.Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
#cv.create_image(0, 0, image=bg_image, anchor='nw')
# add canvas text at coordinates x=15, y=20
# anchor='nw' implies upper left corner coordinates
#cv.create_text(15, 20, text="Fichier de configuration : "+ wrapper.config_path, fill="red", anchor='nw')
# now add some button widgets
champ_label = tk.Label(wrapper.root, textvariable=wrapper.config_path,justify="left", anchor='nw')
champ_label.pack()
champ_label.place(height=30, width=600)

btn1 = tk.Button(cv, text="Train", command=wrapper.train)
btn1.pack(side='left', padx=10, pady=5, anchor='sw')
btn2 = tk.Button(cv, text="Quit", command=wrapper.root.destroy)
btn2.pack(side='left', padx=10, pady=5, anchor='sw')

#entry = tk.Entry(cv, justify="center")
#entry.pack(side = "right")
#entry2 = tk.Entry(cv)
#entry2.pack(side = "right")
#entry3 = tk.Entry(cv, justify="center")
#entry3.pack(side = "right")



menubar = tk.Menu(wrapper.root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open dataset", command=wrapper.browse_dataset)
filemenu.add_command(label="Open config", command=wrapper.browse_config)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=wrapper.root.quit)
menubar.add_cascade(label="File", menu=filemenu)

wrapper.root.config(menu=menubar)




wrapper.root.mainloop()
