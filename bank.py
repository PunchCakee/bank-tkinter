import string
from tkinter import *
from tkinter import messagebox
import yaml
from yaml import Loader


#for testing only remove on use of public
#or set this to False
devmode = False

class Bank:

    def withdraw(self):
        try:
            with open('config.yaml','r') as file:
                amount = float(entry.get())
                data = yaml.load(file, Loader=Loader)
            with open('config.yaml','w') as file:
                data['balance'] -= amount
                messagebox.showinfo(title="withdraw", message=f"{amount} has been withdrawn, current balance is {data['balance']}")
                yaml.dump(data,file)

        except ValueError as err:
            messagebox.showwarning(title="warning",message="only numbers are allowed, it looks like you tried to enter a string or you left it empty.")
            print(err)

    def balance(self):
        with open('config.yaml','r') as file:
            data = yaml.load(file, Loader=Loader)
            messagebox.showinfo(title="balance",message=f"your balance is {data['balance']}")

    def add(self):
        with open('config.yaml','r') as file:
            amount = float(entry.get())
            data = yaml.load(file, Loader=Loader)
        with open('config.yaml','w') as file:
            data['balance'] += amount
            messagebox.showinfo(title="withdraw", message=f"{amount} has been added, current balance is {data['balance']}")
            yaml.dump(data,file)


#----------------------------------------------------------------------------------#
window = Tk()

window.geometry("500x200")

Label(window,text="Enter amount to withdraw",font=('bold',14)).pack()
entry = Entry(window)
entry.pack()

button_withdraw = Button(window,text="withdraw",command=Bank().withdraw) 
button_withdraw.pack()

show_balance = Button(window,text="show balance",command=Bank().balance)
show_balance.pack()

if devmode == True:
    devmode_button = Button(window,text="devmode add",command=Bank().add)
    devmode_button.pack()

window.resizable(False, False)
window.mainloop()
