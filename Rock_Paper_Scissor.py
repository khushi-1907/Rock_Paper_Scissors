import tkinter as tk
from tkinter import messagebox, ttk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x600")
root.configure(bg="#f4f6f8")

# Fonts
TITLE_FONT = ("Segoe UI", 26, "bold")
LABEL_FONT = ("Segoe UI", 16)
BUTTON_FONT = ("Segoe UI", 14)

# Global variables
user_score = 0
comp_score = 0
choices = ["Rock", "Paper", "Scissors"]
emojis = {"Rock": "🧱", "Paper": "📄", "Scissors": "✂️"}

# Functions
def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)

    user_label.config(text=f"You: {emojis[user_choice]}")
    comp_label.config(text=f"Computer: {emojis[comp_choice]}")

    if user_choice == comp_choice:
        result_label.config(text="It's a Tie!", fg="#007acc")
    elif (
        (user_choice == "Rock" and comp_choice == "Scissors") or
        (user_choice == "Paper" and comp_choice == "Rock") or
        (user_choice == "Scissors" and comp_choice == "Paper")
    ):
        user_score += 1
        result_label.config(text="You Win! 🎉", fg="#28a745")
    else:
        comp_score += 1
        result_label.config(text="You Lose! 😢", fg="#dc3545")

    update_score()

def update_score():
    score_label.config(text=f"Score: You {user_score} - {comp_score} Computer")

def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_label.config(text="You: ❓")
    comp_label.config(text="Computer: ❓")
    result_label.config(text="Let's Play!", fg="#333")
    update_score()

def exit_game():
    if messagebox.askyesno("Exit", "Do you want to quit?"):
        root.destroy()

# Title
title = tk.Label(root, text="🎮 Rock Paper Scissors", font=TITLE_FONT, bg="#f4f6f8", fg="#222")
title.pack(pady=30)

# Player and Computer choices
user_label = tk.Label(root, text="You: ❓", font=LABEL_FONT, bg="#f4f6f8", fg="#333")
user_label.pack(pady=10)

comp_label = tk.Label(root, text="Computer: ❓", font=LABEL_FONT, bg="#f4f6f8", fg="#333")
comp_label.pack(pady=10)

# Result display
result_label = tk.Label(root, text="Let's Play!", font=("Segoe UI", 18, "bold"), bg="#f4f6f8")
result_label.pack(pady=20)

# Scoreboard
score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=LABEL_FONT, bg="#f4f6f8", fg="#444")
score_label.pack(pady=10)

# Styling Buttons
def create_modern_button(parent, text, color, command):
    return tk.Button(
        parent,
        text=text,
        font=BUTTON_FONT,
        width=12,
        height=2,
        bg=color,
        fg="#000",
        bd=0,
        activebackground="#e6e6e6",
        cursor="hand2",
        command=command
    )

# Button Frame
button_frame = tk.Frame(root, bg="#f4f6f8")
button_frame.pack(pady=25)

rock_btn = create_modern_button(button_frame, "🧱 Rock", "#ffccd5", lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = create_modern_button(button_frame, "📄 Paper", "#d1f7c4", lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = create_modern_button(button_frame, "✂️ Scissors", "#cfe2ff", lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Control Buttons (Reset, Exit)
control_frame = tk.Frame(root, bg="#f4f6f8")
control_frame.pack(pady=30)

reset_btn = create_modern_button(control_frame, "🔄 Restart", "#e2e3e5", reset_game)
reset_btn.grid(row=0, column=0, padx=15)

exit_btn = create_modern_button(control_frame, "❌ Exit", "#ffe2e2", exit_game)
exit_btn.grid(row=0, column=1, padx=15)

# Main loop
root.mainloop()
