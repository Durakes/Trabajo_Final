from tkinter import *
import windows_app.dashboard_window as dashboard_w

def Login(root, mainFrame):                    # Primera pantalla de login
    root.title("Login")
    mainFrame.config(width = "425", height = "852")
    mainFrame.pack()
    
    Label(mainFrame, text = "Logo").place(relx = 0.5, rely = 0.2)
    Label(mainFrame, text = "Username").place(x = 90, y = 200)
    Label(mainFrame, text = "Password").place(x = 90, y = 230)

    usernameEntry = Entry(mainFrame, width = 25, borderwidth = 2)
    usernameEntry.place(x = 190, y = 200)
    usernameEntry.pack_propagate(0)

    passwordEntry = Entry(mainFrame, width = 25, borderwidth = 2, show = "*")
    passwordEntry.place(x = 190, y = 230)
    passwordEntry.pack_propagate(0)
    
    Button(mainFrame, text = "Log in", width = 20, command = lambda: dashboard_w.Dashboard(root, mainFrame)).place(x = 130, y = 280)