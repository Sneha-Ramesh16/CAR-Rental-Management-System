import tkinter as tk
import tkinter.font as tkFont
import mysql.connector
from tkinter import *

class App:

    GListBox_400 = None

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

        GButton_949=tk.Button(root)
        GButton_949["bg"] = "#210d0d"
        ft = tkFont.Font(family='Times',size=10)
        GButton_949["font"] = ft
        GButton_949["fg"] = "#d71111"
        GButton_949["justify"] = "center"
        GButton_949["text"] = "View"
        GButton_949.place(x=250,y=30,width=70,height=25)
        GButton_949["command"] = View

        App.GListBox_400=tk.Listbox(root)
        App.GListBox_400["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        App.GListBox_400["font"] = ft
        App.GListBox_400["fg"] = "#333333"
        App.GListBox_400["justify"] = "center"
        App.GListBox_400.place(x=20,y=80,width=558,height=403)


def View():

    conn = mysql.connector.connect(host="localhost", user="root", password="Rr2163?!", database="car_rentals")
    cur = conn.cursor()

    cur.execute("select * from car_details")
    c = cur.fetchall()

    App.GListBox_400.insert(END," Car No      Car Type    Agent ID    RentalPrice    Tariff    Car Name")
    App.GListBox_400.insert(END,"-----------------------------------------------------------------------")


    for i in c:
        App.GListBox_400.insert(END,str(i[0]) + "    " + str([i[1]]) + "     " + str(i[2]) + "     " + str(i[3]) + "     " + str(i[4]) + "     " + str(i[5]))

    conn.commit()
    conn.close()
