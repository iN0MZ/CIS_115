# message.py
# Ryan Carroll
# CIS 115 (NLE01)
# Asks the user for a filename and checks to see if the file exists. If not it prompts the user to create one.


# Import the sys module, which contains the `exit()` function
import sys

# Define the main function
def main():
    # Ask the user to enter a file name
    file_name = input("Please enter a file name: ")

    # Initialize the user_input variable to None
    user_input = None

    # Try to open the file in read mode
    try:
        new_file = open(f'{file_name}', 'r')
    # If the file doesn't exist, catch the FileNotFoundError
    except FileNotFoundError as e:
        # Print the error message
        print(e)
        # Notify the user that the file doesn't exist
        print("file does not exist")
        # Ask the user if they want to create a new file
        print("Would you like to create a new file?\n(y/n):")

    # Get the user's input
    user_input = input()

    # Validate the user's input using a while loop
    while user_input.lower() != 'y' and user_input.lower() != 'n':
        # If the input is invalid, ask the user to enter a valid answer
        user_input = input("Please enter a valid answer(y / n): ")
        # If the user says 'n', close the program
        if user_input.lower() == 'n':
            print('Closing program.')
            sys.exit()
        # If the user says 'y', create a new file with the same name
        # as the one they entered earlier and write to it
        if user_input.lower() == 'y':
            new_file = open(f"{file_name}", "w")
            new_file.write("This is a new text file!")
            # Notify the user that the file was created
            print("The file was created.")
        # Close the file
        new_file.close()

# Call the main function
main()
