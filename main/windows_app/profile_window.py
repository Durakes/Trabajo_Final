from tkinter import *
import windows_app.dashboard_window as dw
import windows_app.newPayment_window as npw
import os
from PIL import Image, ImageTk

my_path = os.getcwd()
print(my_path)

visaLogo = None
paypalLogo = None
mastercardLogo = None

def Profile(root, mainFrame):

    root.title("Profile")

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "425", height = "852")
    mainFrame.pack()
    global visaLogo 
    visaLogo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\Visa.png").resize((50,25), Image.ANTIALIAS))
    global paypalLogo 
    paypalLogo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\Paypal.png").resize((52,20), Image.ANTIALIAS))
    global mastercardLogo
    mastercardLogo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\Mastercard.png").resize((50,28), Image.ANTIALIAS))

    Label(mainFrame, text = "Perfil").place(x = 190, y = 50)
    Label(mainFrame, text = "Nombre: ").place(x = 200, y = 100)
    Label(mainFrame, text = "Apellidos: ").place(x = 200, y = 130)
    Label(mainFrame, text = "Correo: ").place(x = 200, y = 160)

    Label(mainFrame, text = "Cuentas asociadas:").place(x = 70, y = 250)

    Label(mainFrame, image = paypalLogo).place(x = 50, y = 320)
    Label(mainFrame, text = "**** 1234", bg = "white").place(x = 110, y = 320)
    Label(mainFrame, text = "01/22", bg = "white").place(x = 170, y = 320)
    Button(mainFrame, text = "Borrar").place(x = 300, y = 320)

    Label(mainFrame, image = visaLogo).place(x = 50, y = 355)
    Label(mainFrame, text = "**** 1234", bg = "white").place(x = 110, y = 360)
    Label(mainFrame, text = "01/22", bg = "white").place(x = 170, y = 360)
    Button(mainFrame, text = "Borrar").place(x = 300, y = 360)

    Label(mainFrame, image = mastercardLogo).place(x = 50, y = 400)
    Label(mainFrame, text = "**** 1234", bg = "white").place(x = 110, y = 400)
    Label(mainFrame, text = "01/22", bg = "white").place(x = 170, y = 400)
    Button(mainFrame, text = "Borrar").place(x = 300, y = 400)

    Button(mainFrame, text = "Agregar nuevo método de pago", command = lambda: npw.NewPaymenMethod(root, mainFrame)).place(x = 110, y = 450)
    Button(mainFrame, text = "Volver", command = lambda: dw.Dashboard(root, mainFrame)).place(x = 180, y = 500 )
