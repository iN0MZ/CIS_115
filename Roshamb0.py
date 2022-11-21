# This program will play you in Rock, Paper, Scissors
# Ryan Carroll

import random
import re

rock = 1
paper = 2
scissors = 3
cpu_choice = 0
user_choice = 0
valid_inputs = False

def main():
    cpu_choice()
    user_choice()

def cpu_choice():
    cpu_choice = random.choice([1,2,3])
    print(cpu_choice)

def user_choice():
    while True:
        try:
            userInput = input(print("Select Rock, Paper or Scissors: "))
            userInput = userInput.lower()
            rock_re = re.compile("rock", flags=re.I)
            paper_re = re.compile("paper", flags=re.I)
            scissors_re = re.compile("scissors", flags=re.I)
            valid_inputs = [rock_re, paper_re, scissors_re]
            return
        else:
            print('Bad choice')
            break

def is_input_valid(user_choice):
    return any([x.search(user_choice) is not none for x in valid_inputs])
main()