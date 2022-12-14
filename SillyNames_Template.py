##Funny Name Generator Project
##Using Tuples 

import random
import csv

def main():
    ##the following print statements will be provided to you
    first_name_tup = tupleCreate()
    print(f"{first_name_tup}")
    print("Welcome to the Silly Name generator.")
    print("Generate a list of names for your sidekick/friend/pet.")
    print("The 10 names will be exported to a .txt file!")
    fileName = userInput()

    tupleCreate()

    ##Create Tuple with given first names.
    first_name_file = 'first_names_silly_name_generator.txt'
    last_name_file = 'last_names_silly_name_generator.txt'
    first = tupleCreate()
    last = tupleCreate()

    ##create a function called userInput() to receive the name of the file.

    input("\nHit Enter to Generate.\n")

    ##create a function called "createFile"
    ##that only takes user's file name and returns a file object.

    ##place your generator file here. It is a void function that
    ##takes 3 arguments.

    print("\n\nFile has been created.\n")
    input("Hit enter to Quit")


def userInput():
    ##This function takes no parameters

    ##this function takes user input for a file name.

    ##Input validation if '.txt' is does not exist add it

    ##return the file name string
    user = input("\nPlease enter a file name:\n")


def tupleCreate():
    first_name_tup = None
    # with open('first_names_silly_name_generator.txt', 'r') as f:
    #     mylist = [tuple(map(str, i.split(','))) for i in f]

    with open("{}") as load_file:
        reader = csv.reader(load_file, delimiter=",")
        data = [row for row in reader]
        first_name_tup = tuple(*data)
        return first_name_tup
    # ('word1','word2','word3','word4','word5')


#     if '.txt' not in user:
#
#         ##connact .txt to name
#
#
# def createFile():
#     ##this function takes one parameter called "file name"
#
#     ##open a new file in mode 'w' with the given file name.
#
#     ##return the created file. Do NOT close file here.
#
#
# def generateNames(firstName, lastName, file):
#
#     ##Randomly generate names with a for loop 10 times
#
#     ##you must generate by first getting a randomly generated index THEN
#     ##assign it to either first or last
#
#     ##append/write each first + last name to the file
#     ##Each name MUST be on a new line!!
#
#     ##you will want to remove the names from the new coped list to ensure
#     ##no names are choosen twice!
#
#     ##print out the names in console
#
#
#     ##close file outside of the for loop!
#
#     firstName = list(firstName)
#     lastName = list(lastName)
#
#     print("\t\tYour Generated Names:")
#     ##Your for loop
#       ##find a random index in your list
#       ##
#
#       ##find the item by using the index
#       ##
#
#       ##remove the items from list
#       ##
#
#       ##make a variable that has first + last names
#
#       ##print
#
#       ##write to file
#
#

main()
