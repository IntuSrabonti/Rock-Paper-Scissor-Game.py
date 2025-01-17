import tkinter as tk
import random
user_score = 0
comp_score = 0
def update_score():
    score_label.config(text=f"Player: {user_score} | Computer: {comp_score}")

def play(choice):
    global user_score, comp_score
    options = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(options)
    if choice == comp_choice:
        result = "Tie!"
    elif (choice == "Rock" and comp_choice == "Scissors") or \
         (choice == "Scissors" and comp_choice == "Paper") or \
         (choice == "Paper" and comp_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        comp_score += 1
    result_label.config(text=f"Your choice: {choice}\nComputer's choice: {comp_choice}\n{result}")
    update_score()
root = tk.Tk()
root.geometry("500x400")
root.title("Welcome To Playing World")
score_label = tk.Label(root, text=f"Player: {user_score} | Computer: {comp_score}", font=("Helvetica", 16))
score_label.pack(pady=40)
result_label = tk.Label(root, text="Choose Your Preferable One!", font=("Helvetica", 16))
result_label.pack(pady=50)
rock_button = tk.Button(root, text="Rock", command=lambda: play("Rock"))
rock_button.pack(side=tk.LEFT, pady=50)

paper_button = tk.Button(root, text="Paper", command=lambda: play("Paper"))
paper_button.pack(side=tk.LEFT, pady=50)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play("Scissors"))
scissors_button.pack(side=tk.LEFT, pady=50)

root.mainloop()
