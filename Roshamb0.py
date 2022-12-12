# This program will play you in Rock, Paper, Scissors
# Ryan Carroll

import random
from roshamb0_artwork import you_ready, you_win, you_lose, you_tie

player_roll = None
cpu_roll = None


########################################
# Defines the Main function
# Defines and sets cpu_roll and player_roll to the correct integer value

def main():
    cpu_roll = cpu_choice(player_score)
    user_str_input = user_choice()
    player_roll = numAssign(user_str_input)
    comparison(player_roll, cpu_roll, user_str_input, player_score)




def cpu_choice(player_score):
    cpu_select = random.choice([1, 2, 3])
    # if cpu_select == 1:
    #     print(f"The computer picked Rock!")
    # elif cpu_select == 2:
    #     print("The computer picked Paper!")
    # elif cpu_select == 3:
    #     print("The computer picked Scissors!")
    print(f"{you_ready}\n® Ryan Carroll 2022\nCurrent win rate:{player_score}")
    return cpu_select


##################################################################
# user_choice: Takes user input as a string
# defines what input is acceptable
# checks to

def user_choice():
    userInput = None
    acceptedInput = ['rock', 'paper', 'scissors']
    while userInput not in acceptedInput:
        userInput = input(str("Lets play a game.\nSelect Rock, Paper or Scissors: "))

        if userInput.lower() in acceptedInput:
            return userInput.lower()
        else:
            print("Unexpected input\nPlease choose: rock, paper or scissors")
            continue


#########################################################################
# numAssign: Assigns the random number to an associated object
# "this is not the efficient way" - just do it
# This function takes the string input and changes it to an integer item key
# You could remove this function by using a dictionary instead
# importing user_str_input and checking it against each possible output
def numAssign(user_str_input):
    if user_str_input == "rock":
        player_choice = 1
    elif user_str_input == "paper":
        player_choice = 2
    elif user_str_input == "scissors":
        player_choice = 3
    return player_choice


def comparison(player_roll, cpu_roll, user_str_input, player_score):
    print(f"You picked: {user_str_input}")
    if player_roll == 1 and cpu_roll == 2:
        player_score += -1
        return player_score, print(f"The CPU selected: paper!\nPaper covers Rock\n{you_lose}")

    elif player_roll == 1 and cpu_roll == 3:
        player_score += 1
        return player_score, print(f"The CPU selected: scissors!\nRock smashes Scissors\n{you_win}")

    elif player_roll == 2 and cpu_roll == 1:
        player_score += 1
        return player_score, print(f"The CPU selected: rock!\nPaper covers Rock\n{you_win}")

    elif player_roll == 2 and cpu_roll == 3:
        player_score += -1
        return player_score, print(f"The CPU selected: scissors!\nScissors cuts Paper\n{you_lose}")

    elif player_roll == 3 and cpu_roll == 1:
        player_score += -1
        return player_score, print(f"The CPU selected: rock!\nRock smashes Scissors\n{you_lose}")

    elif player_roll == 3 and cpu_roll == 2:
        player_score += 1
        return player_score, print(f"The CPU selected: paper!\nScissors cuts Paper\n{you_win}")

    elif player_roll == cpu_roll:
        return player_score, print(f"The CPU chose: {user_str_input}\n {you_tie}")
    return

def clear():
    print("\n" * 47)


while True:
    clear()
    main()
    if input("Play again? (Y/N)").strip().upper() != 'Y':
        break
