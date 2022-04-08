
board = [[' ',' ',' ',' ',' ', ' '],[' ',' ',' ',' ',' ', ' '],[' ',' ',' ',' ',' ', ' '],[' ',' ',' ',' ',' ', ' '],[' ',' ',' ',' ',' ', ' '],[' ',' ',' ',' ',' ', ' '],[' ',' ',' ',' ',' ', ' ']]

# Printing board
def print_board(board):
    head = ' '
    # Printing the number
    for num in range(1, len(board)+1):
        head += ' ' + str(num) + '  '
    print(head)
    #Printing the first row
    split_row = "+---" * len(board) + '+'
    print(split_row)
    # Printing the body
    for row in range(len(board[0])):
        print("|   "*len(board) + '|')
        row_with_item = ''
        for col in range(len(board)):
            row_with_item += "| " + str(board[col][row]) + ' '
        print(row_with_item + "|")
        print("|   "*len(board) + '|')
        print(split_row)

# Available column
def available_column(board):
    col = []
    for i in range(len(board)):
        if board[i][0] == " ":
            col.append(i+1)
    return ', '.join(map(str, col))

# Checking and adding symbol to the board
def adding_piece_to_board(board, player, col):
    # Check if the entered column is the right one
    if col > 7 or col < 1:
        print('\nThe column is not exist, please pick a column between 1 and 7 \n')
        return False
    # Check if the column is full
    elif " " not in board[col-1]:
        print('\nThe column is full, please pick another column')
        return False
    # If there is nothing wrong with the input then add the symbol to the board
    else:
        for i in range(len(board[0])-1,-1, -1):
            if board[col-1][i] == " ":
                board[col-1][i] = player
                print()
                print(f'Place an {player} in the column {col}')
                print()
                return True

# Function to check if any player has won the game
def has_won(board, symbol ):
    # Check horizontally winning
    for row in range(len(board[0])):
        for col in range(len(board)-3):
            if board[col][row] == symbol and board[col+1][row] == symbol and board[col+2][row] == symbol and board[col+3][row] == symbol:
                return True
    # Check vertically winning
    for col in range(len(board)):
        for row in range(len(board[0])-3):
            if board[col][row] == symbol and board[col][row+1] == symbol and board[col][row+2] == symbol and board[col][row+3] == symbol:
                return True
    # Checking / diagonally winning
    for col in range(len(board)-3):
        for row in range(3, len(board[0])):
            if board[col][row] == symbol and board[col+1][row-1] == symbol and board[col+2][row-2] == symbol and board[col+3][row-3] == symbol:
                return True
    # Checking \ diagonally winning
    for col in range(4):
        for row in range(3):
            if board[col][row] == symbol and board[col+1][row+1] == symbol and board[col+2][row+2] == symbol and board[col+3][row+3] == symbol:
                return True
    return False

# all the block has filled up and no player win
def tie_game(board):
    count = 0
    for col in board:
        if " " not in col: 
            count += 1
    if count == 7:
        print("It is a tie game")
        return True
    return False

# Checking if either player win or they are tie and stop the game with a not True
def game_over(board):
    if has_won(board, "X"):
        print("X has won the game")
        return True
    elif has_won(board, "O"):
        print("O has won the game")
        return True
    else:
        tie_game(board)

# Start game play
def play_game():
    my_board = []
    for col in range(7):
        my_board.append([' '] * 6)
    while True:
        symbol = input("Please choose your symbol between X and O: ")
        if symbol == "X" or symbol == "O":
            break
        else:
            print("Wrong choice, please choose again")
        
    while (not game_over(my_board)):
        print_board(my_board)      
        print()
        available = available_column(my_board)
        print(f"Available column to choose: {available} \n")
        while True:
            column = int(input(f'Player with symbol {symbol}, please enter the column that you want to drop: '))
            if not adding_piece_to_board(my_board, symbol, column):
                True
            else:
                break
            
        # Switching turn
        if symbol == "X":
            symbol = "O"
        else:   
            symbol = "X"
        

play_game()
