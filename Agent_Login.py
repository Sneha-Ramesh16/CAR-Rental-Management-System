import tkinter as tk
import tkinter.font as tkFont
import mysql.connector
from tkinter import messagebox

class App:
    GLineEdit_897 = None
    GLineEdit_736 = None
    root = None

    def __init__(self, root):
        #setting title
        root.title("EXISTING AGENT LOGIN")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_780=tk.Label(root)
        GLabel_780["bg"] = "#171414"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_780["font"] = ft
        GLabel_780["fg"] = "#e01919"
        GLabel_780["justify"] = "center"
        GLabel_780["text"] = "Email ID"
        GLabel_780.place(x=50,y=90,width=70,height=25)

        GLabel_369=tk.Label(root)
        GLabel_369["bg"] = "#180404"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_369["font"] = ft
        GLabel_369["fg"] = "#de1919"
        GLabel_369["justify"] = "center"
        GLabel_369["text"] = "Password"
        GLabel_369.place(x=50,y=160,width=70,height=25)

        GButton_464=tk.Button(root)
        GButton_464["bg"] = "#1b1919"
        ft = tkFont.Font(family='Times',size=10)
        GButton_464["font"] = ft
        GButton_464["fg"] = "#e60f0f"
        GButton_464["justify"] = "center"
        GButton_464["text"] = "Submit"
        GButton_464.place(x=130,y=250,width=70,height=25)
        GButton_464["command"] = log_in

        App.GLineEdit_897=tk.Entry(root)
        App.GLineEdit_897["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        App.GLineEdit_897["font"] = ft
        App.GLineEdit_897["fg"] = "#333333"
        App.GLineEdit_897["justify"] = "center"
        App.GLineEdit_897["text"] = ""
        App.GLineEdit_897.place(x=190,y=90,width=200,height=25)

        App.GLineEdit_736=tk.Entry(root)
        App.GLineEdit_736["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        App.GLineEdit_736["font"] = ft
        App.GLineEdit_736["fg"] = "#333333"
        App.GLineEdit_736["justify"] = "center"
        App.GLineEdit_736["text"] = ""
        App.GLineEdit_736["show"] = "*"
        App.GLineEdit_736.place(x=190,y=160,width=200,height=25)

        GButton_829=tk.Button(root)
        GButton_829["bg"] = "#131212"
        ft = tkFont.Font(family='Times',size=10)
        GButton_829["font"] = ft
        GButton_829["fg"] = "#e41b1b"
        GButton_829["justify"] = "center"
        GButton_829["text"] = "Exit"
        GButton_829.place(x=340,y=250,width=70,height=25)
        GButton_829["command"] = lambda: root.destroy()

def log_in():

    conn = mysql.connector.connect(host="localhost",user="root",password="Rr2163?!",database="car_rentals")
    cur = conn.cursor()

    e_mailID = App.GLineEdit_897.get()
    pass_word = App.GLineEdit_736.get()

    cur.execute("SELECT agent_id,A_password from agents where agent_email = '{}' and A_password = '{}'".format(e_mailID,pass_word))
    c = cur.fetchall()
    if c:
        messagebox.showinfo("Success","Welcome to SVR")
        import Agent_View
        Agent_View.root = tk.Toplevel(App.root)
        Agent_View.root.resizable(True,True)
        Agent_View.app = Agent_View.App(Agent_View.root)
        Agent_View.root.config(bg="yellow")
        Agent_View.root.mainloop()

    else:
        messagebox.showinfo("Error","Invalid Login!")

    conn.commit()
    conn.close()
