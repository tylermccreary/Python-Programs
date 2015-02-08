# roman_numeral_to_decimal
# A program to convert roman numerals to decimals. Just follows basic rules.
# Author: Tyler McCreary

roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, \
         "M": 1000, "CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9}

def roman_to_decimal(string):
    index = 0
    total = 0
    while index < len(string)-1:
        if roman[string[index]] < roman[string[index+1]]:
            total += roman[string[index+1]] - roman[string[index]]
            index += 2
        else:
            total += roman[string[index]]
            index +=1
    if roman[string[-1]] <= roman[string[-2]]:
            total += roman[string[-1]]
    return total

def main():
    roman_string = input("Please enter a roman numeral: ")
    decimal = roman_to_decimal(roman_string)
    print (decimal)

main()
