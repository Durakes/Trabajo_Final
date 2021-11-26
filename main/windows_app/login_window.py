from tkinter import *
import windows_app.dashboard_window as dashboard_w
import helpers.readfiles as readfiles
from PIL import Image, ImageTk

#* Estructura de la ventana de Inicio.
def Login(root, mainFrame):
    root.title("Inicio")
    mainFrame.config(width = "425", height = "852")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\Logo.png"))
    
    Label(mainFrame, image = logo).place(relx = 0.21, rely = 0.18)
    
    Button(mainFrame, text = "INICIO", width = 20, height = 3, command = lambda: dashboard_w.Dashboard(root, mainFrame)).place(relx = 0.32, y = 280)