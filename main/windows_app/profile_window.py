from tkinter import *
import windows_app.dashboard_window as dashboard_w
import windows_app.newPayment_window as payment_w
import os
from PIL import Image, ImageTk
from tkinter import messagebox as MessageBox

my_path = os.getcwd()

def CreateList():
    file = open(my_path + r"\main\fakedb\payments.txt", "r", encoding = "UTF-8")

    paymentsList = file.readlines()

    file.close()
    for i in range(len(paymentsList)):
        paymentsList[i] = paymentsList[i].split(",")
    
    for i in range (len(paymentsList)):
        paymentsList[i][5] = paymentsList[i][5][:-1]

    return paymentsList

def Erase(index, root, mainFrame):
    paymentsList = CreateList()

    answer = MessageBox.askyesno(message = "¿Desea continuar?")
    if answer == True:

        del paymentsList[index]
        file = open(my_path + r"\main\fakedb\payments.txt", "w", encoding = "UTF-8")

        for i in range(len(paymentsList)):
            file.write(paymentsList[i][0] + "," + paymentsList[i][1] + "," + paymentsList[i][2] + "," + paymentsList[i][3] + "," + paymentsList[i][4] + "," +paymentsList[i][5] + "\n")
        file.close()

        for widget in mainFrame.winfo_children():
            widget.destroy()

        Profile(root, mainFrame)
    else:
        Profile(root, mainFrame)

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

    imageDic = {"1": visaLogo, "2": mastercardLogo, "3": paypalLogo}
    paymentsList = CreateList()
    positiony = 320
    
    for i in range(len(paymentsList)-1,-1,-1):
        Label(mainFrame, image = imageDic[paymentsList[i][1]]).place(x = 50, y = positiony)
        Label(mainFrame, text = paymentsList[i][0], bg = "white").place(x = 120, y = positiony)
        Label(mainFrame, text = "****" + paymentsList[i][3], bg = "white").place(x = 200, y = positiony)
        Label(mainFrame, text = paymentsList[i][4] + "/" + paymentsList[i][5], bg = "white").place(x = 260, y = positiony)
        Button(mainFrame, text = "Borrar", command = lambda index = i: Erase(int(index), root, mainFrame)).place(x = 330, y = positiony)
        positiony = positiony + 40
        

    Button(mainFrame, text = "Agregar nuevo método de pago", command = lambda: payment_w.NewPaymenMethod(root, mainFrame)).place(x = 110, y = 530)
    Button(mainFrame, text = "Volver", command = lambda: dashboard_w.Dashboard(root, mainFrame)).place(x = 180, y = 570 )
