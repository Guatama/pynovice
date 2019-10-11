__author__ = 'Flatline01'
__version__ = '1.0.0'

import os
import platform

testGame = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
newGame = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def clear_screen(JupyterNotebook=False):
    """
        Clear screen in terminal. With JupyerNotebook == True - did it for that enviroment with IPython function
    """
    if JupyterNotebook:
        from IPython.display import clear_output
        clear_output()

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def board_display(board):
    """
        Displaying board-grid and markers in places in term
    """
    spaces = " " * 10
    line_space = spaces + "    |   |    "
    line_horiz = spaces + "—" * 13

    clear_screen()
    print("\n\n")
    print("{}\n{} {} | {} | {} ".format(line_space, spaces, board[1], board[2], board[3]))
    print("{}\n{}".format(line_space, line_horiz))
    print("{}\n{} {} | {} | {} ".format(line_space, spaces, board[1], board[2], board[3]))
    print("{}\n{}".format(line_space, line_horiz))
    print("{}\n{} {} | {} | {} ".format(line_space, spaces, board[1], board[2], board[3]))


    # print(line_space + "\n" + spaces + " " + board[1] + "  | " + board[2] + " | " + board[3] + " ")     # 1 line
    # print(line_space + "\n" + line_horiz)
    # print(line_space + "\n" + spaces + " " + board[4] + "  | " + board[5] + " | " + board[6] + " ")     # 2 line
    # print(line_space + "\n" + line_horiz)
    # print(line_space + "\n" + spaces + " " + board[7] + "  | " + board[8] + " | " + board[9] + " ")     # 3 line
    print(line_space + "\n" * 5)


def place_marker(board, marker, position):
    """
        Placing marker in postion on the board
    """
    board[position] = marker


def space_check(board, position):
    """
        Checking - where a space on the board is freely available
    """
    return board[position] == ' '


def full_board_check(board):
    """
        Checking - if the board is a full and returns a boolean valie. True = full, False - otherwise
    """
    count = 0
    for item in range(1, 10):
        if board[item] != ' ':
            count += 1
    return count == 9


def win_check(board, marker):
    """
        Checking - in each move, do someone win
    """
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
           (board[4] == marker and board[5] == marker and board[6] == marker) or
           (board[7] == marker and board[8] == marker and board[9] == marker) or
           (board[1] == marker and board[4] == marker and board[7] == marker) or
           (board[2] == marker and board[5] == marker and board[8] == marker) or
           (board[3] == marker and board[6] == marker and board[9] == marker) or
           (board[1] == marker and board[5] == marker and board[9] == marker) or
           (board[3] == marker and board[5] == marker and board[7] == marker))


def draw_check(board, marker_1, marker_2):
    """
        Checking - if we have draw situation
    """
    if full_board_check(board) and not win_check(board, marker_1) and not win_check(board, marker_2):
        print("\nThe game is a draw.\n")
        return True
    return False


def choose_first():
    """
        Randomly choose, which player will be first
    """
    from random import randint
    first_player = randint(0, 1)
    if first_player == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def dialog_YN(question):
    """
        Func for questions with bool answer. Return TRUE if Yes, and FALSE if No
    """
    list_of_answer = ['y', 'yes', 'n', 'no']
    answer = ''
    while answer not in list_of_answer:
        answer = input(question).lower()  
        if answer == list_of_answer[0] or answer == list_of_answer[1]:
            bool_answer = True
        elif answer == list_of_answer[2] or answer == list_of_answer[3]:
            bool_answer = False
        else:
            continue
    return bool_answer


def player_input():
    """
        Input function - move of players (markers - X or O, and place in range from 1 to 9)
    """
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?  ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def player_choice(board):
    """
        It's ask user to input position of his move and return that position
    """
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        try:
            position = int(input("Choose your next position (1 - 9): "))
        except Exception:
            continue
    return position


def replay():
    """
        Replay
    """
    return dialog_YN("Do you want to play again? Enter YES or NO -  ")


def start_game(board):
    """
        Main game loop
    """
    clear_screen()
    print("\n\n-----Welcome to Tic Tac Toe!------")
    print("--------------ver 1.0------------")
    print("=" * 40)

    while True:
        theBoard = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print("\n\n" + turn + " will go first.")

        # TODO do alter function for replay.
        # All YES and NO questions with question(str) --> str + Y/N and Bool
        game_on = dialog_YN("Are you ready to play? Enter YES or NO -  ")

        while game_on:
            if turn == 'Player 1':
                board_display(theBoard)
                print("Player 1 move.")
                move = player_choice(theBoard)
                place_marker(theBoard, player1_marker, move)
                if win_check(theBoard, player1_marker):
                    board_display(theBoard)
                    print("\nCongratulations! Player 1 win!")
                    break
                if draw_check(theBoard, player1_marker, player2_marker):
                    break
                turn = 'Player 2'

            else:
                board_display(theBoard)
                print("Player 2 move.")
                move = player_choice(theBoard)
                place_marker(theBoard, player2_marker, move)
                if win_check(theBoard, player2_marker):
                    board_display(theBoard)
                    print("\nCongratulations! Player 2 win!")
                    break
                if draw_check(theBoard, player1_marker, player2_marker):
                    break
                turn = 'Player 1'
        if not replay():
            break


if __name__ == '__main__':
    start_game(newGame)
