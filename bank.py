from tkinter import *
from tkinter import messagebox
import yaml
from yaml import Loader


class Bank():
    def withdraw(self):
        with open('config.yaml','r') as file:
            amount = float(entry_withdraw.get())
            data = yaml.load(file, Loader=Loader)
        with open('config.yaml','w') as file:
            data['balance'] -= amount
            yaml.dump(data,file)

    def balance(self):
        with open('config.yaml','r') as file:
            data = yaml.load(file, Loader=Loader)
            messagebox.showinfo(title="balance",message=f"your balance is {data['balance']}")

        
#----------------------------------------------------------------------------------#
window = Tk()

window.geometry("500x200")

Label(window,text="Enter amount to withdraw",font=('bold',14)).pack()
entry_withdraw = Entry(window)
entry_withdraw.pack()

button_withdraw = Button(window,text="withdraw",command=Bank().withdraw) 
button_withdraw.pack()

show_balance = Button(window,text="show balance",command=Bank().balance)
show_balance.pack()

window.resizable(False, False)
window.mainloop()
