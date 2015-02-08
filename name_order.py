# name_order.py
# A program to reorder a person's name
# Author: Tyler McCreary

def main():
    name = input("Input the name to be reordered: ")
    spaces = name.find(" ")
    if spaces <= 0:
        print("invalid name")
    else:
        first = name[:spaces]
        name = name[spaces + 1:]
        spaces = name.find(" ")
        if spaces == -1:
            print("invalid name")
        else:
            second = name[:spaces]
            name = name[spaces + 1:]
            spaces = name.find(" ")
            if spaces != -1:
                print("invalid name")
            else:
                third = name
                comma = first.find(",")         
                if comma == -1:
                    transformed = third + ', ' + first + ' ' + second
                    print(transformed)
                else:
                    transformed =  second + ' ' + third + ' ' + first[:-1]
                    print(transformed)

main()



