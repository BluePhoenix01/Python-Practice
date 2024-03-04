import os
from tkinter import Tk, ttk

import requests
from dotenv import load_dotenv

load_dotenv()

root = Tk()
root.title("Currency Converter")

frm = ttk.Frame(root, padding=10)
frm.grid()


def validate_amount(text, current_text, action):
    if int(action) == 0:
        return True
    if not text:
        return True
    try:
        print(current_text)
        print(text)
        float(current_text + text)
        return True
    except ValueError:
        return False


vamt = root.register(validate_amount)


def convert():
    from_currency = from_curr.get()
    to_currency = to_curr.get()
    amount = amt.get()

    host = os.environ.get("HOST")
    key = os.environ.get("KEY")

    url = f"https://{host}/exchange"

    querystring = {
        "from": from_currency,
        "to": to_currency,
    }

    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": host,
    }

    response = requests.get(url, headers=headers, params=querystring)

    result_label.config(
        text=f"{amount} {from_currency} To {to_currency} = {float(response.text) * float(amount)}"
    )


ttk.Label(frm, text="Currency Converter").grid(column=0, columnspan=5, row=0)

ttk.Label(frm, text="From").grid(column=0, row=1)
from_curr = ttk.Entry(frm, width=10)
from_curr.grid(row=1, column=1, pady=5)

ttk.Label(frm, text="To").grid(column=2, row=1)
to_curr = ttk.Entry(frm, width=10)
to_curr.grid(row=1, column=3, pady=5)

ttk.Label(frm, text="Amount").grid(column=4, row=1)
amt = ttk.Entry(frm, width=10, validate="key", validatecommand=(vamt, "%S", "%s", "%d"))
amt.grid(row=1, column=5, pady=5)


ttk.Button(frm, text="Convert", command=convert).grid(column=6, row=1)

result_label = ttk.Label(frm, text="")
result_label.grid(row=2, column=0, columnspan=6)

root.mainloop()
