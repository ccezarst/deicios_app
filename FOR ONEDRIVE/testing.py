from tkinter import *
import time

frame = Tk()

def load(a):
	if a:
		toplevel.destroy()
	else:
		toplevel = Toplevel()
		Label(toplevel, text="adadasdawsd")
		toplevel.mainloop()

load(False)
time.sleep(5)
load(True)

frane.mainloop()