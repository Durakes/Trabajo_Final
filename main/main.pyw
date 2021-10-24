from tkinter import *
import os
from PIL import Image,ImageTk
my_path = os.getcwd()
root = Tk()
root.resizable(0,0)

# ! Frames
dashboardFrame = Frame()
registerFrame = Frame()
loginFrame = Frame()
profileFrame = Frame()
paymentFrame = Frame()

# ! Variables de Login
usernameEntry = Entry()
passwordEntry = Entry()

# ! Variables de Dashboard
categoryEntry = Entry()
paymentEntry = Entry()
dateEntry = Entry()
topAmount = Label()
currentAmount = Label()

# ! Variables de Profile

visaLogo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\Visa.png").resize((50,25), Image.ANTIALIAS))
paypalLogo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\Paypal.png").resize((52,20), Image.ANTIALIAS))
mastercardLogo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\Mastercard.png").resize((50,28), Image.ANTIALIAS))

# ! Variables de Registro
amountEntry = Entry()
storeEntry = Entry()
categoryEntry = Entry()
paymentEntry = Entry()
dateEntry = Entry()


def Login():                    # Primera pantalla de login
    root.title("Login")

    loginFrame.config(width = "425", height = "852")
    loginFrame.pack()
    
    Label(loginFrame, text = "Logo").place(x = 180, y = 150)
    Label(loginFrame, text = "Username").place(x = 90, y = 200)
    Label(loginFrame, text = "Password").place(x = 90, y = 230)

    usernameEntry = Entry(loginFrame, width = 25, borderwidth = 2)
    usernameEntry.place(x = 190, y = 200)
    usernameEntry.pack_propagate(0)

    passwordEntry = Entry(loginFrame, width = 25, borderwidth = 2, show = "*")
    passwordEntry.place(x = 190, y = 230)
    passwordEntry.pack_propagate(0)
    
    Button(loginFrame, text = "Log in", width = 20, command = Dashboard).place(x = 130, y = 280)

def Register():                 # Pantalla de registro de nuevo gasto
    root.title("Register")

    dashboardFrame.pack_forget()

    registerFrame.config(width = "425", height = "852")
    registerFrame.pack()

    Label(registerFrame, text = "Ingrese el monto gastado").place(x = 150, y = 50)
    amountEntry = Entry(registerFrame, width = 25, borderwidth = 2)
    amountEntry.place(x = 145, y = 75)


    Label(registerFrame, text = "Seleccione la categoría correspondiente").place(x = 110, y = 120)
    categoryEntry = Entry(registerFrame, width = 25, borderwidth = 2, fg = "gray")
    categoryEntry.place(x = 145, y = 145)
    categoryEntry.insert(0, "Seleccione una opción")

    Label(registerFrame, text = "Seleccione el modo de pago empleado").place(x = 110, y = 190)
    paymentEntry = Entry(registerFrame, width = 25, borderwidth = 2, fg = "gray")
    paymentEntry.place(x = 145, y = 215)
    paymentEntry.insert(0, "Seleccione una opción")

    Label(registerFrame, text = "Ingrese la fecha de la compra").place(x = 110, y = 260)
    dateEntry = Entry(registerFrame, width = 25, borderwidth = 2, fg = "gray")
    dateEntry.place(x = 145, y = 285)
    dateEntry.insert(0, "dd/mm/aaaa")

    Label(registerFrame, text = "Ingrese el nombre de la tienda o servicio").place(x = 110, y = 330)
    storeEntry = Entry(registerFrame, width = 25, borderwidth = 2)
    storeEntry.place(x = 145, y = 355)

    Button(registerFrame, text = "Guardar", width = 10, command = Dashboard).place(x = 80, y = 450)
    Button(registerFrame, text = "Cancelar", width = 10, command = Dashboard).place(x = 250, y = 450)


def Profile():                  # Pantalla de perfil de usuario
    root.title("Profile")

    dashboardFrame.pack_forget()
    paymentFrame.pack_forget()

    profileFrame.config(width = "425", height = "852")
    profileFrame.pack()

    Label(profileFrame, text = "Perfil").place(x = 190, y = 50)
    Label(profileFrame, text = "Nombre: ").place(x = 200, y = 100)
    Label(profileFrame, text = "Apellidos: ").place(x = 200, y = 130)
    Label(profileFrame, text = "Correo: ").place(x = 200, y = 160)

    Label(profileFrame, text = "Cuentas asociadas:").place(x = 70, y = 250)

    Label(profileFrame, image = paypalLogo).place(x = 50, y = 320)
    Label(profileFrame, text = "**** 1234", bg = "white").place(x = 110, y = 320)
    Label(profileFrame, text = "01/22", bg = "white").place(x = 170, y = 320)
    Button(profileFrame, text = "Borrar").place(x = 300, y = 320)

    Label(profileFrame, image = visaLogo).place(x = 50, y = 355)
    Label(profileFrame, text = "**** 1234", bg = "white").place(x = 110, y = 360)
    Label(profileFrame, text = "01/22", bg = "white").place(x = 170, y = 360)
    Button(profileFrame, text = "Borrar").place(x = 300, y = 360)

    Label(profileFrame, image = mastercardLogo).place(x = 50, y = 400)
    Label(profileFrame, text = "**** 1234", bg = "white").place(x = 110, y = 400)
    Label(profileFrame, text = "01/22", bg = "white").place(x = 170, y = 400)
    Button(profileFrame, text = "Borrar").place(x = 300, y = 400)

    Button(profileFrame, text = "Agregar nuevo método de pago", command = NewPaymenMethod).place(x = 110, y = 450)
    Button(profileFrame, text = "Volver", command = Dashboard).place(x = 180, y = 500 )


def Dashboard():            # Dashboard de los últimos movimientos realizados por el usuario

    root.title("Dashboard")

    loginFrame.pack_forget()
    profileFrame.pack_forget()
    registerFrame.pack_forget()

    dashboardFrame.config(width = "425", height = "852")
    dashboardFrame.pack()
    
    Label(dashboardFrame, text = "Límite establecido: ").place(x = 150, y = 30)
    topAmount = Label(dashboardFrame, text = "$" + "100000")
    topAmount.place(x = 170, y = 50)

    Label(dashboardFrame, text = "Usted está gastando en el mes: ").place(x = 120, y = 100)
    currentAmount = Label(dashboardFrame, text = "$" + "100000")
    currentAmount.place(x = 170, y = 120)

    Label(dashboardFrame, text = "Fecha").place(x = 50, y = 200)
    Label(dashboardFrame, text = "Tienda").place(x = 200, y = 200)
    Label(dashboardFrame, text = "Monto").place(x = 340, y = 200)

    Label(dashboardFrame, text = "21/10/2021", bg = "white").place(x = 50, y = 230)
    Label(dashboardFrame, text = "Amazon", bg = "white").place(x = 200, y = 230)
    Label(dashboardFrame, text = "$500", bg = "white").place(x = 340, y = 230)

    Label(dashboardFrame, text = "21/10/2021", bg = "white").place(x = 50, y = 260)
    Label(dashboardFrame, text = "Amazon", bg = "white").place(x = 200, y = 260)
    Label(dashboardFrame, text = "$500", bg = "white").place(x = 340, y = 260)

    Label(dashboardFrame, text = "21/10/2021", bg = "white").place(x = 50, y = 290)
    Label(dashboardFrame, text = "Amazon", bg = "white").place(x = 200, y = 290)
    Label(dashboardFrame, text = "$500", bg = "white").place(x = 340, y = 290)

    Label(dashboardFrame, text = "21/10/2021", bg = "white").place(x = 50, y = 320)
    Label(dashboardFrame, text = "Amazon", bg = "white").place(x = 200, y = 320)
    Label(dashboardFrame, text = "$500", bg = "white").place(x = 340, y = 320)

    Label(dashboardFrame, text = "21/10/2021", bg = "white").place(x = 50, y = 350)
    Label(dashboardFrame, text = "Amazon", bg = "white").place(x = 200, y = 350)
    Label(dashboardFrame, text = "$500", bg = "white").place(x = 340, y = 350)

    Button(dashboardFrame, text = "Registro", width = 10, command = Register).place(x = 50, y = 500)
    Button(dashboardFrame, text = "Reportes", width = 10).place(x = 170, y = 500)
    Button(dashboardFrame, text = "Perfil", width = 10, command = Profile).place(x = 290, y = 500)
    Button(dashboardFrame, text = "Salir", width = 10, command = quit).place(x = 170, y = 550)


def NewPaymenMethod():
    root.title("Agregar Método de Pago")

    profileFrame.pack_forget()

    paymentFrame.config(width = "425", height = "852")
    paymentFrame.pack()

    Label(paymentFrame, text = "Nombre de la Tarjeta").place(x = 50, y = 200)
    paymentNameEntry = Entry(paymentFrame, width = 20, borderwidth = 2)
    paymentNameEntry.place(x = 200, y = 200)

    Label(paymentFrame, text = "Tipo de Tarjeta").place(x = 50, y = 230)
    cardType = Entry(paymentFrame, width = 20, borderwidth = 2)
    cardType.place(x = 200, y = 230)

    Label(paymentFrame, text = "Número de la Tarjeta").place(x = 50, y = 260)
    cardNumber = Entry(paymentFrame, width = 20, borderwidth = 2)
    cardNumber.place(x = 200, y = 260)

    Label(paymentFrame, text = "Fecha de Expiración").place(x = 50, y = 290)
    cardDate = Entry(paymentFrame, width = 20, borderwidth = 2)
    cardDate.place(x = 200, y = 290)

    Button(paymentFrame, text = "Guardar", command = Profile).place(x = 120, y = 390)
    Button(paymentFrame, text = "Cancelar", command = Profile).place(x = 250, y = 390)

Login()

root.mainloop() 