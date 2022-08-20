import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

import mysql.connector

global name, phone_no, email, agentTable, root


class App:
    GLineEdit_528 = None
    GLineEdit_239 = None
    GLineEdit_864 = None
    GLineEdit_972 = None
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_951=tk.Label(root)
        GLabel_951["bg"] = "#250505"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_951["font"] = ft
        GLabel_951["fg"] = "#f12121"
        GLabel_951["justify"] = "center"
        GLabel_951["text"] = "Name"
        GLabel_951.place(x=60,y=90,width=70,height=25)

        GLabel_512=tk.Label(root)
        GLabel_512["bg"] = "#1e0d0d"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_512["font"] = ft
        GLabel_512["fg"] = "#e32424"
        GLabel_512["justify"] = "center"
        GLabel_512["text"] = "Email ID"
        GLabel_512.place(x=60,y=150,width=70,height=25)

        GLabel_696=tk.Label(root)
        GLabel_696["bg"] = "#170606"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_696["font"] = ft
        GLabel_696["fg"] = "#ec2e2e"
        GLabel_696["justify"] = "center"
        GLabel_696["text"] = "Phone"
        GLabel_696.place(x=60,y=210,width=70,height=25)

        GLabel_56=tk.Label(root)
        GLabel_56["bg"] = "#230d0d"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_56["font"] = ft
        GLabel_56["fg"] = "#f63434"
        GLabel_56["justify"] = "center"
        GLabel_56["text"] = "Desired Password"
        GLabel_56.place(x=40,y=260,width=108,height=42)

        App.GLineEdit_528=tk.Entry(root)
        App.GLineEdit_528["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        App.GLineEdit_528["font"] = ft
        App.GLineEdit_528["fg"] = "#333333"
        App.GLineEdit_528["justify"] = "center"
        App.GLineEdit_528["text"] = ""
        App.GLineEdit_528.place(x=210,y=90,width=200,height=25)

        App.GLineEdit_239=tk.Entry(root)
        App.GLineEdit_239["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        App.GLineEdit_239["font"] = ft
        App.GLineEdit_239["fg"] = "#333333"
        App.GLineEdit_239["justify"] = "center"
        App.GLineEdit_239["text"] = ""
        App.GLineEdit_239.place(x=210,y=150,width=200,height=25)

        App.GLineEdit_864=tk.Entry(root)
        App.GLineEdit_864["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        App.GLineEdit_864["font"] = ft
        App.GLineEdit_864["fg"] = "#333333"
        App.GLineEdit_864["justify"] = "center"
        App.GLineEdit_864["text"] = ""
        App.GLineEdit_864.place(x=210,y=210,width=200,height=25)

        App.GLineEdit_972=tk.Entry(root)
        App.GLineEdit_972["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        App.GLineEdit_972["font"] = ft
        App.GLineEdit_972["fg"] = "#333333"
        App.GLineEdit_972["justify"] = "center"
        App.GLineEdit_972["text"] = ""
        App.GLineEdit_972.place(x=210,y=270,width=200,height=25)

        GButton_8=tk.Button(root)
        GButton_8["bg"] = "#210404"
        ft = tkFont.Font(family='Times',size=10)
        GButton_8["font"] = ft
        GButton_8["fg"] = "#e61d1d"
        GButton_8["justify"] = "center"
        GButton_8["text"] = "Register"
        GButton_8.place(x=180,y=380,width=70,height=25)
        GButton_8["command"] = add_agent

        GButton_833=tk.Button(root)
        GButton_833["bg"] = "#120a0a"
        ft = tkFont.Font(family='Times',size=10)
        GButton_833["font"] = ft
        GButton_833["fg"] = "#d21717"
        GButton_833["justify"] = "center"
        GButton_833["text"] = "Exit"
        GButton_833.place(x=320,y=380,width=70,height=25)
        GButton_833["command"] = lambda: root.destroy()


def add_agent():
    conn = mysql.connector.connect(host="localhost", user="root", password="Rr2163?!", database="car_rentals")
    conn.autocommit = True

    cur = conn.cursor()

    global name, phone_no, email, agentTable
    name = App.GLineEdit_528.get()
    phone_no = App.GLineEdit_864.get()
    email = App.GLineEdit_239.get()

    ID = "0_" + email
    password = App.GLineEdit_972.get()

    cur.execute( "insert into agents values ('{}','{}','{}','{}','{}')".format(ID, name, phone_no, email,password))
    try:
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "You are added Successfully!")

    except:
        messagebox.showinfo("Error", "Couldn't add data to database!")

