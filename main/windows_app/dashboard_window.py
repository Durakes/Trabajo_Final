from tkinter import *
import windows_app.register_window as rw
import windows_app.reports_window as rpw
import windows_app.profile_window as pw
import os

shownRegisters = []
def CreateList():
    my_path = os.getcwd()
    file = open(my_path + r"\main\db\registers.txt", "r", encoding="UTF-8")

    registers_ = file.readlines()
    for i in range (len(registers_)):
        registers_[i]=registers_[i].split(",")
    file.close()
    shownRegisters = registers_[-5:]

    for i in range (len(shownRegisters)):
        shownRegisters[i][4] = shownRegisters[i][4][:-1]
    
    return shownRegisters

def Dashboard(root, mainFrame):
    root.title("Dashboard")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "425", height = "852")
    mainFrame.pack()
    
    shownRegisters = CreateList()

    Label(mainFrame, text = "Límite establecido: ").place(x = 150, y = 30)
    Label(mainFrame, text ="10000").place(x = 170, y = 50)

    Label(mainFrame, text = "Usted está gastando en el mes: ").place(x = 120, y = 100)
    currentAmount = Label(mainFrame, text = str(rw.totalSpend))
    currentAmount.place(x = 170, y = 120)

    Label(mainFrame, text = "Fecha").place(x = 50, y = 200)
    Label(mainFrame, text = "Tienda").place(x = 200, y = 200)
    Label(mainFrame, text = "Monto").place(x = 340, y = 200)

    Label(mainFrame, text = shownRegisters[4][3], bg = "white").place(x = 50, y = 230)
    Label(mainFrame, text = shownRegisters[4][4], bg = "white").place(x = 200, y = 230)
    Label(mainFrame, text = shownRegisters[4][0], bg = "white").place(x = 340, y = 230)

    Label(mainFrame, text = shownRegisters[3][3], bg = "white").place(x = 50, y = 260)
    Label(mainFrame, text = shownRegisters[3][4], bg = "white").place(x = 200, y = 260)
    Label(mainFrame, text = shownRegisters[3][0], bg = "white").place(x = 340, y = 260)

    Label(mainFrame, text = shownRegisters[2][3], bg = "white").place(x = 50, y = 290)
    Label(mainFrame, text = shownRegisters[2][4], bg = "white").place(x = 200, y = 290)
    Label(mainFrame, text = shownRegisters[2][0], bg = "white").place(x = 340, y = 290)

    Label(mainFrame, text = shownRegisters[1][3], bg = "white").place(x = 50, y = 320)
    Label(mainFrame, text = shownRegisters[1][4], bg = "white").place(x = 200, y = 320)
    Label(mainFrame, text = shownRegisters[1][0], bg = "white").place(x = 340, y = 320)

    Label(mainFrame, text = shownRegisters[0][3], bg = "white").place(x = 50, y = 350)
    Label(mainFrame, text = shownRegisters[0][4], bg = "white").place(x = 200, y = 350)
    Label(mainFrame, text = shownRegisters[0][0], bg = "white").place(x = 340, y = 350)

    Button(mainFrame, text = "Registro", width = 10, command = lambda: rw.Register(root, mainFrame)).place(x = 50, y = 500)
    Button(mainFrame, text = "Reportes", width = 10, command = lambda: rpw.Reports(root, mainFrame)).place(x = 170, y = 500)
    Button(mainFrame, text = "Perfil", width = 10, command = lambda: pw.Profile(root, mainFrame)).place(x = 290, y = 500)
    Button(mainFrame, text = "Salir", width = 10, command = quit).place(x = 170, y = 550)