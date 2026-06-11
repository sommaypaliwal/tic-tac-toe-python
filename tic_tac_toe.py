from random import randrange

def display_board(board):
    for i in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   ",i[0],"   ","|   ",i[1],"   ","|   ",i[2],"   |",sep="")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    while True:
        try:
            move = int(input("Enter move from (1 to 9) : "))
        except ValueError:
            print("Please enter an integer")
            continue
    
        if move < 1 or move > 9:
            print("Please enter valid integer")
            continue

        row = (move - 1)//3
        col = (move - 1)%3

        if board[row][col] in ['X' , 'O']:
            print("Place already occupied ")
            continue
        
        board[row][col] = user_symbol
        break
    

def make_list_of_free(board):
    free = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X' , 'O']:
               free.append((i,j))
    return free

def is_victory_for(board , sign):
    for i in board:
        if i[0] == i[1] == i[2] == sign:
            return True
    for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] == sign:
                return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    
    return False

def make_computer_move(board):
    free = make_list_of_free(board)
    
    row , col = free[randrange(len(free))]
    
    board[row][col] = computer_symbol

board = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
         ]

print("Please select a symbol : ")
while  True:
    try:
        symbol = int(input("Press 1 for X and 2 for O : "))
    except ValueError:
        print("Please enter an integer. 1 or 2.")
        continue

    if symbol < 1 or symbol > 2:
        print("Please enter 1 or 2.")
        continue

    symbol_list = ["X", "O"]

    user_symbol = symbol_list[symbol - 1]

    if user_symbol == "X":
       computer_symbol = "O"
    else:
       computer_symbol = "X"

    break


while True:

    display_board(board)

    enter_move(board)

    if is_victory_for(board , user_symbol):
        display_board(board)
        print("You won")
        break

    free = make_list_of_free(board)
    if len(free) == 0:
        display_board(board)
        print("Match Tie ")
        break

    make_computer_move(board)

    if is_victory_for(board , computer_symbol):
        display_board(board)
        print("Computer won")
        break

    free = make_list_of_free(board)
    if len(free) == 0:
        display_board(board)
        print("Match Tie ")
        break
