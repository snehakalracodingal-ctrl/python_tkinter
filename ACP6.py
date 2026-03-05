import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Function to play the game
def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    computer_label.config(text="Computer chose: " + computer_choice)
    result_label.config(text=result)

# Window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x300")

# Title
title = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 16))
title.pack(pady=10)

# Buttons
rock_btn = tk.Button(window, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.pack(pady=5)

paper_btn = tk.Button(window, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.pack(pady=5)

scissor_btn = tk.Button(window, text="Scissors", width=10, command=lambda: play("Scissors"))
scissor_btn.pack(pady=5)

# Labels
computer_label = tk.Label(window, text="Computer chose: ", font=("Arial", 12))
computer_label.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

window.mainloop()