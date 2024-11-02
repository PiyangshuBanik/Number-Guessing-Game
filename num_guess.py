import tkinter as tk
import random

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number")
        self.master.geometry("800x500")
        self.master.configure(bg="#f0f0f0")  # Light gray background
        
        # Initialize game variables
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 10
        
        # Create GUI components
        self.label = tk.Label(master, text="Guess a number between 1 and 100", bg="#f0f0f0", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Submit Guess", command=self.check_guess, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.guess_button.pack(pady=10)

        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game, bg="#f44336", fg="white", font=("Arial", 12))
        self.reset_button.pack(pady=10)

        self.hint_label = tk.Label(master, text="", bg="#f0f0f0", font=("Arial", 12))
        self.hint_label.pack(pady=10)

        self.attempts_label = tk.Label(master, text=f"Attempts remaining: {self.attempts}", bg="#f0f0f0", font=("Arial", 12))
        self.attempts_label.pack(pady=10)

        # Add a welcome message
        self.welcome_label = tk.Label(master, text="Piyangshu Welcomes you to The Number Guessing Game!", bg="#f0f0f0", font=("Arial", 16, "bold"))
        self.welcome_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < 1 or guess > 100:
                self.hint_label.config(text="Please guess a number between 1 and 100.", fg="orange")
                return
            
            if guess < self.number_to_guess:
                self.hint_label.config(text="Too low!", fg="blue")
            elif guess > self.number_to_guess:
                self.hint_label.config(text="Too high!", fg="red")
            else:
                self.hint_label.config(text=f"Congratulations! You've guessed the number {self.number_to_guess}!", fg="green")
                return
            
            self.attempts -= 1
            self.attempts_label.config(text=f"Attempts remaining: {self.attempts}")
            
            if self.attempts == 0:
                self.hint_label.config(text=f"Game Over! The number was {self.number_to_guess}.", fg="red")
                self.guess_button.config(state=tk.DISABLED)
        
        except ValueError:
            self.hint_label.config(text="Please enter a valid number.", fg="orange")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 10
        self.attempts_label.config(text=f"Attempts remaining: {self.attempts}")
        self.hint_label.config(text="")
        self.entry.delete(0, tk.END)
        self.guess_button.config(state=tk.NORMAL)

# Create the main window
root = tk.Tk()
game = GuessTheNumberGame(root)
root.mainloop()