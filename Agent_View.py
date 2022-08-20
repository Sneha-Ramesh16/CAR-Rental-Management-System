import tkinter as tk
import tkinter.font as tkFont



class App:

    root = None
    def __init__(self, root):
        #setting title
        root.title("Welcome Agent")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_370=tk.Button(root)
        GButton_370["bg"] = "#1b0e0e"
        ft = tkFont.Font(family='Times',size=10)
        GButton_370["font"] = ft
        GButton_370["fg"] = "#f32626"
        GButton_370["justify"] = "center"
        GButton_370["text"] = "View"
        GButton_370.place(x=270,y=170,width=88,height=54)
        GButton_370["command"] = open_view

        GButton_267=tk.Button(root)
        GButton_267["bg"] = "#150c0c"
        ft = tkFont.Font(family='Times',size=10)
        GButton_267["font"] = ft
        GButton_267["fg"] = "#f91f1f"
        GButton_267["justify"] = "center"
        GButton_267["text"] = "Update"
        GButton_267.place(x=270,y=260,width=86,height=50)
        GButton_267["command"] = open_update

        GButton_99=tk.Button(root)
        GButton_99["bg"] = "#1b0a0a"
        ft = tkFont.Font(family='Times',size=10)
        GButton_99["font"] = ft
        GButton_99["fg"] = "#f91b1b"
        GButton_99["justify"] = "center"
        GButton_99["text"] = "Delete"
        GButton_99.place(x=270,y=350,width=86,height=51)
        GButton_99["command"] = open_delete

        GButton_555=tk.Button(root)
        GButton_555["bg"] = "#150909"
        ft = tkFont.Font(family='Times',size=10)
        GButton_555["font"] = ft
        GButton_555["fg"] = "#d31616"
        GButton_555["justify"] = "center"
        GButton_555["text"] = "Add"
        GButton_555.place(x=270,y=110,width=84,height=37)
        GButton_555["command"] = open_add

def open_add():
    import Add
    Add.root = tk.Toplevel(App.root)
    Add.app = Add.App(Add.root)
    Add.root.config(bg="yellow")
    Add.root.mainloop()

def open_delete():
    import Delete
    Delete.root = tk.Toplevel(App.root)
    Delete.app = Delete.App(Delete.root)
    Delete.root.config(bg="yellow")
    Delete.root.mainloop()

def open_update():
    import Update
    Update.root = tk.Toplevel(App.root)
    Update.app = Update.App(Update.root)
    Update.root.config(bg="yellow")
    Update.root.mainloop()

def open_view():
    import View
    View.root = tk.Toplevel(App.root)
    View.app = View.App(View.root)
    View.root.config(bg="yellow")
    View.root.mainloop()
