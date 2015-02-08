# file_search.py
# A program to search text files.
# Author: Tyler McCreary

import string

def main(): 
    search_string = input("Input the string to search for: ")
    found = False
    line = 1

    try:
        input_file = open("filesearchtest.txt", "r")
        for line_str in input_file:
            index = line_str.find (search_string)
            if index != -1:
                found = True
                break
            else:
                line = line + 1
        if found == False:
            print("String not found")
        else:
            print("String found: line " + str(line))

    except IOError:
        print("File not found")

main()

