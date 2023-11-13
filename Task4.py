import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock, Paper, Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.user_choice_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.score_var = tk.StringVar()
        self.feedback_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Label explaining the game logic
        game_logic_label = tk.Label(self.master, text="Game Logic", font=('Helvetica', 16, 'bold'))
        game_logic_label.pack(pady=10)  # Add vertical spacing

        game_logic_text = (
            "• Rock beats scissors\n"
            "• Scissors beat paper\n"
            "• Paper beats rock"
        )
        game_logic_detail_label = tk.Label(self.master, text=game_logic_text, font=('Helvetica', 12))
        game_logic_detail_label.pack()

        # Label and Entry for the user to input choice
        tk.Label(self.master, text="Choose Rock, Paper, or Scissors:").pack(pady=5)  # Add vertical spacing
        entry = tk.Entry(self.master, textvariable=self.user_choice_var)
        entry.pack(pady=5)  # Add vertical spacing

        # Button to submit the user's choice
        tk.Button(self.master, text="Submit", command=self.play).pack(pady=5)  # Add vertical spacing

        # Button to play again
        tk.Button(self.master, text="Play Again", command=self.reset_game).pack(pady=5)  # Add vertical spacing
        
        # Display result and score
        result_label = tk.Label(self.master, textvariable=self.result_var, font=('Helvetica', 14))
        result_label.pack(pady=3)  # Add vertical spacing

        score_label = tk.Label(self.master, textvariable=self.score_var, font=('Helvetica', 12))
        score_label.pack(pady=3)  # Add vertical spacing

        # Feedback Entry and Submit Button
        tk.Label(self.master, text="Feedback:").pack(pady=3)  # Add vertical spacing
        feedback_entry = tk.Entry(self.master, textvariable=self.feedback_var)
        feedback_entry.pack(pady=5)  # Add vertical spacing

        tk.Button(self.master, text="Submit Feedback", command=self.submit_feedback).pack(pady=3)  # Add vertical spacing

        # Button to play again
        tk.Button(self.master, text="Play Again", command=self.reset_game).pack(pady=5)  # Add vertical spacing

    def play(self):
        user_choice = self.user_choice_var.get().lower()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        result = self.determine_winner(user_choice, computer_choice)

        if "win" in result.lower():
            self.result_var.set(f"Result: {result.capitalize()}")
        elif "lose" in result.lower():
            self.result_var.set(f"Result: {result.capitalize()}")
        else:
            self.result_var.set(f"Result: {result.capitalize()}")

        self.update_score(result)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            return "You win!"
        else:
            return "You lose!"

    def update_score(self, result):
        if "win" in result.lower():
            self.user_score += 1
        elif "lose" in result.lower():
            self.computer_score += 1

        self.score_var.set(f"Score: You {self.user_score} - {self.computer_score} Computer")

    def reset_game(self):
        self.user_choice_var.set("")
        self.result_var.set("")
        self.result_var.config(fg='black')
        self.score_var.set("")

    def submit_feedback(self):
        feedback = self.feedback_var.get()
        messagebox.showinfo("Feedback Submitted", f"Feedback received: {feedback}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")  # Set window size to 500x400
    app = RockPaperScissorsGame(root)
    root.mainloop()
