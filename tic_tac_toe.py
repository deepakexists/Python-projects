# import tkinter as tk
# from tkinter import messagebox

# def check_winner():
#     for combo in [
#     [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
#         if button[combo[0]]["text"] == button[combo[1]]["text"] == button[combo[2]]["text"] !="":
#             button[combo[0]].config(bg="green")
#             button[combo[1]].config(bg="green")
#             button[combo[2]].config(bg="green")
#             messagebox.showinfo("Tic-Tac-Toe", f" player {button[combo[0]]['text']} Wins!")
#             root.quit()

# def button_click(index):
#     if button[index]["text"] == "" and not winner:
#         button[index]["text"] = current_player
#         check_winner()
#         toggle_player()

# def toggle_player():
#     global current_player
#     current_player = "X" if current_player == "O" else "O"
#     label.config(text = f"player {current_player}'s turn")  

# root = tk.Tk()
# root.title("Tic-Tac-Toe")

# button = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i:button_cleck(i)) for i in range(9)]

# for i, button in enumerate(button):
#     button.grid(row=i // 3, column=i % 3)

# current_player = "X"
# winner = False
# label = tk.Label(root, text=f"player {current_player}'s turn", font=("normal", 16))
# label.grid(row=3, column=0, columnspan=3)

# root.mainloop()










import tkinter as tk
from tkinter import messagebox

# Global variables
current_player = "X"
winner = False

# Check for winner
def check_winner():
    global winner

    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combo in winning_combinations:
        if (
            buttons[combo[0]]["text"] ==
            buttons[combo[1]]["text"] ==
            buttons[combo[2]]["text"] != ""
        ):
            winner = True

            buttons[combo[0]].config(bg="lightgreen")
            buttons[combo[1]].config(bg="lightgreen")
            buttons[combo[2]].config(bg="lightgreen")

            messagebox.showinfo(
                "Tic-Tac-Toe",
                f"Player {buttons[combo[0]]['text']} Wins!"
            )
            return

    # Check for draw
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        winner = True


# Change player
def toggle_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    label.config(text=f"Player {current_player}'s Turn")


# Handle button click
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player

        check_winner()

        if not winner:
            toggle_player()


# Create window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons
buttons = []

for i in range(9):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 25),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )

    btn.grid(row=i // 3, column=i % 3)
    buttons.append(btn)

# Status label
label = tk.Label(
    root,
    text=f"Player {current_player}'s Turn",
    font=("Arial", 16)
)

label.grid(row=3, column=0, columnspan=3, pady=10)

# Run application
root.mainloop()