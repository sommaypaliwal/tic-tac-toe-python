from random import randrange

def display_board(board):
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   ",row[0],"   |   ",row[1],"   |   ",row[2],"   |",sep="")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    
    while True:
        try:
             move = int(input("Enter move from (1 to 9) : "))
        except ValueError:
            print("Please enter an integer : ")
            continue
        
        if move<1 or move>9:
            print("Enter valid move")
            continue

        row = (move - 1)//3
        col = (move - 1)%3

        if board[row][col] in ['X' , 'O']:
            print("Place already occupied")
            continue

        board[row][col] = 'O'
        break


def make_list_of_free_fields(board):
    free = []

    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X','O']:
                free.append((row,col))

    return free


def victory_for(board, sign):
    for row  in board:
        if row[0] == row[1] == row[2] == sign:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False
    

def draw_move(board):
    free = make_list_of_free_fields(board)

    row , col = free[randrange(len(free))]

    board[row][col] = 'X'

board = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
        ]

while True:
    
    display_board(board)

    enter_move(board)

    if victory_for(board,'O'):
        display_board(board)
        print("You won")
        break
    
    free = make_list_of_free_fields(board)
    if len(free) == 0:
        display_board(board)
        print("Match tie")
        break

    draw_move(board)

    if victory_for(board,'X'):
        display_board(board)
        print("Computer won")
        break

    free = make_list_of_free_fields(board)
    if len(free) == 0:
        display_board(board)
        print("Match tie")
        break