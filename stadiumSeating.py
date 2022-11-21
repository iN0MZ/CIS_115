# Ryan Carroll
# CIS_115_NLE01
# stadiumSeating.py

class_a = 0
class_b = 0
class_c = 0
total_sales = 0
def main():
    get_tickets_sold()

def get_tickets_sold():
    class_a = input("How many Class A tickets were sold?")
    class_b = input("How many Class B tickets were sold?")
    class_c = input("How many Class C tickets were sold?")
    return
def calc_total_sales():
    total_a = class_a * 20
    total_b = class_b * 15
    total_c = class_c * 10
    total_sales = total_a + total_b + total_c
    return total_sales
