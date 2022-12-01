#mockSaveFile.py

def main():
    print("\tMenu\n")
    print("1. Start New Game")
    print("2. Continue")
    print("3. Quit")

    print("Please pick an option.")
    choice = input()
    if choice == '2':
        try:
            saveFile1 = open("save001.txt", 'r')
        except FileNotFoundError:
            print("Error: No saved game file found.")
            print("Would you like to start a new game\nY/N:?")
            user = input()
            if user.lower() == 'y':
                saveFile1 = open("save001.txt", 'w')
        except:
            print("Unknown error")
            sys.exit()
        else:
            print("welcome back!")
main()