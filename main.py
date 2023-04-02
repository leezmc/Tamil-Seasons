# Takes input of Gregorian date and outputs the Tamil season that it is in
# Author: Michael Lee
# Date: February 7, 2023

import sys
# takes abbreviate month and returns the month number
def monthNum(abbr):
    months = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 
              'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
    return months.get(abbr.lower(), 0)

# Checks if the user inputted month and day are valid days/months
def validDay(month, day):
    if month == 2:
        if 1 <= day <=29:
            return True
        else:
            return False
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= day <= 31:
            return True
        else:
            return False
    elif month in [4, 6, 9, 11]:
        if 1 <= day <= 30:
            return True
        else:
            return False
    else:
        return False

# Returns the Tamil month given day and month
def tamilSeason(month, day):
    if month == 2 and day >= 15 or month == 3 or month == 4 and day <= 14:
        return "IlaVenil"
    elif month == 4 and day >= 15 or month == 5 or month == 6 and day <= 14:
        return "MuthuVenil"
    elif month == 6 and day >= 15 or month == 7 or month == 8 and day <= 14:
        return "Kaar"
    elif month == 8 and day >= 15 or month == 9 or month == 10 and day <= 14:
        return "Kulir"
    elif month == 10 and day >= 15 or month == 11 or month == 12 and day <= 14:
        return "MunPani"
    elif month == 12 and day >= 15 or month == 1 or month == 2 and day <= 14:
        return "PinPani"

def main(): 
    print("Welcome to Tamil season converter.")
    monthAbbr = input("Enter Month (three letter abbrv.): ")
    month = monthNum(monthAbbr)
    if month == 0:
        print("Month Invalid")
        sys.exit(0)
    day = int(input("Enter Day (number): "))
    if not validDay(month, day):
        print("Day Invalid")
        sys.exit(0)
    actSeason = tamilSeason(month, day)
    print("Tamil Season is", actSeason)

if __name__ == '__main__':
    main()
