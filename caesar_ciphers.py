# casesar_ciphers.py
# A program to encode and decode Casesar ciphers.
# Author: Tyler McCreary

import string

def encode(character, offset):
    #Check to see if the characters are uppercase or lowercase or not a letter.
    #If the character is a letter, add the offset.
    if character in string.ascii_lowercase:
        index = string.ascii_lowercase.index(character)
        index = index + int(offset)
        if index > 25:
            index = index - 26
        return string.ascii_lowercase[index]
    elif character in string.ascii_uppercase:
        index = string.ascii_uppercase.index(character)
        index = index + int(offset)
        if index > 25:
            index = index - 26
        return string.ascii_uppercase[index]
    else:
        return character
        
def main():
    try:
        file_name = input("Input the file name to search for: ")
        offset = input("Input the offset: ")
        boolean = True

        input_file = open(file_name, "r")
        character = input_file.read(1)
        result = ''

        while boolean:
            character = encode(character, offset)
            result = result + character
        
            character = input_file.read(1)
            if not character:
                break
        print(result)
    except IOError:
        print("Invalid File")

main()
        
