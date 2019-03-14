
import sys
sys.path.insert(0, "classe/")
sys.path.insert(0, "function/")
sys.path.insert(0, "UI/")

from ui import *

gui=ui()
#gui.wrapper.save_config()

gui.wrapper.root.mainloop()
