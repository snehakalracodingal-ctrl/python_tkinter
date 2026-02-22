import tkinter as tk

def calculate_product():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    result_label.config(text="Product: " + str(result))

window = tk.Tk()
window.title("Product Calculator")
window.geometry("300x250")


tk.Label(window, text="Enter First Number").pack(pady=10)
entry1 = tk.Entry(window)
entry1.pack()


tk.Label(window, text="Enter Second Number").pack(pady=10)
entry2 = tk.Entry(window)
entry2.pack()

tk.Button(window, text="Calculate Product", command=calculate_product).pack(pady=10)


result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
