from tkinter import *
import windows_app.register_window as rw
import windows_app.reports_window as rpw
import windows_app.profile_window as pw

def Dashboard(root, mainFrame):          # Dashboard de los últimos movimientos realizados por el usuario

    root.title("Dashboard")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "425", height = "852")
    mainFrame.pack()
    
    Label(mainFrame, text = "Límite establecido: ").place(x = 150, y = 30)
    topAmount = Label(mainFrame, text = str(rw.totalSpend))
    topAmount.place(x = 170, y = 50)

    Label(mainFrame, text = "Usted está gastando en el mes: ").place(x = 120, y = 100)
    currentAmount = Label(mainFrame, text = str(rw.totalSpend))
    currentAmount.place(x = 170, y = 120)

    Label(mainFrame, text = "Fecha").place(x = 50, y = 200)
    Label(mainFrame, text = "Tienda").place(x = 200, y = 200)
    Label(mainFrame, text = "Monto").place(x = 340, y = 200)

    Label(mainFrame, text = "21/10/2021", bg = "white").place(x = 50, y = 230)
    Label(mainFrame, text = "Amazon", bg = "white").place(x = 200, y = 230)
    Label(mainFrame, text = "$500", bg = "white").place(x = 340, y = 230)

    Label(mainFrame, text = "21/10/2021", bg = "white").place(x = 50, y = 260)
    Label(mainFrame, text = "Amazon", bg = "white").place(x = 200, y = 260)
    Label(mainFrame, text = "$500", bg = "white").place(x = 340, y = 260)

    Label(mainFrame, text = "21/10/2021", bg = "white").place(x = 50, y = 290)
    Label(mainFrame, text = "Amazon", bg = "white").place(x = 200, y = 290)
    Label(mainFrame, text = "$500", bg = "white").place(x = 340, y = 290)

    Label(mainFrame, text = "21/10/2021", bg = "white").place(x = 50, y = 320)
    Label(mainFrame, text = "Amazon", bg = "white").place(x = 200, y = 320)
    Label(mainFrame, text = "$500", bg = "white").place(x = 340, y = 320)

    Label(mainFrame, text = "21/10/2021", bg = "white").place(x = 50, y = 350)
    Label(mainFrame, text = "Amazon", bg = "white").place(x = 200, y = 350)
    Label(mainFrame, text = "$500", bg = "white").place(x = 340, y = 350)

    Button(mainFrame, text = "Registro", width = 10, command = lambda: rw.Register(root, mainFrame)).place(x = 50, y = 500)
    Button(mainFrame, text = "Reportes", width = 10, command = lambda: rpw.Reports(root, mainFrame)).place(x = 170, y = 500)
    Button(mainFrame, text = "Perfil", width = 10, command = lambda: pw.Profile(root, mainFrame)).place(x = 290, y = 500)
    Button(mainFrame, text = "Salir", width = 10, command = quit).place(x = 170, y = 550)