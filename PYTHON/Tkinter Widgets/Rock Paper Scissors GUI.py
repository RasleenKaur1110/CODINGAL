import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.choices = ["Rock", "Paper", "Scissors"]

        tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 14)).pack(pady=10)
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        for choice in self.choices:
            tk.Button(root, text=choice, font=("Arial", 12), command=lambda c=choice: self.play(c)).pack(pady=5)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
        else:
            result = "Computer wins!"

        self.result_label.config(text=f"You: {user_choice} | Computer: {computer_choice}\n{result}")

if __name__ == "__main__":
    root = tk.Tk()
    RockPaperScissors(root)
    root.mainloop()