from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import windows_app.dashboard_window as dashboard_w
import os
from datetime import date

monthDic = {1: "Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}

categories = ["Entreten.","Comida", "Educación", "Ropa", "Otros"]

def GetPaymets():
    my_path = os.getcwd()
    file = open(my_path + r"\main\fakedb\payments.txt", "r", encoding="UTF-8")
    paymentsFile = file.readlines()
    payments = []
    for i in range (len(paymentsFile)):
        paymentsFile[i] = paymentsFile[i].split(",")

    for i in range(len(paymentsFile)):
        payments.append(paymentsFile[i][0])
    
    return payments

def CreateList():
    my_path = os.getcwd()
    file = open(my_path + r"\main\fakedb\registers.txt", "r", encoding="UTF-8")

    registers_ = file.readlines()

    for i in range (len(registers_)):
        registers_[i] = registers_[i].split(",")
    file.close()

    #? Por si se necesita leer las tiendas luego
    #!for i in range(len(registers_)):
        #!registers_[i][4] = registers_[i][4][:-1]

    return registers_

def CreateTableValues():
    testList = [["Enero",0], ["Febrero",0], ["Marzo",0], ["Abril",0], ["Mayo",0], ["Junio",0], ["Julio",0], ["Agosto",0], ["Septiembre",0], ["Octubre",0], ["Noviembre",0], ["Diciembre",0]]

    registers_ = CreateList()

    for i in range (len(registers_)):
        for number in monthDic:
            if number == int(registers_[i][4]):
                for j in range(len(testList)):
                    if testList[j][0] == monthDic[number]:
                        testList[j][1] = testList[j][1] + int(registers_[i][0])
    
    return testList

def CreateCategoryDic():
    registers_ = CreateList()
    categories_ = ["Entretenimiento", "Comida", "Educación", "Ropa", "Otros"]

    categoriesDictionary = {category : 0 for category in categories_}
    
    for i in range(len(registers_)):
        if int(registers_[i][4]) == date.today().month:
            for name in categoriesDictionary:
                if name == registers_[i][1]:
                    categoriesDictionary[name] = categoriesDictionary[name] + int(registers_[i][0])

    return categoriesDictionary

def CreatePaymentDic():
    registers_ = CreateList()
    payments_ = GetPaymets()

    paymentsDictionary = {payment : 0 for payment in payments_}

    for i in range(len(registers_)):
        if int(registers_[i][4]) == date.today().month:
            for name in paymentsDictionary:
                if name == registers_[i][2]:
                    paymentsDictionary[name] = paymentsDictionary[name] + int(registers_[i][0])

    return paymentsDictionary

def Reports(root, mainFrame):
    #TODO Alinear elementos
    root.title("Reporte Mensual")
    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "425", height = "852")
    mainFrame.pack()

    Label(mainFrame, text = "Reporte Mensual").place(x = 20, y = 20)
    Label(mainFrame, text = monthDic[date.today().month]).place(x = 320, y = 20)

    CreateGraphV(mainFrame)

    Label(mainFrame, text = "Métodos de pago mas usados").place(x = 50, y = 300)

    CreateGraphH(mainFrame)

    Label(mainFrame, text = "Resumen gasto total de los últimos 5 meses").place(x = 50, y = 520)

    CreateTable(mainFrame)

    Button(mainFrame, text = "Volver", width = 20, command = lambda: dashboard_w.Dashboard(root, mainFrame)).place(x = 125, y = 810)

def CreateGraphV(mainFrame):
    categoriesDictionary = CreateCategoryDic()

    global amounts
    amounts = [categoriesDictionary["Entretenimiento"], 
                categoriesDictionary["Comida"], 
                categoriesDictionary["Educación"], 
                categoriesDictionary["Ropa"], 
                categoriesDictionary["Otros"]]

    categoriesReport, catGraph = plt.subplots(dpi = 80, figsize = (5,3), sharey = True, facecolor = "#f0f0ed")
    categoriesReport.suptitle("Reporte mensual por categorías")
    catGraph.bar(categories, amounts)
    catGraph.set_ylim(0, max(amounts)*1.2)
    for i in range(len(categories)):
        catGraph.text(i, amounts[i], amounts[i], ha = "center", va= "bottom")

    categoriesCanvas = FigureCanvasTkAgg(categoriesReport, master = mainFrame)
    categoriesCanvas.draw()
    categoriesCanvas.get_tk_widget().place(x = 20, y = 60)

def CreateGraphH(mainFrame):
    paymentsDictionary = CreatePaymentDic()
    payments = GetPaymets()
    amounts2 = []
    for name in paymentsDictionary:
        amounts2.append(paymentsDictionary[name])

    paymentMethodsReport, payGraph = plt.subplots(dpi = 80, figsize = (5,2.3), sharey = True, facecolor = "#f0f0ed")
    paymentMethodsReport.suptitle("Reporte mensual por tipo de pago")
    payGraph.barh(payments, amounts2)

    payGraph.set_xlim(0, max(amounts2)*1.2)
    for i in range(len(payments)):
        payGraph.text(amounts2[i], i, amounts2[i], ha = "left", va= "center")

    paymentsCanvas = FigureCanvasTkAgg(paymentMethodsReport, master = mainFrame)
    paymentsCanvas.draw()
    paymentsCanvas.get_tk_widget().place(x = 20, y = 330)

def CreateTable(mainFrame):
    monthList = CreateTableValues()
    lastMonthTable = ttk.Treeview(mainFrame, columns = (1,2), show = "headings", height = "10")

    lastMonthTable.place(x=110, y=550)

    lastMonthTable.column(1, width = 100)
    lastMonthTable.column(2, width=100, anchor=CENTER)

    lastMonthTable.heading(1, text = "Mes")
    lastMonthTable.heading(2, text = "Total Gastado")

    for i in range(len(monthList)):
        lastMonthTable.insert("", "end", values=monthList[i])