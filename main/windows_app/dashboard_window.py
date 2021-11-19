from tkinter import *
import windows_app.register_window as register_w
import windows_app.reports_window as reports_w
import windows_app.profile_window as profile_w
import helpers.readfiles as readfiles
from datetime import date

#* Función que crea la lista de los últimos 5 registros.
def CreateDashList():
    registers_ = readfiles.GetRegistersFile()
    shownRegisters = registers_[-10:]

    for i in range (len(shownRegisters)):
        shownRegisters[i][5] = shownRegisters[i][5][:-1]
    
    return shownRegisters

#* Función que calcula y devuelve el total registrado del mes.
def TotalMonthSpent():
    registers_ = readfiles.GetRegistersFile()
    amount = 0.0
    for i in range(len(registers_)):
        if date.today().month == int(registers_[i][4]):
            amount = amount + float(registers_[i][0])

    return amount

#* Función que lee el límite para mostrarlo luego.
def TakeLimit():
    content = [readfiles.GetLimitFile()[-1]]

    for i in range(len(content)):
        content[i]=content[i].split(",")
    finalLimit = content[0][0]

    return finalLimit

#* Estructura de la ventana del Dashboard general.
def Dashboard(root, mainFrame):
    root.title("Dashboard")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "425", height = "852")
    #? mainFrame.config(width = "425", height = "670")
    mainFrame.pack()
    
    amount = TotalMonthSpent()
    shownRegisters = CreateDashList()
    finalLimit = TakeLimit()
    Label(mainFrame, text = "Límite establecido:  " + finalLimit).place(x = 140, y = 50)

    Label(mainFrame, text = "Usted está gastando en el mes:  " + str(amount)).place(x = 110, y = 100)

    Label(mainFrame, text = "Últimos 10 gastos registrados: ").place(x = 50, y = 160)

    Label(mainFrame, text = "Fecha").place(x = 50, y = 200)
    Label(mainFrame, text = "Tienda").place(x = 200, y = 200)
    Label(mainFrame, text = "Monto").place(x = 340, y = 200)

    positiony = 230
    for i in range(len(shownRegisters)-1,-1,-1):
        Label(mainFrame, text = shownRegisters[i][3], bg = "white").place(x = 50, y = positiony)
        Label(mainFrame, text = shownRegisters[i][5], bg = "white").place(x = 200, y = positiony)
        Label(mainFrame, text = "S/." + shownRegisters[i][0], bg = "white").place(x = 340, y = positiony)
        positiony = positiony + 30

    Button(mainFrame, text = "Registro", width = 10, command = lambda: register_w.Register(root, mainFrame)).place(x = 50, y = 550)
    Button(mainFrame, text = "Reportes", width = 10, command = lambda: reports_w.Reports(root, mainFrame)).place(x = 170, y = 550)
    Button(mainFrame, text = "Perfil", width = 10, command = lambda: profile_w.Profile(root, mainFrame)).place(x = 290, y = 550)
    Button(mainFrame, text = "Salir", width = 10, command = quit).place(x = 170, y = 600)