# word_sequence_analysis.py
# A program that parses a sentence and stores information about the order in which the words appear.
# Author: Tyler McCreary

import string

def find_occurences(input_string, string):
    input_list = input_string.split()
    changing_list = input_string.split()
    num_occurences = 0
    occurences = []
    for compare in input_list:
        if string == compare:
            occurences.append(changing_list.index(compare) + num_occurences)
            num_occurences = num_occurences + 1
            changing_list.remove(compare)
    return occurences

def main():
        input_string = (input("Please input a string: "))
        input_list = input_string.split()
        used = []
        for string in input_list:
                if string not in used:
                        occurences = find_occurences(input_string, string)
                        print (string + ": ", end='')
                        words_after = []
                        for num in occurences:
                            num_after = int(num) + 1
                            if num_after < len(input_list) :
                                if input_list[num_after] not in words_after:
                                    words_after.append(input_list[num_after])
                                    if occurences.index(num) > 0 :
                                        print(", " + input_list[num_after], end='')
                                    else:
                                        print(input_list[num_after], end='')
                                        used.append(string)

                        print()
main()
