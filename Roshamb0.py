# This program will play you in Rock, Paper, Scissors
# Ryan Carroll

import random
player_roll = None
cpu_roll = None
def main():
    cpu_roll = cpu_choice()
    userInput = user_choice()
    player_roll = numAssign(userInput)

    comparison(player_roll, cpu_roll)


def cpu_choice():
    cpu_select = random.choice([1, 2, 3])
    if cpu_select == 1:
        print("The computer picked Rock!")
    elif cpu_select == 2:
        print("The computer picked Paper!")
    elif cpu_select == 3:
        print("The computer picked Scissors!")
    return cpu_select
def user_choice():
    userInput = input(str("Select Rock, Paper or Scissors: "))
    acceptedInput = ['rock', 'paper', 'scissors']
    if userInput.lower() not in acceptedInput:
        print("Invalid choice. Please try again.")
    print("User_Choice function: Much Success")
    return userInput.lower()



# def is_input_valid(user_choice):
#     return any([x.search(user_choice) is not none for x in valid_inputs])


def numAssign(userInput):
    if userInput == "rock":
        player_choice = 1
    elif userInput == "paper":
        player_choice = 2
    elif userInput == "scissors":
        player_choice = 3
    return player_choice



def comparison(player_roll, cpu_roll):
    if player_roll == 1 and cpu_roll == 2:
        return print("Paper covers Rock\n You Lose!")

    elif player_roll == 1 and cpu_roll == 3:
        return print("Rock smashes Scissors\nYou Win!")

    elif player_roll == 2 and cpu_roll == 1:
        return print("Paper covers Rock\nYou Win!")

    elif player_roll == 2 and cpu_roll == 3:
        return print("Scissors cuts Paper\nYou Lose!")

    elif player_roll == 3 and cpu_roll == 1:
        return print("Rock smashes Scissors\nYou Lose!")

    elif player_roll == 3 and cpu_roll == 2:
        return print("Scissors cuts Paper\nYou Win!")

    elif player_roll == cpu_roll:
        return print("Tie")




main()

