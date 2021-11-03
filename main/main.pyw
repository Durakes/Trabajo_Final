from tkinter import *
import os
import windows_app.login_window as lg

my_path = os.getcwd()
root = Tk()
root.resizable(0,0)
mainFrame = Frame(root)
lg.Login(root, mainFrame)

def quit_me():
    root.quit()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", quit_me)
root.mainloop()