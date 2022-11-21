# Ryan Carroll
# CIS_115_NLE01
# paintEstimater.py
# Asks user square footage and returns data required to paint

# A painting company has determined that for every 112 square feet of wall space, one gallon of paint and
# eight hours of labor will be required.

labor_rate = 35
wall_space = 112

def main():
    area, cost_per_gallon = get_data()
    paint_cost, multiplier = calculate_paint(area, cost_per_gallon)
    labor_total = int(labor_charges(multiplier))
    final_bill = total_charges(paint_cost, labor_total)
    printTotals(labor_total, paint_cost, multiplier, final_bill)

def get_data():
    area = int(input("Enter total wall space in SqFt:"))
    cost_per_gallon = int(input("Enter cost per Gallon of paint:"))
    return area, cost_per_gallon

def calculate_paint(area, cost_per_gallon):
    multiplier = int(area) / int(wall_space)
    paint_cost = cost_per_gallon * multiplier
    return int(paint_cost), int(multiplier)

def labor_charges(multiplier):
    labor_total = labor_rate * multiplier
    return labor_total

def total_charges(paint_cost, labor_total):
    final_bill = paint_cost + labor_total
    return final_bill

def printTotals(labor_total, paint_cost, multiplier, final_bill):
    print(f"Total labor required in hours: {multiplier}")
    print(f"Total labor costs: ${labor_total}")
    print(f"Total paint needed (Gallons): {multiplier}")
    print(f"Paint costs: {paint_cost}")
    print(f"Total cost: ${final_bill}")
main()