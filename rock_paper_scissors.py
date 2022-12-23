# This program will play you in Rock, Paper, Scissors
# Ryan Carroll

import random
from rock_paper_scissors_artwork import you_ready, you_win, you_lose, you_tie

player_roll = None
cpu_roll = None


########################################
# Main: while loop prints the title img, copywriter, as well as wins and losses
# defines cpu_roll, user_str_input and player_roll
# cpu_roll = 1, 2 or 3 assigned by cpu_choice function
# user_str_input = 'rock' 'paper' or 'scissors'
# player_roll = 1, 2 or 3 now after passing through numAssign()
# while loop prompts the user to play and gets both cpu and user rolls
# calls comparison() for game logic
# Displays wins and losses again and prompts the user to play again
# clear() to wipe the console and start over

def main():
    wins = 0
    losses = 0
    while True:
        print(f"{you_ready}\n®Ryan Carroll 2022\nWins:{wins}\nLosses:{losses}")
        cpu_roll = cpu_choice()
        user_str_input = user_choice()
        player_roll = numAssign(user_str_input)
        if comparison(player_roll, cpu_roll, user_str_input) == 1:
            wins += 1
            print(f"Wins: {wins}\nLosses: {losses}")
        else:
            losses += 1
            print(f"Wins: {wins}\nLosses: {losses}")
        if input("Play again? (Y/N)").strip().upper() != 'Y':
            break
        clear()


#####################################################
# cpu_choice(): gets a random number for the computer
# 1, 2 or 3 is the output
#

def cpu_choice():
    cpu_select = random.choice([1, 2, 3])
    return cpu_select


################################################################
# user_choice(): Takes user input as a string
# defines what input is acceptable
# checks to see if the input matches and if not restarts the loop

def user_choice():
    userInput = None
    acceptedInput = ['rock', 'paper', 'scissors']
    while userInput not in acceptedInput:
        userInput = input("Lets play a game.\nSelect Rock, Paper or Scissors: \n")

        if userInput.lower() in acceptedInput:
            return userInput.lower()
        else:
            print("Unexpected input\nPlease choose: rock, paper or scissors")
            continue


#########################################################################
# numAssign: Assigns the random number to an associated object
# "this is not the efficient way"
# You could remove this function by using a dictionary instead
# This function takes the string input and changes it to an integer item key
# importing user_str_input and checking it against each possible output
# Export player_choice
def numAssign(user_str_input):
    if user_str_input == "rock":
        player_choice = 1
    elif user_str_input == "paper":
        player_choice = 2
    elif user_str_input == "scissors":
        player_choice = 3
    return player_choice


##################################################################
# comparison(): Takes the following arguments:
# player_roll, cpu_roll and user_str_input
# Calculates the different game outcomes and will assign a score to
# result +/- 1
# Draws art through print statements
# Returns result

def comparison(player_roll, cpu_roll, user_str_input):
    result = 0
    print(f"You picked: {user_str_input}")
    if player_roll == 1 and cpu_roll == 2:
        result = -1
        print(f"The CPU selected: paper!\nPaper covers Rock\n{you_lose}")
    elif player_roll == 1 and cpu_roll == 3:
        result = 1
        print(f"The CPU selected: scissors!\nRock smashes Scissors\n{you_win}")

    elif player_roll == 2 and cpu_roll == 1:
        result = 1
        print(f"The CPU selected: rock!\nPaper covers Rock\n{you_win}")

    elif player_roll == 2 and cpu_roll == 3:
        result = -1
        print(f"The CPU selected: scissors!\nScissors cuts Paper\n{you_lose}")

    elif player_roll == 3 and cpu_roll == 1:
        result = -1
        print(f"The CPU selected: rock!\nRock smashes Scissors\n{you_lose}")

    elif player_roll == 3 and cpu_roll == 2:
        result = 1
        print(f"The CPU selected: paper!\nScissors cuts Paper\n{you_win}")

    elif player_roll == cpu_roll:
        result = 0
        print(f"The CPU chose: {user_str_input}\n {you_tie}")
    return result


################################################
# clear(): This function wipes the console with new lines
#
def clear():
    print("\n" * 47)


#############################################################
# The if __name__ == "__main__": statement is used to check whether the code is being
# run directly from the command line or being called from another module.
# If the code is being run directly from the command line, then the if statement
# evaluates to True and the main() function is called.
#

main()
