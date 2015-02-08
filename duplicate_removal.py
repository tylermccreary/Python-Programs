# duplicate_removal.py
# A program to remove duplicate values from data input.  Enter 0 to quit.
# Author: Tyler McCreary

def main():
    input_number = int(input("Please input a number: "))
    input_list = []
    
    while (input_number != 0):
        if input_list.count(input_number) == 0:
            input_list.append (input_number)
        input_number = int(input("Please input a number: "))
       
    print ("List with duplicates removed: " + str(input_list))

main()
