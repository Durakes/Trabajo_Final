from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import windows_app.dashboard_window as dw
import os

testList = [["Enero",2000,20], ["Febrero",1000, 10], ["Marzo",1000, 10], ["Abril",1000, 10], ["Mayo",1000, 10], ["Junio",1000, 10], ["Julio",1000, 10], ["Agosto",1000, 10], ["Septiembre",1000, 10], ["Octubre",1000, 10], ["Noviembre",1000, 10], ["Diciembre",1000, 10]]
payments = ["Visa", "Master\nCard", "Paypal"]
categories = ["Entreten.","Comida", "Educación", "Ropa", "Otros"]
months = ["Septiembre", "Octubre", "Noviembre", "Diciembre", "Enero"]
amounts = []
amounts2 = []

def CreateList():
    my_path = os.getcwd()
    file = open(my_path + r"\main\db\registers.txt", "r", encoding="UTF-8")

    registers_ = file.readlines()

    for i in range (len(registers_)):
        registers_[i] = registers_[i].split(",")
    file.close()

    for i in range(len(registers_)):
        registers_[i][4] = registers_[i][4][:-1]
    
    for i in range(len(registers_)):
        registers_[i][0] = registers_[i][0][3:]

    return registers_

def CreateCategoryDic():
    registers_ = CreateList()
    categories_ = ["Entretenimiento","Comida", "Educación", "Ropa", "Otros"]

    categoriesDictionary = {category : 0 for category in categories_}
    
    for i in range(len(registers_)):
        for name in categoriesDictionary:
            if name == registers_[i][1]:
                categoriesDictionary[name] = categoriesDictionary[name] + int(registers_[i][0])

    return categoriesDictionary

def CreatePaymentDic():
    registers_ = CreateList()
    payments_ = ["Visa", "MasterCard", "Paypal"]

    paymentsDictionary = {payment : 0 for payment in payments_}

    for i in range(len(registers_)):
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
    Label(mainFrame, text = "Octubre").place(x = 320, y = 20)

    CreateGraphV(mainFrame)

    Label(mainFrame, text = "Métodos de pago mas usados").place(x = 50, y = 300)

    CreateGraphH(mainFrame)

    Label(mainFrame, text = "Resumen gasto total de los últimos 5 meses").place(x = 50, y = 520)

    CreateTable(mainFrame)

    Button(mainFrame, text = "Volver", width = 20, command = lambda: dw.Dashboard(root, mainFrame)).place(x = 120, y = 810)

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
    
    global amounts2
    amounts2 = [paymentsDictionary["Visa"], 
                paymentsDictionary["MasterCard"], 
                paymentsDictionary["Paypal"]]
    
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
    lastMonthTable = ttk.Treeview(mainFrame, columns = (1,2,3), show = "headings", height = "10")

    lastMonthTable.place(x=50, y=550)

    lastMonthTable.column(1, width = 100)
    lastMonthTable.column(2, width=100, anchor=CENTER)
    lastMonthTable.column(3, width=100, anchor=CENTER)

    lastMonthTable.heading(1, text = "Mes")
    lastMonthTable.heading(2, text = "Total Gastado")
    lastMonthTable.heading(3, text = "Diferencia")

    for i in range(len(testList)):
        lastMonthTable.insert("", "end", values=testList[i])