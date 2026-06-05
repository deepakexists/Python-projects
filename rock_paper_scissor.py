'''
WORKFLOW OF PROJECT
1= Input from user(rock, paper, scissor)
2- Computer choice (Computer will chose randomly not conditionaly)
2- Print result

Cases :
A- Rock
Rock - Rock = tie
Rock - paper = paper win
Rock - scissor = Rock wins

B- Paper
paper - paper = tie
paper - rock = rock win
paper - scissor = scissor win

C- Scissor
Scissor - scissor = tie
Scissor - rock = rock win
Scissor - paper = scissor win

'''

import random
list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move(Rock, Paper, Scissor): ")
comp_choice = random.choice(list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if(comp_choice == user_choice):
    print("Both chooses same:- Match tie")

elif(comp_choice == "Rock"):
    if(user_choice == "paper"):
        print("Paper cover the Rock = YOU WIN")
    else:
        print("Rock smashes Scissor = Computer win")

elif(comp_choice == "paper"):
    if(user_choice == "Rock"):
        print("Paper cover the Rock = Computer win")
    else:
        print("Scissor cut the paper = YOU WIN")

elif(comp_choice == "Scissor"):
    if(user_choice == "paper"):
        print("Scissor cut the paper = computer win")
    else:
        print("Rock smashes Scissor = YOU WIN")