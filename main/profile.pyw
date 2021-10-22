from tkinter import *

root = Tk()
root.title("Profile")
root.resizable(0,0)

mainFrame = Frame()
mainFrame.config(width = "425", height = "852")
mainFrame.pack()

Label(mainFrame, text = "Perfil").place(x = 190, y = 50)
Label(mainFrame, text = "Nombre: ").place(x = 200, y = 100)
Label(mainFrame, text = "Apellidos: ").place(x = 200, y = 130)
Label(mainFrame, text = "Correo: ").place(x = 200, y = 160)

Label(mainFrame, text = "Cuentas asociadas:").place(x = 70, y = 250)

Label(mainFrame, text = "PAYPAL", bg = "white").place(x = 50, y = 320)
Label(mainFrame, text = "**** 1234", bg = "white").place(x = 110, y = 320)
Label(mainFrame, text = "01/22", bg = "white").place(x = 170, y = 320)
Button(mainFrame, text = "Borrar").place(x = 300, y = 320)

Label(mainFrame, text = "Visa", bg = "white").place(x = 50, y = 360)
Label(mainFrame, text = "**** 1234", bg = "white").place(x = 110, y = 360)
Label(mainFrame, text = "01/22", bg = "white").place(x = 170, y = 360)
Button(mainFrame, text = "Borrar").place(x = 300, y = 360)


Label(mainFrame, text = "Master", bg = "white").place(x = 50, y = 400)
Label(mainFrame, text = "**** 1234", bg = "white").place(x = 110, y = 400)
Label(mainFrame, text = "01/22", bg = "white").place(x = 170, y = 400)
Button(mainFrame, text = "Borrar").place(x = 300, y = 400)

Button(mainFrame, text = "Agregar nuevo método de pago").place(x = 110, y = 450)
Button(mainFrame, text = "Volver").place(x = 180, y = 500 )

root.mainloop()