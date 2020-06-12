import random

def display_board(board):
    """
    The parameter board is a list that contains the X's and O's of each player
    The index of the markers corresponds to the location on the board. The 0 index is blank
    or will have a dummy value

    :param board:
    :return:
    """
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")
    display_hline()
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    display_hline()
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")


def display_hline():
    """
    displays the horizontal lines of the board for visual purposes
    :return:
    """
    for i in range(12):
        print("-", end="")
    print()


def place_marker(board, marker, position1):
    """
    Displays the board with marker and current player position
    :param board:
    :param marker:
    :param position1:
    :return:
    """
    board[position1] = marker


def check_empty_space(board, position1):
    """
    Checks to see if the current position is occupied.
    :param board:
    :param position1:
    :return: boolean if the marker at the position is " ".
    """
    return board[position1] == " "


def is_board_full(board):
    """
    Checks if the board is full method will return True
    """
    for i in range(1, 10):
        if check_empty_space(board, i):
            return False
    return True


def player_position(board, play1):
    """
    :param board:
    :param play1:
    :return: position where player wants to place the marker.
    """
    pos = 0
    while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not(check_empty_space(board, pos)):
        pos = int(input("{} please choose your position (1-9): ".format(play1)))
    return pos


def check_winner(board, marker):
    """
    Method that checks if a player has won.
    Takes in the current board and a current marker to test for a win
    """
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or   # across the top
            (board[4] == marker and board[5] == marker and board[6] == marker) or   # across the middle
            (board[1] == marker and board[2] == marker and board[3] == marker) or   # across the bottom
            (board[7] == marker and board[4] == marker and board[1] == marker) or   # down the middle
            (board[8] == marker and board[5] == marker and board[2] == marker) or   # down the middle
            (board[9] == marker and board[6] == marker and board[3] == marker) or   # down the right side
            (board[7] == marker and board[5] == marker and board[3] == marker) or   # diagonal
            (board[9] == marker and board[5] == marker and board[1] == marker))     # diagonal


def choose_starter(p1, p2):
    """
    Selects a random player to go first
    """
    names = [p1, p2]
    random.shuffle(names)
    return (names[0], names[1])


def player_marker(starter):
    """
    returns a tuple that keeps track of player1 and player2 markers (X's or O's)
    """
    markers = ""

    while markers != "X" or markers != "O":
        # The starting player selects their marker
        markers = input("{} do you want to be 'X's or 'O's?: ".format(starter)).upper()
        if markers == "X":
            return ("X","O")
        else:
            return ("O", "X")


def play_again():
    rematch = input("Do you want a rematch? (Yes or No): ")
    if rematch[0].upper() == 'Y':
        return True
    else:
        return False


if __name__ == "__main__":
    print("Welcome!"
          "Thank you for playing Tic Tac Toe")
    name1 = input("Enter your name: ")
    name2 = input("Enter the other player's name: ")
    p1, p2 = choose_starter(name1, name2)
    turn = p1

    while True:
        # initially board is empty
        game_board = [" "] * 10

        player1_marker, player2_marker = player_marker(p1)

        lets_play = input("{} and {} Are you ready to play? (Yes, No): ".format(p1, p2))

        if lets_play[0].upper() == "Y":
            play = True
        else:
            play = False

        while play:
            if turn == p1:
                print("\n"*50)
                display_board(game_board)
                position = player_position(game_board, turn)  # returns the position where marker should go
                place_marker(game_board, player1_marker, position)
                # check for a win after placing marker

                if check_winner(game_board, player1_marker):
                    print("\n"*50)
                    display_board(game_board)
                    print("Congratulations {name1}! You have won the game".format(name1 = p1))
                    play = False
                else:
                    if is_board_full(game_board):
                        print("\n"*50)
                        display_board(game_board)
                        print("Cats game")
                        break
                    else:
                        turn = p2
            else:
                # It is player 2's turn
                print("\n"*50)
                display_board(game_board)
                position = player_position(game_board, turn)
                place_marker(game_board, player2_marker, position)
                # Check fora  win after placing the marker

                if check_winner(game_board, player2_marker):
                    print("\n"*50)
                    display_board(game_board)
                    print("Congratulations {name2}! You have won the game".format(name2=p2))
                    play = False
                else:
                    if is_board_full(game_board):
                        print("\n"*50)
                        display_board(game_board)
                        print("Cats game")
                        break
                    else:
                        turn = p1
        if not play_again():
            break
    print("\n\nThank you for playing. Bye!")




