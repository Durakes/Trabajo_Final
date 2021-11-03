from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import windows_app.dashboard_window as dw

testList = [["Enero",2000,20], ["Febrero",1000, 10], ["Marzo",1000, 10], ["Abril",1000, 10], ["Mayo",1000, 10], ["Junio",1000, 10], ["Julio",1000, 10], ["Agosto",1000, 10], ["Septiembre",1000, 10], ["Octubre",1000, 10], ["Noviembre",1000, 10], ["Diciembre",1000, 10]]
payments = ["Visa", "Master\nCard", "Paypal"]
categories = ["Entreten.","Comida", "Educación", "Ropa", "Otros"]
colors = ["red", "blue", "green", "yellow", "black"]
colors2 = ["red", "blue", "green"]
months = ["Septiembre", "Octubre", "Noviembre", "Diciembre", "Enero"]
amounts = [10, 20, 30, 10, 50]
amounts2 = [3000, 100, 450]

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
    paymentMethodsReport, payGraph = plt.subplots(dpi = 80, figsize = (5,2.3), sharey = True, facecolor = "#f0f0ed")
    paymentMethodsReport.suptitle("Reporte mensual por tipo de pago")
    payGraph.barh(payments, amounts2)

    payGraph.set_xlim(0, max(amounts2)*1.2)
    for i in range(len(payments)):
        payGraph.text(amounts2[i], i, amounts2[i], ha = "left", va= "center")

    paymentsCanvas = FigureCanvasTkAgg(paymentMethodsReport, master = mainFrame)
    paymentsCanvas .draw()
    paymentsCanvas .get_tk_widget().place(x = 20, y = 330)

def CreateTable(mainFrame):
    lastMonthTable = ttk.Treeview(mainFrame, columns = (1,2,3), show = "headings", height = "10")

    lastMonthTable.place(x = 50, y = 550)

    lastMonthTable.column(1, width = 100)
    lastMonthTable.column(2, width=100, anchor=CENTER)
    lastMonthTable.column(3, width=100, anchor=CENTER)

    lastMonthTable.heading(1, text = "Mes")
    lastMonthTable.heading(2, text = "Total Gastado")
    lastMonthTable.heading(3, text = "Diferencia")

    for i in range(len(testList)):
        lastMonthTable.insert("", "end", values=testList[i])