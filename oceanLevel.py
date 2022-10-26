# oceanLevel.py
# Ryan Carroll
# CIS 115 (NLE01)
# Displays the number of millimeters that the ocean will have risen each year for the next 25 years

mm_rise_per_year = 1.6  # Rise per year of ocean in MM
expected_rise = 0       # Declaring the variable
years = int(input("Input a value representing years between 1 and 25: "))  # Taking input then,
                                                                           # setting that input to the var years
if years >=1 and years <= 26:  # If year is within the given range then do the math below
    expected_rise = years * mm_rise_per_year  # Math
    print("   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(\n `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `")  # Who doesn't like art?
    print(f"The sea level in {years} year(s) is expected to be:"     # Prints years
          f"", format(expected_rise, '.1f'), "millimeters higher.")  # Prints expected_rise formatted to one decimal
else:
    print("Please enter a valid number of years.")