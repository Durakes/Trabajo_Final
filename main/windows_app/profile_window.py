from tkinter import *
import windows_app.dashboard_window as dashboard_w
import windows_app.newPayment_window as payment_w
import windows_app.limit_window as limit_w
import helpers.readfiles as rfiles
from PIL import Image, ImageTk
from tkinter import messagebox as MessageBox

my_path = rfiles.Route()

#* Función para crear y dar formato a la lista de metodos de pago que se mostrarán en la ventana principal.
def CreateList():
    paymentsList = rfiles.GetPaymentsFile()
    for i in range (len(paymentsList)):
        paymentsList[i][5] = paymentsList[i][5][:-1]

    return paymentsList

#* Función para borrar un método de pago
def Erase(index, root, mainFrame):
    paymentsList = CreateList()

    answer = MessageBox.askyesno(message = "¿Desea continuar?")
    if answer == True:

        del paymentsList[index]
        file = open(my_path + r"\main\fakedb\payments.txt", "w", encoding = "UTF-8")

        for i in range(len(paymentsList)):
            file.write(",".join(paymentsList[i]) + "\n")
        file.close()

        for widget in mainFrame.winfo_children():
            widget.destroy()

        Profile(root, mainFrame)
    else:
        Profile(root, mainFrame)

#* Función para verificar que la cantidad de metodos de pago sean máximo 5.
def CheckPayments(root, mainFrame):
    numPayments = rfiles.GetPaymentsFile()

    if len(numPayments) >= 5:
        MessageBox.showwarning("Cuidado", "Ha alcanzado la máxima cantidad de metodos de pago")
    else:
        payment_w.NewPaymenMethod(root, mainFrame)

#* Estructura de la ventana de Perfil.
def Profile(root, mainFrame):

    root.title("Perfil")

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "425", height = "852")
    #? mainFrame.config(width = "425", height = "700")
    mainFrame.pack()

    global visaLogo 
    visaLogo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\Visa.png").resize((50,25), Image.ANTIALIAS))
    global paypalLogo 
    paypalLogo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\Paypal.png").resize((52,20), Image.ANTIALIAS))
    global mastercardLogo
    mastercardLogo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\Mastercard.png").resize((50,28), Image.ANTIALIAS))
    global profileLogo
    profileLogo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\Profile.png").resize((150,150), Image.ANTIALIAS))

    Label(mainFrame, text = "Perfil").place(x = 250, y = 50)
    Label(mainFrame, image = profileLogo).place(x = 30, y = 30)
    Label(mainFrame, text = "Nombre: Eduardo Gonzalo").place(x = 200, y = 100)
    Label(mainFrame, text = "Apellidos: Bautista Arrilucea").place(x = 200, y = 130)
    Label(mainFrame, text = "Correo: eduardo.bautistaa@usil.pe").place(x = 200, y = 160)

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
        
    Button(mainFrame, text = "Agregar nuevo método de pago", command = lambda: CheckPayments(root, mainFrame)).place(x = 110, y = 530)
    Button(mainFrame, text = "Agregar monto límite", command = lambda: limit_w.Limit(root, mainFrame)).place(x = 140, y = 580)
    Button(mainFrame, text = "Volver", command = lambda: dashboard_w.Dashboard(root, mainFrame)).place(x = 180, y = 630)