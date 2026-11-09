# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 9 Assignment 3

def print_board(board):
    border = '-' * (2 * len(board) + 1)
    print(border)

    for row in board:
        print("|" + "|" .join(row) + "|")
        print(border)

board1_list = [['*','*','*'],
               ['*','+','*'],
               ['*','*','*']]
print_board(board1_list)
print() #just for a spacer line
board2_list = [['*',' ',' ','*'],
               ['*',' ',' ','*'],
               ['*',' ',' ','*'],
               ['*',' ',' ','*']]
print_board(board2_list)
print() #just for a spacer line
board3_list = [['*',' ','*',' ','*'],
               [' ','*',' ','*',' '],
               [' ',' ',' ',' ',' '],
               [' ','+',' ','+',' '],
               ['+',' ','+',' ','+']]
print_board(board3_list)