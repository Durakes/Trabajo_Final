from tkinter import *

root = Tk()
root.title("Register Entry")
root.resizable(0,0)

mainFrame = Frame()
mainFrame.config(width = "425", height = "852")
mainFrame.pack()

Label(mainFrame, text = "Ingrese el monto gastado").place(x = 150, y = 50)
Entry(mainFrame, width = 25, borderwidth = 2).place(x = 145, y = 75)

Label(mainFrame, text = "Seleccione la categoría correspondiente").place(x = 110, y = 120)
categoryEntry = Entry(mainFrame, width = 25, borderwidth = 2, fg = "gray")
categoryEntry.place(x = 145, y = 145)
categoryEntry.insert(0, "Seleccione una opción")

Label(mainFrame, text = "Seleccione el modo de pago empleado").place(x = 110, y = 190)
paymentEntry = Entry(mainFrame, width = 25, borderwidth = 2, fg = "gray")
paymentEntry.place(x = 145, y = 215)
paymentEntry.insert(0, "Seleccione una opción")

Label(mainFrame, text = "Ingrese la fecha de la compra").place(x = 110, y = 260)
dateEntry = Entry(mainFrame, width = 25, borderwidth = 2, fg = "gray")
dateEntry.place(x = 145, y = 285)
dateEntry.insert(0, "dd/mm/aaaa")

Label(mainFrame, text = "Ingrese el nombre de la tienda o servicio").place(x = 110, y = 330)
Entry(mainFrame, width = 25, borderwidth = 2).place(x = 145, y = 355)

Button(mainFrame, text = "Guardar", width = 10).place(x = 80, y = 450)
Button(mainFrame, text = "Cancelar", width = 10).place(x = 250, y = 450)

root.mainloop()