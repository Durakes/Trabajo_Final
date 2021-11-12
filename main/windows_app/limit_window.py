from tkinter import *
import os
import windows_app.profile_window as profile_w
from datetime import date

def Limit(root, mainFrame):
    
    root.title("Límite")
    global limitEntry
    limitEntry = StringVar()
    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "425", height = "852")
    mainFrame.pack()

    Label(mainFrame, text = "Establece tu límite mensual").place(x = 130, y = 70)
    Label(mainFrame, text = "Mes: " + str(date.today().month)).place(x = 120, y = 110)
    Label(mainFrame, text = "Ingresa tu monto límite: ").place(x = 80, y = 150)
    Entry(mainFrame, width = 25, borderwidth = 2, textvariable = limitEntry).place(x = 220, y = 150)

    Button(mainFrame, text = "Guardar", width = 10, command = lambda: SetLimit(root, mainFrame)).place(x = 150, y = 220)
    Button(mainFrame, text = "Volver", command = lambda: profile_w.Profile(root, mainFrame)).place(x = 170, y = 280)

def SetLimit(root, mainFrame):
    limit = limitEntry.get()

    my_path = os.getcwd()

    rfile = open(my_path + r"\main\fakedb\limits.txt", "r")
    limits_ = rfile.readlines()
    rfile.close()

    if len(limits_) != 0:
        lastLimit = limits_[-1]
        lastLimit = lastLimit.split(",")
        lastLimit[2] = lastLimit[2][:-1]
        if int(lastLimit[1]) == date.today().month and int(lastLimit[2]) == date.today().year:
            lastLimit[0] = limit
            del limits_[-1]
            limits_.append(",".join(lastLimit))
            wfile = open(my_path + r"\main\fakedb\limits.txt", "w", encoding = "UTF-8")
            for line in limits_:
                wfile.write(line + "\n")
            wfile.close()

        else:
            wfile = open(my_path + r"\main\fakedb\limits.txt", "a", encoding = "UTF-8")
            wfile.write(limit + "," + str(date.today().month) + "," + str(date.today().year) +"\n")
    else:
        wfile = open(my_path + r"\main\fakedb\limits.txt", "a", encoding = "UTF-8")
        wfile.write(limit + "," + str(date.today().month) + "," + str(date.today().year) +"\n")
    
    profile_w.Profile(root, mainFrame)