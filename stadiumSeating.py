# Ryan Carroll
# CIS_115_NLE01
# stadiumSeating.py
# Converts ticket types into correct dollar amount then adds the total

a_value = 20    #
b_value = 15    # Sets the ticket prices as constants
c_value = 10    #

def main():
    num1, num2, num3 = get_tickets_sold()  # Calls get tickets sold and sets output to num 1,2,3
    total_sum = calc_total_sales(num1,num2,num3) # Calls calc_total_sales passing num 1,2,3 - Sets to total_sum variable
    output(total_sum) # calls total sum function

def get_tickets_sold(): # Asks the user for input then sets the input to variables num 1,2,3
    num1 = int(input("How many Class A tickets were sold? "))
    num2 = int(input("How many Class B tickets were sold? "))
    num3 = int(input("How many Class C tickets were sold? "))
    return int(num1), int(num2), int(num3) # Returns the integer of each variable

def calc_total_sales(num1, num2, num3): # Does math and outputs total_sum
    total_a = num1 * a_value
    total_b = num2 * b_value
    total_c = num3 * c_value
    total_sum = total_a + total_b + total_c
    return total_sum

def output(total_sum): # Prints the total sum variable
    print(f"${total_sum}")


main()
