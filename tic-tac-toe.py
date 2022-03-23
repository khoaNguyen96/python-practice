     # Creating a board with the size of player choice
from asyncio import create_subprocess_shell
from re import X
from tabnanny import check


def create_board(board_size):
    board = [[' '] * int(board_size) for col in range(int(board_size))]
    return board
    
    # Function to print the board to the terminal
def print_board(board):
    head = '   '
    # Printing the column number
    for num in range(1, len(board)+1):
        head += ' ' + str(num) + '  '
    print(head)
    #Printing the first row
    split_row = "  " + "+---" * len(board) + '+'
    print(split_row)
    # Printing the body
    for row in range(len(board)):
        row_with_item = str(row+1) + ' '
        for col in range(len(board)):
            row_with_item += "| " + str(board[col][row]) + ' '
        print(row_with_item + "|")
        print(split_row)

    # Check if the player win 
def has_won(board, symbol):
        # Vertically win |
    for col in range(len(board)):
        for row in range(len(board)-2):
            if board[col][row] == symbol and board[col][row+1] == symbol and board[col][row+2] == symbol:
                return True
        # Horizontally win -
    for row in range(len(board)):
        for col in range(len(board)-2):
            if board[col][row] == symbol and board[col+1][row] == symbol and board[col+2][row] == symbol:
                return True
        # Diagonally \ win 
    for col in range(len(board)-2):
        for row in range(len(board)-2):
            if board[col][row] == symbol and board[col+1][row+1] == symbol and board[col+2][row+2] == symbol:
                return True
        # Diagonally / win
    for col in range(len(board)-2):
        for row in range(2, len(board)):
            if board[col][row] == symbol and board[col+1][row-1] == symbol and board[col+2][row-2] == symbol:
                return True
    return False

    # Function to check if the box is out of move and there is a tie
def tie_game(board):
    for col in board:
        if " " not in col:
            print("Oops, there is no move left so it is a Tie-Game")
            return True
        else:
            return False

    # Checking if the game is over then stop the game
def game_over(board):
    if has_won(board, "X"):
        print("X player has won the game")
        return True
    elif has_won(board, "O"):
        print("O player has won the game")
        return True
    else: 
        tie_game(board)

    # Function to check if the box has been tick before.
def check_marked(board, col, row):
    if board[col-1][row-1] == 'X' or board[col-1][row-1] == "O":
        return True
    else:
        return False

        
    # Function to run the game
def play_game():
    players = ["X", "O"]
    print("""           ****  WELCOME TO TIC-TAC-TOE  ****
-> This game will allow you to choose how big is the board you want to play with
---> Each player will choose your symbol between 'X' and 'O' to play the game.
-----> The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner 
-------> The game is starting now and remember to have fun""")
    while True:
        board_size = input("\nPlease choose the size of the board (Ex: 3x3 will be 3, 4x4 will be 4,...): ")
        my_board = create_board(board_size)
        print_board(my_board)
        print()
        answer = input("Is this the board size you want to choose or do you want to have different size [Y (yes)/ N (no)]: ")
        if answer != 'Y' and answer != 'N':
            print("\nWrong answer, please type Y for yes or N for no.\n")
            answer = input("Is this the board size you want to choose or do you want to have different size [Y (yes)/ N (no)]: ")
            if answer == "N":
                True
            else:
                break
        if answer == "N":
            True
        else:
            break
    player = input("\nFirst player please choose X or O: ")
    while (player != 'X' and player != 'O'):
        print("\nWrong input, please choose again.\n")
        player = input("Please choose again between X or O: ")
    print(f"Second player will be: {players[1-players.index(player)]}\n")
    while not game_over(my_board):
        while True:
            print(f"{player}'s player turn:")
            col = int(input("->Please enter what column number do you want to mark in: "))
            row = int(input("->Please enter what row number do you want to mark in: "))
            if check_marked(my_board,col,row):
                print(f"\nSorry, the {players[1-players.index(player)]} player has marked there. Please choose another spot.\n")
                True
            else:
                break
        my_board[col-1][row-1] = player
        print()
        print_board(my_board)
        print()
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
play_game()