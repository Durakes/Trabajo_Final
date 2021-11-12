from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import windows_app.profile_window as profile_w
import os

def NewPaymenMethod(root, mainFrame):
    root.title("Agregar Método de Pago")
    global cardID
    global cardNumber
    global monthExp
    global yearExp
    cardID = StringVar()
    cardNumber = StringVar()
    monthExp = StringVar()
    yearExp = StringVar()


    payments_=["Visa","Master Card", "PayPal"]

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "425", height = "852")
    mainFrame.pack()

    Label(mainFrame, text = "Nombre de la Tarjeta").place(x = 50, y = 200)
    Entry(mainFrame, width = 20, borderwidth = 2, textvariable=cardID).place(x = 200, y = 200)

    Label(mainFrame, text = "Tipo de Tarjeta").place(x = 50, y = 230)
    global cardType
    cardType = ttk.Combobox(mainFrame, width = 20)
    cardType["values"] = payments_
    cardType.place(x = 200, y = 230)

    Label(mainFrame, text = "Número de la Tarjeta").place(x = 50, y = 260)
    Entry(mainFrame, width = 20, borderwidth = 2, textvariable = cardNumber).place(x = 200, y = 260)

    Label(mainFrame, text = "Fecha de Expiración").place(x = 50, y = 290)
    Label(mainFrame, text = "Mes:").place(x = 170, y = 290)
    Entry(mainFrame, width = 20, borderwidth = 2, textvariable = monthExp).place(x = 200, y = 290)
    Label(mainFrame, text = "Año:").place(x = 250, y = 290)
    Entry(mainFrame, width = 8, borderwidth = 2, textvariable = yearExp).place(x = 280, y = 290)

    Button(mainFrame, text = "Guardar", command = lambda: SavePaymentType(root, mainFrame)).place(x = 120, y = 390)
    Button(mainFrame, text = "Cancelar", command = lambda: profile_w.Profile(root, mainFrame)).place(x = 250, y = 390)

def SavePaymentType(root, mainFrame):
    global index
    
    cardname = cardID.get()
    cardnum = cardNumber.get()
    cardtype = cardType.get()
    expmonth = monthExp.get()
    expyear = yearExp.get()
    
    if int(expmonth) > 12 or int(expyear) <= 2021:
        MessageBox.showwarning("Cuidado", "La fecha ingresada no es válida, intente nuevamente")
        NewPaymenMethod(root, mainFrame) #! Verificar, solo limpiar los datos
    else: 
        if len(expmonth) == 1:
            expmonth="0"+expmonth
        
        if cardtype=="Visa":
            index=1
        elif cardtype=="Master Card":
            index=2
        elif cardtype=="PayPal":
            index=3

        last_four=cardnum[-4:]

        my_path = os.getcwd()
        cards = open(my_path + r"\main\fakedb\payments.txt", "a", encoding = "UTF-8")
        cards.write(cardname + "," + str(index) + "," + cardtype + "," + last_four + "," + expmonth + "," + expyear + "\n")
        cards.close()
        profile_w.Profile(root, mainFrame)