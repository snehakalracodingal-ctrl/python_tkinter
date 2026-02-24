import tkinter as tk

# Function to convert inches to centimeters
def convert_length():
    inches = float(entry_inches.get())
    centimeters = inches * 2.54
    result_label.config(text=f"{inches} inches = {centimeters:.2f} cm")

# Create main window
root = tk.Tk()
root.title("Length Converter App")
root.geometry("350x200")
root.resizable(False, False)

# Heading Label
heading = tk.Label(root, text="Inches to Centimeters Converter", font=("Arial", 12, "bold"))
heading.pack(pady=10)

# Input Label
label_inches = tk.Label(root, text="Enter length in inches:")
label_inches.pack()

# Entry Box
entry_inches = tk.Entry(root)
entry_inches.pack(pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert_length)
convert_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack()

# Run the application
root.mainloop()