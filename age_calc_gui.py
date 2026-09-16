import tkinter as tk
from datetime import date
from tkinter import messagebox


def calculate_age():
    name = name_value.get().strip()

    if not name:
        messagebox.showwarning("Missing Name", "Please enter your name.")
        return

    try:
        birth_date = date(
            int(year_value.get()),
            int(month_value.get()),
            int(day_value.get())
        )
    except ValueError:
        messagebox.showerror(
            "Invalid Date",
            "Please enter a valid birth date."
        )
        return

    today = date.today()

    if birth_date > today:
        messagebox.showerror(
            "Invalid Date",
            "Birth date cannot be in the future."
        )
        return

    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    result_label.config(text=f"{name}'s age is {age}.")


# Create the main window
root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
root.title("Age Calculator")

# Name
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)

name_value = tk.StringVar()
name_entry = tk.Entry(root, textvariable=name_value)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Year
tk.Label(root, text="Year:").grid(row=1, column=0, padx=10, pady=10)

year_value = tk.StringVar()
year_entry = tk.Entry(root, textvariable=year_value)
year_entry.grid(row=1, column=1, padx=10, pady=10)

# Month
tk.Label(root, text="Month:").grid(row=2, column=0, padx=10, pady=10)

month_value = tk.StringVar()
month_entry = tk.Entry(root, textvariable=month_value)
month_entry.grid(row=2, column=1, padx=10, pady=10)

# Day
tk.Label(root, text="Day:").grid(row=3, column=0, padx=10, pady=10)

day_value = tk.StringVar()
day_entry = tk.Entry(root, textvariable=day_value)
day_entry.grid(row=3, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(
    root,
    text="Calculate Age",
    command=calculate_age
)
calculate_button.grid(row=4, column=1, pady=10)

# Result
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=1, pady=15)

# Start the application
root.mainloop()