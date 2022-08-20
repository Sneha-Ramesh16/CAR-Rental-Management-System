import tkinter as tk
import tkinter.font as tkFont
import mysql.connector
from tkinter import messagebox


class App:
    GLineEdit_99 = None

    def __init__(self, root):
        # setting title
        root.title("Delete")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_743 = tk.Label(root)
        GLabel_743["bg"] = "#191818"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_743["font"] = ft
        GLabel_743["fg"] = "#cc4040"
        GLabel_743["justify"] = "center"
        GLabel_743["text"] = "Car Number "
        GLabel_743.place(x=80, y=110, width=139, height=37)

        App.GLineEdit_99 = tk.Entry(root)
        App.GLineEdit_99["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        App.GLineEdit_99["font"] = ft
        App.GLineEdit_99["fg"] = "#333333"
        App.GLineEdit_99["justify"] = "center"
        App.GLineEdit_99["text"] = "Entry"
        App.GLineEdit_99.place(x=270, y=110, width=271, height=36)

        GButton_972 = tk.Button(root)
        GButton_972["bg"] = "#111112"
        ft = tkFont.Font(family='Times', size=10)
        GButton_972["font"] = ft
        GButton_972["fg"] = "#cc0000"
        GButton_972["justify"] = "center"
        GButton_972["text"] = "Delete"
        GButton_972.place(x=250, y=220, width=94, height=34)
        GButton_972["command"] = delete


def delete():
    conn = mysql.connector.connect(host="localhost", user="root", password="Rr2163?!", database="car_rentals")
    cur = conn.cursor()

    Car_no = App.GLineEdit_99.get()

    cur.execute("delete from car_details where car_no = '{}'".format(Car_no))

    try:
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Car Detail Removed Successfully!")

    except:
        messagebox.showinfo("Error", "Couldn't delete car detail!")
