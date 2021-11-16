from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from tkcalendar import *
import windows_app.dashboard_window as dashboard_w
import helpers.readfiles as readfiles
from datetime import date

#* Función para crear la lista de los nombres de los tipos de pago creados.
def GetPaymets():
    paymentsFile = readfiles.GetPaymentsFile()
    payments = []

    for i in range(len(paymentsFile)):
        payments.append(paymentsFile[i][0])
    
    return payments

#* Función para verificar si el registro sobrepasa el límite. 
def VerifyLimit(amount,monthR, yearR):
    content = [readfiles.GetLimitFile()[-1]]
    currentAmount = TotalMonthSpent()
    for i in range(len(content)):
        content[i]=content[i].split(",")
    
    content[0][2] = content[0][2][:-1]
    
    if monthR == int(content[0][1]) and yearR == int(content[0][2]):
            if float(content[0][0]) > currentAmount + amount:
                return True
            else:
                return False
        
#* Función para calcular el total gastado en el mes.
def TotalMonthSpent():
    registers_ = readfiles.GetRegistersFile()
    amount = 0.0
    for i in range(len(registers_)):
        if date.today().month == int(registers_[i][4]):
            amount = amount + float(registers_[i][0])

    return amount

#* Función para guardar los registros en el archivo .txt
def GetRegisters(root, mainFrame):
    amount = amountEntry.get()
    category = categoriesDropBox.get()
    payment = paymentsDropBox.get()

    date_ = varDateEntry.get_date() #! Return a datetime.date
    month = date_.month
    store = storeEntry.get()

    my_path = readfiles.Route()
    limitVerified = VerifyLimit(float(amount), month, date_.year)

    if limitVerified == True:
        file = open(my_path + r"\main\fakedb\registers.txt", "a", encoding="UTF-8")
        file.write(str(amount) + "," + str(category) + "," + str(payment) + "," + str(date_) + "," + str(month) + "," + str(store) + "\n")
        file.close()
        dashboard_w.Dashboard(root, mainFrame)
    else:
        shouldContinue=MessageBox.askyesno(message = f"Con este gasto (S/.{amount}) está excediendo el límite establecido mensual. ¿Desea continuar?")
        if shouldContinue == True:
            file = open(my_path + r"\main\fakedb\registers.txt", "a", encoding="UTF-8")
            file.write(str(amount) + "," + str(category) + "," + str(payment) + "," + str(date_) + "," + str(month) + "," + str(store) + "\n")
            file.close()
            dashboard_w.Dashboard(root, mainFrame)
        else:
            dashboard_w.Dashboard(root, mainFrame)

#* Estructura de la ventana de Registro.
def Register(root, mainFrame):
    root.title("Registro")
    global amountEntry
    amountEntry = StringVar()

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "425", height = "852")
    mainFrame.pack()

    Label(mainFrame, text = "Ingrese el monto gastado").place(x = 150, y = 50)
    Entry(mainFrame, width = 25, borderwidth = 2, textvariable = amountEntry).place(x = 145, y = 75)

    categoriesNames = ["Entretenimiento", "Comida", "Educación", "Ropa", "Otros"]
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