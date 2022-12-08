# lists.py
# Ryan Carroll
# CIS 115 (NLE01)
# Adds items to a list

def main():
    newList = []
    addToList = 0
    print("Please add a grocery item to the list.")
    item = input()
    while addToList <1:
        while item in newList:
            item = input("\nItem already in list. Please try again.")
        newList.append(item)
        print("Do you wish to add another item? (y/n).")
        answer = input().lower()

        while answer not in ['yes', 'no', 'n', 'y']:
            answer = input("Please enter a valid answer: (y/n)")

        if answer == 'y' or answer == 'yes':
            item = input("Enter next item: ")

        else:
            addToList += 1

    output(newList)
    input()

def output(aList):
    groceryList = ['Oregano', 'Sage', 'Rosemary', "Sea Salt", 'Olive Oil']
    grocery = aList + groceryList
    print("\t\tList\t\t")
    for i in grocery:
        address = grocery.index(i)
        print(f"Item:{i}, || Index #:{address}")



main()