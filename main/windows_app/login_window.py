from tkinter import *
import windows_app.dashboard_window as dashboard_w

def Login(root, mainFrame):
    root.title("Inicio")
    mainFrame.config(width = "425", height = "852")
    mainFrame.pack()
    
    Label(mainFrame, text = "Logo").place(relx = 0.5, rely = 0.2)
    
    Button(mainFrame, text = "INICIO", width = 20, height = 3, command = lambda: dashboard_w.Dashboard(root, mainFrame)).place(relx = 0.35, y = 280)