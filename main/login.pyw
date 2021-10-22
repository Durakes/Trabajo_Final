import tkinter
from tkinter import *

root = Tk()
root.title("Login")
root.resizable(0,0)

mainFrame = Frame()
mainFrame.config(width = "425", height = "852")
mainFrame.pack()

Label(mainFrame, text = "Logo").place(x = 180, y = 150)
Label(mainFrame, text = "Username").place(x = 90, y = 200)
Label(mainFrame, text = "Password").place(x = 90, y = 230)

Entry(mainFrame, width = 25, borderwidth = 2).place(x = 190, y = 200)
Entry(mainFrame, width = 25, borderwidth = 2, show = "*").place(x = 190, y = 230)

Button(mainFrame, text = "Log in", width = 20).place(x = 150, y = 280)

root.mainloop() 