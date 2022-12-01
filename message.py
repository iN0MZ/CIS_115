# message.py
# Ryan Carroll
# CIS 115 (NLE01)
# Does input validation. Is homework. Much success

import sys

def main():
    file_name = input("Please enter a file name: ")
    userInput = None
    try:
        new_file = open(f'{file_name}', 'r')
    except FileNotFoundError as e:
        print(e)
        print("file does not exist")
        print("Would you like to create a new file?\n(y/n):")

        userInput = input()
        while userInput.lower() != 'y' and userInput.lower() != 'n':
            userInput = input("Please enter a valid answer(y / n): ")
        if userInput.lower() == 'n':
            print('Closing program.')
            sys.exit()
        if userInput.lower() == 'y':
            new_file = None
            new_file.write(str(userInput))
            new_file.write("This is a new file!")
            new_file.close()
main()