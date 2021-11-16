from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import windows_app.dashboard_window as dashboard_w
import helpers.readfiles as readfiles
import os
from datetime import date

monthDic = {1: "Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}

categories = ["Entreten.","Comida", "Educación", "Ropa", "Otros"]

def GetPaymets():
    paymentsFile = readfiles.GetPaymentsFile()
    payments = []
    for i in range(len(paymentsFile)):
        payments.append(paymentsFile[i][0])
    
    return payments

def CreateTableValues():
    monthTuple = [["Enero",0], ["Febrero",0], ["Marzo",0], ["Abril",0], ["Mayo",0], ["Junio",0], ["Julio",0], ["Agosto",0], ["Septiembre",0], ["Octubre",0], ["Noviembre",0], ["Diciembre",0]]

    registers_ = readfiles.GetRegistersFile()

    for i in range (len(registers_)):
        for number in monthDic:
            if number == int(registers_[i][4]):
                for j in range(len(monthTuple)):
                    if monthTuple[j][0] == monthDic[number]:
                        monthTuple[j][1] = monthTuple[j][1] + float(registers_[i][0])
    
    return monthTuple

def CreateCategoryDic():
    registers_ = readfiles.GetRegistersFile()
    categories_ = ["Entretenimiento", "Comida", "Educación", "Ropa", "Otros"]

    categoriesDictionary = {category : 0.0 for category in categories_}
    
    for i in range(len(registers_)):
        if int(registers_[i][4]) == date.today().month:
            for name in categoriesDictionary:
                if name == registers_[i][1]:
                    categoriesDictionary[name] = categoriesDictionary[name] + float(registers_[i][0])

    return categoriesDictionary

def CreatePaymentDic():
    registers_ = readfiles.GetRegistersFile()
    payments_ = GetPaymets()

    paymentsDictionary = {payment : 0 for payment in payments_}

    for i in range(len(registers_)):
        if int(registers_[i][4]) == date.today().month:
            for name in paymentsDictionary:
                if name == registers_[i][2]:
                    paymentsDictionary[name] = paymentsDictionary[name] + float(registers_[i][0])

    return paymentsDictionary

def Reports(root, mainFrame):
    root.title("Reporte Mensual")
    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "1080", height = "425")
    mainFrame.pack()

    Label(mainFrame, text = "Reporte Mensual").place(x = 20, y = 20)
    Label(mainFrame, text = monthDic[date.today().month]).place(x = 1000, y = 20)

    CreateGraphV(mainFrame)

    CreateGraphH(mainFrame)

    CreateTable(mainFrame)

    Button(mainFrame, text = "Volver", width = 20, command = lambda: dashboard_w.Dashboard(root, mainFrame)).place(x = 460, y = 360)

def CreateGraphV(mainFrame):
    categoriesDictionary = CreateCategoryDic()

    categoryAmounts = [categoriesDictionary["Entretenimiento"], 
                categoriesDictionary["Comida"], 
                categoriesDictionary["Educación"], 
                categoriesDictionary["Ropa"], 
                categoriesDictionary["Otros"]]

    categoriesReport, catGraph = plt.subplots(dpi = 80, figsize = (5,3), sharey = True, facecolor = "#f0f0ed")
    categoriesReport.suptitle("Reporte mensual por categorías")
    catGraph.bar(categories, categoryAmounts)
    catGraph.set_ylim(0, max(categoryAmounts)*1.2)
    for i in range(len(categories)):
        catGraph.text(i, categoryAmounts[i], categoryAmounts[i], ha = "center", va= "bottom")

    categoriesCanvas = FigureCanvasTkAgg(categoriesReport, master = mainFrame)
    categoriesCanvas.draw()
    categoriesCanvas.get_tk_widget().place(x = 20, y = 90)

def CreateGraphH(mainFrame):
    paymentsDictionary = CreatePaymentDic()
    payments = GetPaymets()
    paymentsAmounts = []
    for name in paymentsDictionary:
        paymentsAmounts.append(paymentsDictionary[name])

    paymentMethodsReport, payGraph = plt.subplots(dpi = 80, figsize = (5,3), sharey = True, facecolor = "#f0f0ed")
    paymentMethodsReport.suptitle("Reporte mensual por tipo de pago")
    payGraph.barh(payments, paymentsAmounts)

    payGraph.set_xlim(0, max(paymentsAmounts)*1.2)
    for i in range(len(payments)):
        payGraph.text(paymentsAmounts[i], i, paymentsAmounts[i], ha = "left", va= "center")

    paymentsCanvas = FigureCanvasTkAgg(paymentMethodsReport, master = mainFrame)
    paymentsCanvas.draw()
    paymentsCanvas.get_tk_widget().place(x = 425, y = 90)

def CreateTable(mainFrame):
    monthList = CreateTableValues()
    lastMonthTable = ttk.Treeview(mainFrame, columns = (1,2), show = "headings", height = "10")

    lastMonthTable.place(x = 840, y = 90)

    lastMonthTable.column(1, width = 100)
    lastMonthTable.column(2, width=100, anchor=CENTER)

    lastMonthTable.heading(1, text = "Mes")
    lastMonthTable.heading(2, text = "Total Gastado")

    for i in range(len(monthList)):
        lastMonthTable.insert("", "end", values=monthList[i])