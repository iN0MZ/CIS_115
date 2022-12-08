# Ryan Carroll
# CIS_115_NLE01
# paintEstimater.py
# Asks user square footage / paint costs and returns data required to quote jobs

# A painting company has determined that for every 112 square feet of wall space, one gallon of paint and
# eight hours of labor will be required.

labor_rate = 35     # Labor rate constant
wall_space = 112    # Wall space constant

def main():
    area, cost_per_gallon = get_data()                                  # Run get_data() and set output to variables area and cost_per_gallon
    paint_cost, multiplier = calculate_paint(area, cost_per_gallon)     # Take above variables and import into calculate_paint - output to variables
    labor_total = int(labor_charges(multiplier))                        # Calculates labor costs with imported multiplier, exports labor_total variable
    final_bill = total_charges(paint_cost, labor_total)                 # Adds the variables paint_cost and labor_total, exports to final_bill
    printTotals(labor_total, paint_cost, multiplier, final_bill)        # Print function

def get_data():
    area = int(input("Enter total wall space in SqFt:"))                # Asks user to input total SqFt of wall
    cost_per_gallon = int(input("Enter cost per Gallon of paint:"))     # Asks user to input cost per Gallon of paint
    return area, cost_per_gallon

def calculate_paint(area, cost_per_gallon):     # Calculates paint costs
    multiplier = int(area) / int(wall_space)    # Imports area and cost_per_gallon
    paint_cost = cost_per_gallon * multiplier   # Does math
    return int(paint_cost), int(multiplier)     # Returns values

def labor_charges(multiplier):                  # Calculates labor charge
    labor_total = labor_rate * multiplier       #
    return labor_total

def total_charges(paint_cost, labor_total):     # Calculates total charges of paint and labor costs
    final_bill = paint_cost + labor_total       #
    return final_bill

def printTotals(labor_total, paint_cost, multiplier, final_bill): #
    print(f"Total labor required: {multiplier} Hours")            #
    print(f"Total labor costs: ${labor_total}")                   # Defines printTotals and prints each line
    print(f"Total paint needed: {multiplier} Gallons")            #
    print(f"Paint cost: ${paint_cost}")                           #
    print(f"Total job cost: ${final_bill}")                       #

main() # Calling main function