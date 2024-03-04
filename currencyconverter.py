import os
from tkinter import Tk, ttk

import requests
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

root = Tk()
root.title("Currency Converter")

frm = ttk.Frame(root, padding=10)
frm.grid()


def validate_amount(new_text, current_val, action):
    """Makes sure amount entered is a valid float"""
    # if action == 0 aka delete then skip the validation
    if int(action) == 0:
        return True
    if not new_text:
        return True
    try:
        float(current_val + new_text)
        return True
    except ValueError:
        return False


vamt = root.register(validate_amount)


def convert():
    """Does the conversiona and inserts result in a label below"""
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

# Validate command args
# %S = the text string being inserted or deleted, if any
# %s = value of entry prior to editing
# %d = Type of action (1=insert, 0=delete, -1 for others)
amt = ttk.Entry(frm, width=10, validate="key", validatecommand=(vamt, "%S", "%s", "%d"))
amt.grid(row=1, column=5, pady=5)


ttk.Button(frm, text="Convert", command=convert).grid(column=6, row=1)


result_label = ttk.Label(frm, text="")
result_label.grid(row=2, column=0, columnspan=6)


root.mainloop()
