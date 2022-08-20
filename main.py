import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("SVR CAR RENTAL MEDIATION SERVICE")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.config(bg="yellow")

        GButton_842=tk.Button(root)
        GButton_842["bg"] = "#070303"
        ft = tkFont.Font(family='Times',size=10)
        GButton_842["font"] = ft
        GButton_842["fg"] = "#f11b1b"
        GButton_842["justify"] = "center"
        GButton_842["text"] = "CUSTOMER LOGIN"
        GButton_842.place(x=190,y=140,width=200,height=25)
        GButton_842["command"] = customer_login

        GButton_41=tk.Button(root)
        GButton_41["bg"] = "#0e0d0d"
        ft = tkFont.Font(family='Times',size=10)
        GButton_41["font"] = ft
        GButton_41["fg"] = "#ed1818"
        GButton_41["justify"] = "center"
        GButton_41["text"] = "EXISTING AGENT LOGIN"
        GButton_41.place(x=190,y=230,width=200,height=25)
        GButton_41["command"] = agent_login

        GButton_972=tk.Button(root)
        GButton_972["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=10)
        GButton_972["font"] = ft
        GButton_972["fg"] = "#ef1e1e"
        GButton_972["justify"] = "center"
        GButton_972["text"] = "NEW AGENT REGISTRATION"
        GButton_972.place(x=190,y=320,width=200,height=25)
        GButton_972["command"] = agent_registration

        GLabel_945=tk.Label(root)
        GLabel_945["bg"] = "#040404"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_945["font"] = ft
        GLabel_945["fg"] = "#e31717"
        GLabel_945["justify"] = "center"
        GLabel_945["text"] = "SVR CAR RENTAL MEDIATION SERVICE"
        GLabel_945.place(x=140,y=50,width=300,height=25)


def customer_login():
    import Customer_View
    Customer_View.root = tk.Toplevel(root)
    Customer_View.root.resizable(True,True)
    Customer_View.app_1 = Customer_View.App(Customer_View.root)
    Customer_View.root.config(bg="yellow")
    Customer_View.root.mainloop()


def agent_login():
    import Agent_Login
    Agent_Login.root = tk.Toplevel(root)
    Agent_Login.root.resizable(True,True)
    Agent_Login.app_2 = Agent_Login.App(Agent_Login.root)
    Agent_Login.root.config(bg="yellow")
    Agent_Login.root.mainloop()


def agent_registration():
    import Agent_Registration
    Agent_Registration.root = tk.Toplevel(root)
    Agent_Registration.root.resizable(True,True)
    Agent_Registration.app_3 = Agent_Registration.App(Agent_Registration.root)
    Agent_Registration.root.config(bg="yellow")
    Agent_Registration.root.mainloop()


root = tk.Tk()
app = App(root)
root.mainloop()
