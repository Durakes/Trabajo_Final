from tkinter import *

import windows_app.login_window as login_w
import helpers.readfiles as readfiles

#my_path = readfiles.Route()

root = Tk()
root.resizable(0,0)
mainFrame = Frame(root)
login_w.Login(root, mainFrame)

def quit_me():
    root.quit()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", quit_me)
root.mainloop()