# lists.py
# Ryan Carroll
# CIS 115 (NLE01)
# Is a grocery list

def main():
    # Create an empty list to store grocery items
    newList = []
    # Initialize variable to control the while loop
    addToList = 0

    # Prompt the user to add an item to the list
    print("Please add a grocery item to the list.")
    item = input()

    # Keep looping until the user is finished adding items
    while addToList <1:
        # Check if the item is already in the list
        while item in newList:
            # If the item is already in the list, prompt the user to try again
            item = input("\nItem already in list. Please try again.")
        # Add the item to the list
        newList.append(item)
        # Ask the user if they want to add another item
        print("Do you wish to add another item? (y/n).")
        answer = input().lower()

        # Check if the user's answer is valid
        while answer not in ['yes', 'no', 'n', 'y']:
            # If the answer is not valid, prompt the user to try again
            answer = input("Please enter a valid answer: (y/n)")

        # If the user wants to add another item, prompt them to enter it
        if answer == 'y' or answer == 'yes':
            item = input("Enter next item: ")

        # If the user does not want to add another item, exit the loop
        else:
            addToList += 1

    # Call the output function and pass it the list of items
    output(newList)
    # Wait for the user to press enter before closing the program
    input()

# Define the output function
def output(aList):
    # Create a list of predefined grocery items
    groceryList = ['Oregano', 'Sage', 'Rosemary', "Sea Salt", 'Olive Oil']
    # Combine the user's list of items with the predefined list
    grocery = aList + groceryList
    # Print a header for the list of items
    print("\t\tList\t\t")
    # Loop through each item in the list
    for i in grocery:
        # Get the index of the current item
        address = grocery.index(i)
        # Print the item and its index
        print(f"Item:{i}, || Index #:{address}")


# Call the main function to run the program
main()


main()