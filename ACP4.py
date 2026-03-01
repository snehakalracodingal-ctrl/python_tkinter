from tkinter import *

# Create window
window = Tk()
window.title("Interest Calculator")
window.geometry("400x350")

# Labels
Label(window, text="Principal Amount").pack()
principal_entry = Entry(window)
principal_entry.pack()

Label(window, text="Rate of Interest (%)").pack()
rate_entry = Entry(window)
rate_entry.pack()

Label(window, text="Time (Years)").pack()
time_entry = Entry(window)
time_entry.pack()

# Function to calculate interest
def calculate():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    
    # Simple Interest
    simple_interest = (p * r * t) / 100
    
    # Compound Interest
    compound_interest = p * (1 + r/100) ** t - p
    
    result_label.config(
        text=f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}"
    )

# Button
Button(window, text="Calculate", command=calculate).pack(pady=10)

# Result Label
result_label = Label(window, text="")
result_label.pack()

# Run the window
window.mainloop()