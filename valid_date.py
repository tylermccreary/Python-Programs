# valid_date.py
# A program to validate dates.
# Author: Tyler McCreary


def isValidYear(year):
    # Only accept years 1600-2400.
            if year <= 2400 and year >= 1600:
                return True
            return False

def isLeapYear(year):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        return False

def isValidMonth(month):
                if month <=12 and month >= 1:
                    return True
                return False

def isValidDay(year, month, day):
            #30 days.
                    if month == 4 or month == 6 or month == 9 or month == 11:
                        if day <= 30 and day >= 1:
                            return True
            #31 days.
                    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                        if day <= 31 and day >= 1:
                            return True
            #February
                    elif month == 2:
                        if isLeapYear(year):
                            if day <= 29 and day >= 1:
                                return True
                    return False
        
def main():
    invalid = True
    while(invalid):
        input_day = int(input("Please enter a day: "))
        input_month = int(input("Please enter a month: "))
        input_year = int(input("Please enter a year: "))    
                       
        if isValidYear(input_year) and isValidMonth(input_month) and isValidDay(input_year, input_month, input_day):
            print("Valid date")
            invalid = False
        else:
            print("Invalid date")
            
main()

