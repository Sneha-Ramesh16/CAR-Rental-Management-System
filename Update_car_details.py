import tkinter as tk
import tkinter.font as tkFont
import mysql.connector
from tkinter import messagebox


class App:
    
    GLineEdit_611 = None
    GLineEdit_51 = None
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_925 = tk.Button(root)
        GButton_925["bg"] = "#1e0f0f"
        ft = tkFont.Font(family='Times', size=10)
        GButton_925["font"] = ft
        GButton_925["fg"] = "#db2929"
        GButton_925["justify"] = "center"
        GButton_925["text"] = "Car Number"
        GButton_925.place(x=30, y=70, width=70, height=25)
        GButton_925["command"] = update_car_number

        GButton_195 = tk.Button(root)
        GButton_195["bg"] = "#0c0202"
        ft = tkFont.Font(family='Times', size=10)
        GButton_195["font"] = ft
        GButton_195["fg"] = "#d21e1e"
        GButton_195["justify"] = "center"
        GButton_195["text"] = "Car Type"
        GButton_195.place(x=140, y=70, width=70, height=25)
        GButton_195["command"] = update_car_type

        GButton_903 = tk.Button(root)
        GButton_903["bg"] = "#1a1414"
        ft = tkFont.Font(family='Times', size=10)
        GButton_903["font"] = ft
        GButton_903["fg"] = "#ef2d2d"
        GButton_903["justify"] = "center"
        GButton_903["text"] = "Rental Price"
        GButton_903.place(x=250, y=70, width=70, height=25)
        GButton_903["command"] = update_car_price

        GButton_267 = tk.Button(root)
        GButton_267["bg"] = "#201414"
        ft = tkFont.Font(family='Times', size=10)
        GButton_267["font"] = ft
        GButton_267["fg"] = "#dc2525"
        GButton_267["justify"] = "center"
        GButton_267["text"] = "Tariff"
        GButton_267.place(x=360, y=70, width=70, height=25)
        GButton_267["command"] = update_car_tariff

        GButton_915 = tk.Button(root)
        GButton_915["bg"] = "#291414"
        ft = tkFont.Font(family='Times', size=10)
        GButton_915["font"] = ft
        GButton_915["fg"] = "#e22222"
        GButton_915["justify"] = "center"
        GButton_915["text"] = "Car Name"
        GButton_915.place(x=470, y=70, width=70, height=25)
        GButton_915["command"] = update_car_name

        GLabel_12 = tk.Label(root)
        GLabel_12["bg"] = "#1d1414"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_12["font"] = ft
        GLabel_12["fg"] = "#de2626"
        GLabel_12["justify"] = "center"
        GLabel_12["text"] = "Enter Car Number"
        GLabel_12.place(x=30, y=190, width=112, height=31)

        GLabel_567 = tk.Label(root)
        GLabel_567["bg"] = "#1a0f0f"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_567["font"] = ft
        GLabel_567["fg"] = "#e42020"
        GLabel_567["justify"] = "center"
        GLabel_567["text"] = "Enter New Value"
        GLabel_567.place(x=40, y=270, width=92, height=30)

        App.GLineEdit_611 = tk.Entry(root)
        App.GLineEdit_611["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        App.GLineEdit_611["font"] = ft
        App.GLineEdit_611["fg"] = "#333333"
        App.GLineEdit_611["justify"] = "center"
        App.GLineEdit_611["text"] = ""
        App.GLineEdit_611.place(x=160, y=190, width=200, height=25)

        App.GLineEdit_51 = tk.Entry(root)
        App.GLineEdit_51["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        App.GLineEdit_51["font"] = ft
        App.GLineEdit_51["fg"] = "#333333"
        App.GLineEdit_51["justify"] = "center"
        App.GLineEdit_51["text"] = ""
        App.GLineEdit_51.place(x=160, y=270, width=200, height=25)


def update_car_number():


        conn = mysql.connector.connect(host="localhost", user="root", password="Rr2163?!", database="car_rentals")
        cur = conn.cursor()

        new_car_no = App.GLineEdit_51.get()
        old_car_no = App.GLineEdit_611.get()

        cur.execute("update car_details set car_no = '{}' where car_no = '{}'".format(new_car_no,old_car_no))
        try:
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Updated Car Number Successfully!")
        except:
            messagebox.showinfo("Error","Couldn't Update Car Number!")



def update_car_type():

        conn = mysql.connector.connect(host="localhost", user="root", password="Rr2163?!", database="car_rentals")
        cur = conn.cursor()

        new_car_type = App.GLineEdit_51.get()
        old_car_no = App.GLineEdit_611.get()

        cur.execute("update car_details set car_type = '{}' where car_no = '{}'".format(new_car_type, old_car_no))
        try:
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Updated Car Type Successfully!")
        except:
            messagebox.showinfo("Error", "Couldn't Update Car Type!")



def update_car_price():


        conn = mysql.connector.connect(host="localhost", user="root", password="Rr2163?!", database="car_rentals")
        cur = conn.cursor()

        new_price = App.GLineEdit_51.get()
        old_car_no = App.GLineEdit_611.get()

        cur.execute("update car_details set rental_price = '{}' where car_no = '{}'".format(new_price, old_car_no))
        try:
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Updated Car Price Successfully!")
        except:
            messagebox.showinfo("Error", "Couldn't Update Car Price!")



def update_car_tariff():


        conn = mysql.connector.connect(host="localhost", user="root", password="Rr2163?!", database="car_rentals")
        cur = conn.cursor()

        new_tariff = App.GLineEdit_51.get()
        old_car_no = App.GLineEdit_611.get()

        cur.execute("update car_details set tariff = '{}' where car_no = '{}'".format(new_tariff, old_car_no))
        try:
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Updated Car Tariff Successfully!")
        except:
            messagebox.showinfo("Error", "Couldn't Update Car Tariff!")



def update_car_name():


        conn = mysql.connector.connect(host="localhost", user="root", password="Rr2163?!", database="car_rentals")
        cur = conn.cursor()

        new_car_name = App.GLineEdit_51.get()
        old_car_no = App.GLineEdit_611.get()

        cur.execute("update car_details set car_name = '{}' where car_no = '{}'".format(new_car_name, old_car_no))
        try:
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Updated Car Name Successfully!")
        except:
            messagebox.showinfo("Error", "Couldn't Update Name Number!")

