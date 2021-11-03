from tkinter import *
import windows_app.profile_window as pw

def NewPaymenMethod(root, mainFrame):
    root.title("Agregar Método de Pago")

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "425", height = "852")
    mainFrame.pack()

    Label(mainFrame, text = "Nombre de la Tarjeta").place(x = 50, y = 200)
    paymentNameEntry = Entry(mainFrame, width = 20, borderwidth = 2)
    paymentNameEntry.place(x = 200, y = 200)

    Label(mainFrame, text = "Tipo de Tarjeta").place(x = 50, y = 230)
    cardType = Entry(mainFrame, width = 20, borderwidth = 2)
    cardType.place(x = 200, y = 230)

    Label(mainFrame, text = "Número de la Tarjeta").place(x = 50, y = 260)
    cardNumber = Entry(mainFrame, width = 20, borderwidth = 2)
    cardNumber.place(x = 200, y = 260)

    Label(mainFrame, text = "Fecha de Expiración").place(x = 50, y = 290)
    cardDate = Entry(mainFrame, width = 20, borderwidth = 2)
    cardDate.place(x = 200, y = 290)

    Button(mainFrame, text = "Guardar", command = lambda: pw.Profile(root, mainFrame)).place(x = 120, y = 390)
    Button(mainFrame, text = "Cancelar", command = lambda: pw.Profile(root, mainFrame)).place(x = 250, y = 390)