from tkinter import *
from tkinter import ttk

money = 0


def freeMoney():
    global money
    money += 1
    moneyLabel["text"] = f'{money}$'


coolWindow = Tk()
coolWindow.title("Cool window")
coolWindow.geometry("300x300")
coolLabel = Label(text="cool money 😎😎😎", font=("Arial", 13))
moneyLabel = Label(text=money, font=("Arial", 20), fg='green')
coolLabel.pack()
moneyLabel.pack()
coolButton = ttk.Button(text="Cool button", command=freeMoney)
coolButton.pack()
coolWindow.minsize(200, 200)
coolWindow.maxsize(600, 600)
coolWindow.mainloop()
