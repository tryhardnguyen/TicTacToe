def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    is_entering = True
    while is_entering:
        team = input("Choose between 'X' or 'O'\n")
        if team.lower() == 'x' or team.lower() == 'o':
            return team
        else:
            print("Sorry, that an invalid input. Please try again")


def place_marker(board, marker, position):
    board[position] = marker
    return board


# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
    if mark == board[7] == board[8] == board[9]:
        return True
    elif mark == board[4] == board[5] == board[6]:
        return True
    elif mark == board[1] == board[2] == board[3]:
        return True
    # Diagonals
    elif mark == board[1] == board[5] == board[9]:
        return True
    elif mark == board[3] == board[5] == board[7]:
        return True
    # Vertical
    elif mark == board[1] == board[4] == board[7]:
        return True
    elif mark == board[2] == board[5] == board[8]:
        return True
    elif mark == board[3] == board[6] == board[9]:
        return True


# Write a function that uses the random module to randomly decide which player goes first.
import random


def goes_first():
    x = 1
    o = 2
    first = random.randint(1, 2)
    if first == x:
        return 'x'
    elif first == o:
        return 'o'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        # space_check = true represent empty space
        if space_check(board, i):
            # Return False because we still have an empty space
            return False
    return True


def next_turn(board, second):
    next_position = int(input(f"{second}, Enter your position from 1-9\n"))
    if space_check(board, next_position):
        return next_position


def replay():
    play_again = input("Enter 'Y' if you want play again, Enter 'N' to exit \n")
    return play_again.lower() == 'y'


def start_game():
    is_on = True
    while is_on:
        board = [" "] * 10
        print("Welcome to Tic Tac Toe!")
        display_board(board)

        player_input()

        # Determine who goes first
        first_player = None
        second_player = None
        first = goes_first()
        if first.lower() == "x":
            first_player = "x"
            second_player = "o"
        elif first.lower() == "o":
            first_player = "o"
            second_player = "x"
        print(f"{first_player} goes first\n")
        while not full_board_check(board):
            # Whoever get first, make the first move, return a position
            position = int(input(f"{first_player} turn, Choose a position (1-9) \n"))
            if space_check(board, position):
                place_marker(board, first_player, position)
                display_board(board)
                # Whoever get first, make the first move, return a position
                if win_check(board, first_player):
                    print(f"{first_player} wins!")
                    break
                elif win_check(board, second_player):
                    print(f"{second_player} wins!")
                    break
                place_marker(board, second_player, next_turn(board, second_player))
                display_board(board)
        print("Tied Game")
        display_board(board)
        if replay():
            start_game()
        else:
            is_on = False


# Calling the game
start_game()
