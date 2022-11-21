new_file = open('newTXTfile.txt', 'w')

for i in range(5):
    user_input = int(input("Enter an Integer:"))
    new_file.write(str(user_input))
    new_file.write("\n")

new_file.close()


int_file = open("newTXTfile.txt", 'r')
read = int_file.readline()
read = read.rstrip('\n')
totes = 0
print(read)
while read != "":
    read = read.rstrip('\n')
    totes += int(read)
    print(read)
    read = int_file.readline()
print(f'The sum of the five integers is: {totes}')

next_file = open('result.txt', 'w')
next_file.write(f'The sum of the five integers is: {totes}')
next_file.close()