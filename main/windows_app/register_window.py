from tkinter import *
from tkinter import ttk
import windows_app.dashboard_window as dw

#! Variables

totalSpend = 0

categoriesDictionary = {"Entretenimiento" : 0, "Comida" : 0, "Educación" : 0, "Ropa" : 0, "Otros" : 0}
paymentsDic = [["Visa", 0], ["MasterCard", 0], ["Paypal", 0]]
categoriesNames= ["Entretenimiento", "Comida", "Educación", "Ropa", "Otros"]

paymentAmount = []

def Register(root, mainFrame):                 # Pantalla de registro de nuevo gasto
    root.title("Register")
    global amountEntry
    amountEntry = StringVar()

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "425", height = "852")
    mainFrame.pack()

    Label(mainFrame, text = "Ingrese el monto gastado").place(x = 150, y = 50)
    Entry(mainFrame, width = 25, borderwidth = 2, textvariable = amountEntry).place(x = 145, y = 75)

    Label(mainFrame, text = "Seleccione la categoría correspondiente").place(x = 110, y = 120)
    global categoriesDropBox 
    categoriesDropBox= ttk.Combobox(mainFrame)
    categoriesDropBox.set("Selecciona una opción")
    categoriesDropBox["values"]  = categoriesNames
    categoriesDropBox.place(x = 145, y = 145)

    Label(mainFrame, text = "Seleccione el modo de pago empleado").place(x = 110, y = 190)
    paymentEntry = Entry(mainFrame, width = 25, borderwidth = 2, fg = "gray")
    paymentEntry.place(x = 145, y = 215)
    paymentEntry.insert(0, "Seleccione una opción")

    Label(mainFrame, text = "Ingrese la fecha de la compra").place(x = 110, y = 260)
    dateEntry = Entry(mainFrame, width = 25, borderwidth = 2, fg = "gray")
    dateEntry.place(x = 145, y = 285)
    dateEntry.insert(0, "dd/mm/aaaa")

    Label(mainFrame, text = "Ingrese el nombre de la tienda o servicio").place(x = 110, y = 330)
    storeEntry = Entry(mainFrame, width = 25, borderwidth = 2)
    storeEntry.place(x = 145, y = 355)

    Button(mainFrame, text = "Guardar", width = 10, command = GetRegisters).place(x = 80, y = 450)
    Button(mainFrame, text = "Cancelar", width = 10, command = lambda: dw.Dashboard(root, mainFrame)).place(x = 250, y = 450)

def GetRegisters():
    amount = amountEntry.get()
    category = categoriesDropBox.get()
    global totalSpend
    totalSpend = totalSpend + int(amount)
    for name in categoriesDictionary:
        if name == category:
            categoriesDictionary[name] = categoriesDictionary[name] + int(amount)
            break