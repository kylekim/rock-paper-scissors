import random


def play():
    user_choice = input("Enter rock, paper, or scissors: ")

    computer_choice = random.randint(1, 3)

    if computer_choice == 1:
        computer_choice = "rock"
    elif computer_choice == 2:
        computer_choice = "paper"
    elif computer_choice == 3:
        computer_choice = "scissors"

    print("The computer chose " + computer_choice)

    if user_choice.lower() == computer_choice:
        print("Tie!")
    elif user_choice.lower() == "rock" and computer_choice == "paper":
        print("You lose!")
    elif user_choice.lower() == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice.lower() == "paper" and computer_choice == "scissors":
        print("You lose!")
    elif user_choice.lower() == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice.lower() == "scissors" and computer_choice == "rock":
        print("You lose!")
    elif user_choice.lower() == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("Error: Invalid user input")


play()
