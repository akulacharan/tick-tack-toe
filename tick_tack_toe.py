# --------- Global Variables -----------
from  random import *
# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Game is still going
game_still_going = True

#winner is?
winner = None

#Who's turn is it
current_player = "Y"

def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")

def play_game():

    # Display initial board
    display_board()

    # while the game is still going
    while game_still_going:
        if current_player != "Y":
            while True:
                num = randint(1, 9)
                pos = str(num)
                if board[num - 1] != "-":
                    continue
                elif pos in board:
                    continue
                else:
                    print("Bot choice is:", num)
                    board[num - 1] = "M"
                    print(display_board())
                    break
        else:
            # handle a single turn of an arbitrary player
            handle_turn(current_player)

        #Check if gameover
        check_if_game_over()

        #flip to the other player
        flip_player()

        # The game has ended
        if winner == "Y" or winner == "M":
            print(winner, "Won.")
        elif winner == None:
            pass
            # or use print("tie") in a rare case



# handle a single turn of an arbitrary player
def handle_turn(player):
    print(player + "'s turn.")
    position = input("choose a number from 1-9: ")

    valid  = False
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Invalid input - choose a number from 1-9:")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there Again!!")

    board[position] = player

    display_board()



def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # Set global variables
    global winner

    # Check if there was a winner anywhere
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    #setup global b=variable
    global game_still_going

    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    #return the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return

def check_columns():
    # setup global b=variable
    global game_still_going

    # Check if any of the rows have all the same value (and is not empty)
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    # If any cols does have a match, flag that there is a win
    if col_1 or col_2 or col_3:
        game_still_going = False

    # return the winner X or O
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return

def check_diagonals():
    # setup global b=variable
    global game_still_going

    # Check if any of the diagonals have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"


    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # return the winner X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return



def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    #global variable
    global current_player
    # If the current player was X, make it O
    if current_player == "Y":
        current_player = 'M'
    # If the current player was O, make it X
    elif current_player == "M":
        current_player = "Y"
    return



play_game()