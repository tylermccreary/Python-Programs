# connect_four.py
# A program to play the game Connect Four with two players.
# Author: Tyler McCreary

import math

#checks to see if someone won vertically
def check_vertical(board):
    #keeps track of how many in a row
    count = 1
    for col in range(8):
        for row in range(8):
            if row + 1 < 8:
                if board[row][col] != ".":
                    if board[row][col] == board[row + 1][col]:
                        count = count + 1
                    else:
                        count = 1
                    if count > 3:
                        return board[row][col]
                else:
                    count = 1
            else:
                count = 1
    return "None"

#checks to see if someone won horizontally
def check_horizontal(board):
    count = 1
    for row in range(8):
        for col in range(8):
            if col + 1 < 8:
                if board[row][col] != ".":
                    if board[row][col] == board[row][col + 1]:
                        count = count + 1
                    else:
                        count = 1
                    if count > 3:
                        return board[row][col]
                else:
                    count = 1
            else:
                count = 1
    return "None"


def check_diagonal(board):
    count = 1
    for row in range(8):
        for col in range(8):
            current_row = row
            current_col = col
            going = True
            while going:
                if current_row + 1 < 8 and current_col + 1 < 8:
                    if board[current_row][current_col] != ".":
                        if board[current_row][current_col] == board[current_row + 1][current_col + 1]:
                            count = count + 1
                            current_row = current_row + 1
                            current_col = current_col + 1
                        else:
                            count = 1
                            going = False
                        if count > 3:
                            return board[row][col]
                    else:
                        count = 1
                        going = False
                else:
                    count = 1
                    going = False

    
    #check going up and left from each spot
    #This is basically the same as above. Just goes the other direction
            current_row = row
            current_col = col
            going = True
            while going:
                if current_row + 1 < 8 and current_col - 1 > 0:
                    if board[current_row][current_col] != ".":
                        if board[current_row][current_col] == board[current_row + 1][current_col - 1]:
                            count = count + 1
                            current_row = current_row + 1
                            current_col = current_col - 1
                        else:
                            count = 1
                            going = False
                        if count > 3:
                            return board[row][col]
                    else:
                        count = 1
                        going = False
                else:
                    count = 1
                    going = False
    return "None"
    
#check for a winner
def check_winner(board):
    result = check_vertical(board)
    if result == "None":
        result = check_horizontal(board)
    if result == "None":
        result = check_diagonal(board)
    return result

#Print the board
def print_board(board):
    for row in range(7, -1, -1):
        for col in range(8):
            print(board[row][col], end = " ")
        print()

#play connect four
def main():
    board = [["." for x in range(8)] for x in range(8)]
    player_1 = True
    done = False
    while not done:
        valid = False
        while not valid:
            if player_1:
                column = int(input("Player 1 move? ")) - 1
            else:
                column = int(input("Player 2 move? ")) - 1
            if column < 8 and column > -1:
                for i in range(8):
                    if board[i][column] == ".":
                        valid = True
            if not valid:
                print("Error. The column must be between 1 and 8, and the column must have at least one empty space.")            

        #each row
        for i in range(8):
            if board[i][column] == ".":
                if player_1:
                    board[i][column] = "X"
                else:
                    board[i][column] = "O"
                break
        print_board(board)

        #look for winner
        result = check_winner(board)
        if result == "X":
            print("Player 1 wins!")
            done = True
        elif result == "O":
            print("Player 2 wins!")
            done = True
        player_1 = not player_1
main()
                
