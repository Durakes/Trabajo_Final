from tkinter import *
from tkinter import ttk
from tkcalendar import *
import windows_app.dashboard_window as dashboard_w
import os
#! Variables
totalSpend = 0
categoriesNames = ["Entretenimiento", "Comida", "Educación", "Ropa", "Otros"]

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

def Register(root, mainFrame):
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

    paymentsNames = GetPaymets()
    Label(mainFrame, text = "Seleccione el modo de pago empleado").place(x = 110, y = 190)
    global paymentsDropBox
    paymentsDropBox = ttk.Combobox(mainFrame)
    paymentsDropBox.set("Selecciona una opción")
    paymentsDropBox["values"] = paymentsNames
    paymentsDropBox.place(x = 145, y = 215)

    Label(mainFrame, text = "Ingrese la fecha de la compra").place(x = 110, y = 260)
    global varDateEntry
    varDateEntry = DateEntry(mainFrame, selectmode ="day")
    varDateEntry.place(x = 145, y = 285)

    Label(mainFrame, text = "Ingrese el nombre de la tienda o servicio").place(x = 110, y = 330)
    global storeEntry
    storeEntry = StringVar()
    Entry(mainFrame, width = 25, borderwidth = 2, textvariable = storeEntry).place(x = 145, y = 355)

    Button(mainFrame, text = "Guardar", width = 10, command = lambda: GetRegisters(root, mainFrame)).place(x = 80, y = 450)
    Button(mainFrame, text = "Cancelar", width = 10, command = lambda: dashboard_w.Dashboard(root, mainFrame)).place(x = 250, y = 450)

def GetRegisters(root, mainFrame):
    amount = amountEntry.get()
    category = categoriesDropBox.get()
    payment = paymentsDropBox.get()
    
    global totalSpend
    totalSpend = totalSpend + int(amount)
    date_ = varDateEntry.get_date() #! Return a datetime.date
    month = date_.month
    store = storeEntry.get()

    my_path = os.getcwd()
    file = open(my_path + r"\main\fakedb\registers.txt", "a", encoding="UTF-8")
    file.write(str(amount) + "," + str(category) + "," + str(payment) + "," + str(date_) + "," + str(month) + "," + str(store) + "\n")
    file.close()
    dashboard_w.Dashboard(root, mainFrame)