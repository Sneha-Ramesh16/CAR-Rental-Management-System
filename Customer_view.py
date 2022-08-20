import tkinter as tk
import tkinter.font as tkFont
import mysql.connector
from tkinter import *
from tkinter import messagebox

class App:
    GLineEdit_525 = None
    GLineEdit_438 = None
    GLineEdit_944 = None
    GListBox_320 = None

    def __init__(self, root):
        #setting title
        root.title("CUSTOMER VIEW")
        #setting window size
        width=100
        height=40
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_784=tk.Label(root)
        GLabel_784["bg"] = "#100f0f"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_784["font"] = ft
        GLabel_784["fg"] = "#fa1a1a"
        GLabel_784["justify"] = "center"
        GLabel_784["text"] = "Name"
        GLabel_784.place(x=40,y=50,width=70,height=25)

        GLabel_507=tk.Label(root)
        GLabel_507["bg"] = "#150707"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_507["font"] = ft
        GLabel_507["fg"] = "#e21c1c"
        GLabel_507["justify"] = "center"
        GLabel_507["text"] = "Phone Number"
        GLabel_507.place(x=40,y=100,width=70,height=25)

        App.GLineEdit_525=tk.Entry(root)
        App.GLineEdit_525["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        App.GLineEdit_525["font"] = ft
        App.GLineEdit_525["fg"] = "#333333"
        App.GLineEdit_525["justify"] = "center"
        App.GLineEdit_525["text"] = ""
        App.GLineEdit_525.place(x=170,y=50,width=200,height=25)

        App.GLineEdit_438=tk.Entry(root)
        App.GLineEdit_438["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        App.GLineEdit_438["font"] = ft
        App.GLineEdit_438["fg"] = "#333333"
        App.GLineEdit_438["justify"] = "center"
        App.GLineEdit_438["text"] = ""
        App.GLineEdit_438.place(x=170,y=100,width=200,height=25)

        App.GListBox_320=tk.Listbox(root)
        App.GListBox_320["bg"] = "#f8f3f3"
        App.GListBox_320["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        App.GListBox_320["font"] = ft
        App.GListBox_320["fg"] = "#333333"
        App.GListBox_320["justify"] = "center"
        App.GListBox_320.place(x=20,y=200,width=602,height=336)
        App.GListBox_320["exportselection"] = "0"
        App.GListBox_320["selectmode"] = "browse"
        App.GListBox_320["setgrid"] = "True"

        GLabel_32=tk.Label(root)
        GLabel_32["bg"] = "#232020"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_32["font"] = ft
        GLabel_32["fg"] = "#de1414"
        GLabel_32["justify"] = "center"
        GLabel_32["text"] = "Maximum Expected Price"
        GLabel_32.place(x=10,y=150,width=142,height=30)

        App.GLineEdit_944=tk.Entry(root)
        App.GLineEdit_944["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        App.GLineEdit_944["font"] = ft
        App.GLineEdit_944["fg"] = "#333333"
        App.GLineEdit_944["justify"] = "center"
        App.GLineEdit_944["text"] = ""
        App.GLineEdit_944.place(x=170,y=150,width=200,height=25)

        GButton_940=tk.Button(root)
        GButton_940["bg"] = "#1b1717"
        ft = tkFont.Font(family='Times',size=10)
        GButton_940["font"] = ft
        GButton_940["fg"] = "#ed1b1b"
        GButton_940["justify"] = "center"
        GButton_940["text"] = "Submit"
        GButton_940.place(x=490,y=60,width=70,height=25)
        GButton_940["command"] = submit

        GButton_417=tk.Button(root)
        GButton_417["bg"] = "#242121"
        ft = tkFont.Font(family='Times',size=10)
        GButton_417["font"] = ft
        GButton_417["fg"] = "#e71e1e"
        GButton_417["justify"] = "center"
        GButton_417["text"] = "Exit"
        GButton_417.place(x=490,y=120,width=70,height=25)
        GButton_417["command"] = lambda: root.destroy()

def submit():
    conn = mysql.connector.connect(host="localhost", user="root", password="Rr2163?!", database="car_rentals")
    cur_1 = conn.cursor()
    cur_2 = conn.cursor()

    name = App.GLineEdit_525.get()
    phone_no = App.GLineEdit_438.get()
    max_price = App.GLineEdit_944.get()

    cur_2.execute("insert into customers values('{}','{}','{}')".format(name,phone_no,max_price))


    cur_1.execute("select C.car_no, C.car_type,C.rental_price,C.tariff,C.car_name,A.agent_name,A.agent_phone_no,A.agent_email from car_details C natural join agents A where C.rental_price + C.tariff <= '{}'".format(max_price))
    m = cur_1.fetchall()

    App.GListBox_320.insert(END,"        Car No     Car Type    RentalPrice   Tariff   Car Name   AgentName   AgentPhoneNum   AgentEmail ")
    App.GListBox_320.insert(END,"-----------------------------------------------------------------------")
    for i in m:
        App.GListBox_320.insert(END,str(i[0]) + "    " + str([i[1]]) + "     " + str(i[2]) + "     " + str(i[3]) + "     " + str(i[4]) + "     " + str(i[5]) + "     " + str(i[6]) + "     " + str(i[7]))

    if cur_1.rowcount == 0:
        messagebox.showinfo("Sorry","No cars exist within your budget!")

    conn.commit()
    conn.close()
