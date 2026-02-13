age= 17 
if (age>=18):
    print("can vote ")
    print("can drive ")
else:
    print("not aligible ")
name=("abhinav","piyush","pandat","pal")
auraname=input("enter your name ")        
if auraname not in name:
    print("you are not aligible for aurafarming")
else:
    print("you are aura farmer")
# GAME BROOOO!!!!!
import random

# Choices
choices = ['rock', 'paper', 'scissors']

# Get user input
user_choice = input("Enter rock, paper, or scissors: ").lower()

# Validate input
if user_choice not in choices:
    print("Invalid input. Please choose rock, paper, or scissors.")
else:
    # Computer randomly chooses
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("You win!")
    else:
        print("Computer wins!")





