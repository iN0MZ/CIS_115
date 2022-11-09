# This program will play you in Rock, Paper, Scissors
# Ryan Carroll

import random
import re

rock = 1
paper = 2
scissors = 3
cpu_choice = 0
user_choice = 0

def main():
    cpu_choice()
    user_choice()

def cpu_choice():
    cpu_choice = random.choice([1,2,3])
    print(cpu_choice)

def user_choice():
    userInput = input(print("Select Rock, Paper or Scissors: "))
    userInput = userInput.lower()
    rock_re.search


main()