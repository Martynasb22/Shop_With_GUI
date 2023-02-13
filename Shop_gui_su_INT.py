import tkinter as tk
from tkinter import ttk

def calculate_change(*args):
    cost = float(price_entry.get())
    amount_received = float(amount_received_entry.get())

    if amount_received < cost:
        change_label.config(text="Klaida: Gauta suma yra mažesnė už kainą.")
    else:
        change = amount_received - cost

        denominations = [1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

        change_breakdown = {}

        for denomination in denominations:
            if change >= denomination:
                number_of_denomination = int(change // denomination)
                change = change - number_of_denomination * denomination
                change_breakdown[denomination] = number_of_denomination

        change_str = "Išmokėtos sumos analizė:\n"
        for denomination, number in change_breakdown.items():
            change_str += f"{number} x {denomination}\n"
        change_label.config(text=change_str)

root = tk.Tk()
root.title("Išmokėtos sumos analizė")
root.geometry("300x200")

price_label = ttk.Label(root, text="Įveskite prekės kainą:")
price_label.grid(row=0, column=0)

price_entry = ttk.Entry(root)
price_entry.grid(row=0, column=1)
price_entry.focus()
price_entry.bind("<Return>", calculate_change)

amount_received_label = ttk.Label(root, text="Įveskite gautą sumą:")
amount_received_label.grid(row=1, column=0)

amount_received_entry = ttk.Entry(root)
amount_received_entry.grid(row=1, column=1)
amount_received_entry.bind("<Return>", calculate_change)

calculate_button = ttk.Button(root, text="Skaičiuoti", command=calculate_change)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

change_label = ttk.Label(root, text="")
change_label.grid(row=3, column=0, columnspan=2)

root.mainloop()