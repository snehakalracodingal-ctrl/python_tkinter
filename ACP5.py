from tkinter import *


window = Tk()
window.title("Password Strength Checker")
window.geometry("400x300")
window.configure(bg="lightblue")


def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password", fg="black")

    elif length < 6:
        result_label.config(text="Weak Password 🔴", fg="red")

    elif length >= 6 and length < 10:
        result_label.config(text="Medium Password 🟡", fg="orange")

    else:
        result_label.config(text="Strong Password 🟢", fg="green")



def toggle_password():
    if show_var.get() == 1:
        entry.config(show="")     
    else:
        entry.config(show="*")    



label = Label(window, text="Enter Password:", bg="lightblue", font=("Arial", 12))
label.pack(pady=10)


entry = Entry(window, show="*", width=25)
entry.pack(pady=5)


show_var = IntVar()
show_check = Checkbutton(window, text="Show Password",
                         variable=show_var,
                         command=toggle_password,
                         bg="lightblue")
show_check.pack()


button = Button(window, text="Check Strength", command=check_strength)
button.pack(pady=10)


result_label = Label(window, text="", bg="lightblue", font=("Arial", 12))
result_label.pack(pady=10)


window.mainloop()