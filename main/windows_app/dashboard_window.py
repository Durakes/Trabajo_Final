from tkinter import *
import windows_app.register_window as register_w
import windows_app.reports_window as reports_w
import windows_app.profile_window as profile_w
import os
from datetime import date

shownRegisters = []
#TODO juntar fors General List y Total Month spent
def CreateGeneralList():
    my_path = os.getcwd()
    file = open(my_path + r"\main\fakedb\registers.txt", "r", encoding="UTF-8")

    registers_ = file.readlines()
    for i in range (len(registers_)):
        registers_[i]=registers_[i].split(",")
    file.close()
    return registers_

def CreateDashList():
    registers_ = CreateGeneralList()
    shownRegisters = registers_[-5:]

    for i in range (len(shownRegisters)):
        shownRegisters[i][5] = shownRegisters[i][5][:-1]
    
    return shownRegisters

def TotalMonthSpent():
    registers_ = CreateGeneralList()
    amount = 0
    for i in range(len(registers_)):
        if date.today().month == int(registers_[i][4]):
            amount = amount + int(registers_[i][0])

    return amount

def TakeLimit():
    my_path = os.getcwd()
    limitfile = open(my_path + r"\main\fakedb\limits.txt")
    content = [limitfile.readlines()[-1]]
    for i in range(len(content)):
        content[i]=content[i].split(",")
    finalLimit = content[0][0]

    return finalLimit

def Dashboard(root, mainFrame):
    root.title("Dashboard")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "425", height = "852")
    mainFrame.pack()
    
    amount = TotalMonthSpent()
    shownRegisters = CreateDashList()
    finalLimit = TakeLimit()
    Label(mainFrame, text = "Límite establecido: ").place(x = 150, y = 30)
    Label(mainFrame, text = finalLimit).place(x = 170, y = 50)

    Label(mainFrame, text = "Usted está gastando en el mes: ").place(x = 120, y = 100)
    currentAmount = Label(mainFrame, text = amount)
    currentAmount.place(x = 170, y = 120)

    Label(mainFrame, text = "Últimos 5 gastos registrados: ").place(x = 50, y = 160)

    Label(mainFrame, text = "Fecha").place(x = 50, y = 200)
    Label(mainFrame, text = "Tienda").place(x = 200, y = 200)
    Label(mainFrame, text = "Monto").place(x = 340, y = 200)

    positiony = 230
    for i in range(len(shownRegisters)-1,-1,-1):
        Label(mainFrame, text = shownRegisters[i][3], bg = "white").place(x = 50, y = positiony)
        Label(mainFrame, text = shownRegisters[i][5], bg = "white").place(x = 200, y = positiony)
        Label(mainFrame, text = "S/." + shownRegisters[i][0], bg = "white").place(x = 340, y = positiony)
        positiony = positiony + 30

    Button(mainFrame, text = "Registro", width = 10, command = lambda: register_w.Register(root, mainFrame)).place(x = 50, y = 500)
    Button(mainFrame, text = "Reportes", width = 10, command = lambda: reports_w.Reports(root, mainFrame)).place(x = 170, y = 500)
    Button(mainFrame, text = "Perfil", width = 10, command = lambda: profile_w.Profile(root, mainFrame)).place(x = 290, y = 500)
    Button(mainFrame, text = "Salir", width = 10, command = quit).place(x = 170, y = 550)