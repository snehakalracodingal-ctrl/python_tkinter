import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())

        birth_date = date(year, month, day)
        today = date.today()

        if birth_date > today:
            messagebox.showerror("Error", "Birth date cannot be in the future!")
            return

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Your Age is: {age} years")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values!")

root = tk.Tk()
root.title("Age Calculator App")
root.geometry("350x250")

tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold"))

# Day
tk.Label(root, text="Day").pack()
entry_day = tk.Entry(root)
entry_day.pack()

# Month
tk.Label(root, text="Month").pack()
entry_month = tk.Entry(root)
entry_month.pack()

# Year
tk.Label(root, text="Year").pack()
entry_year = tk.Entry(root)
entry_year.pack()

# Button
tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()