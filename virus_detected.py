# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = Tk()
root.geometry("200x200")


def msg():
	#messagebox.showwarning("Alert", "Stop! Virus Found.")
    #messagebox.showinfo("Info", "Please run a full system scan immediately.")
    #messagebox.showerror("Error", "Virus Detected! Please take necessary actions.")
    messagebox.askquestion("Virus Detected", "A virus has been detected on your system. Do you want to run a full system scan now?")


button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)


root.mainloop()