import time
from random import randint


def board(play_board: list):  # designing the visualization of tic-tac-toe board
    print('''
    +-------+-------+-------+           
    |   {}   |   {}   |   {}   |
    +-------+-------+-------+ 
    |   {}   |   {}   |   {}   |
    +-------+-------+-------+ 
    |   {}   |   {}   |   {}   |
    +-------+-------+-------+     
    '''.format(play_board[0][0],
               play_board[0][1],
               play_board[0][2],
               play_board[1][0],
               play_board[1][1],
               play_board[1][2],
               play_board[2][0],
               play_board[2][1],
               play_board[2][2],
               ))


def update_board(player, n):                        # row eq = (n-1)//3     col eq = (n%3) - 1   this is the derivation
    global set_board                                # Number    set_board[row][col]     row match       col-match
                                                    #   1               [0][0]              1-0             1-0
    if player == 'user':                            #   2               [0][1]              2-0             2-1
        set_board[(n - 1) // 3][(n % 3) - 1] = 'O'  #   3               [0][2]              3-0             3-2
    elif player == 'com':                           #   4               [1][0]              4-1             4-0
        set_board[(n - 1) // 3][(n % 3) - 1] = 'X'  #   5               [1][1]              5-1             5-1
                                                    #   6               [1][2]              6-1             6-2
    return board(set_board)                         #   7               [2][0]              7-2             7-0
                                                    #   8               [2][1]              8-2             8-1
                                                    #   9               [2][2]              9-2             9-2
def user_win() -> bool:
    if set_board[0] == ['O', 'O', 'O'] or \
            set_board[1] == ['O', 'O', 'O'] or \
            set_board[2] == ['O', 'O', 'O'] or \
            (set_board[0][0] == 'O' and set_board[1][0] == 'O' and set_board[2][0] == 'O') or \
            (set_board[0][1] == 'O' and set_board[1][1] == 'O' and set_board[2][1] == 'O') or \
            (set_board[0][2] == 'O' and set_board[1][2] == 'O' and set_board[2][2] == 'O') or \
            (set_board[0][0] == 'O' and set_board[1][1] == 'O' and set_board[2][2] == 'O') or \
            (set_board[0][2] == 'O' and set_board[1][1] == 'O' and set_board[2][0] == 'O'):
        return True     # Eight conditions when user wins
    else:
        return False


def com_win() -> bool:
    if set_board[0] == ['X', 'X', 'X'] or \
            set_board[1] == ['X', 'X', 'X'] or \
            set_board[2] == ['X', 'X', 'X'] or \
            (set_board[0][0] == 'X' and set_board[1][0] == 'X' and set_board[2][0] == 'X') or \
            (set_board[0][1] == 'X' and set_board[1][1] == 'X' and set_board[2][1] == 'X') or \
            (set_board[0][2] == 'X' and set_board[1][2] == 'X' and set_board[2][2] == 'X') or \
            (set_board[0][0] == 'X' and set_board[1][1] == 'X' and set_board[2][2] == 'X') or \
            (set_board[0][2] == 'X' and set_board[1][1] == 'X' and set_board[2][0] == 'X'):
        return True     # Eight conditions when com wins
    else:
        return False


def set_board_single():         # converting 3x3 array to 1X1 list containing all the items
    global set_board_sing       # the purpose is to be the reference for checking the remaining available boxes
    set_board_sing = []
    for i in range(3):
        for j in range(3):
            set_board_sing.append(set_board[i][j])


def play(answer):
    if answer == 'Y':
        return True
    elif answer == 'N':
        return False
    else:
        return None


def reset_board():  # to reset the board after a single game is complete
    global set_board
    set_board = [[1, 2, 3],
                 [4, 'X', 6],
                 [7, 8, 9]
                 ]


print('''
    Welcome to the classic tic-tac-toe game
    You will play against the computer
    You will go with the 'O'
    While the computer goes with the 'X'
    Make your move by entering the number of box you choose 
    
    Here the computer goes first ...
''')

time.sleep(8)

reset_board()
board(set_board)

play('Y')

while play:
    for i in range(4):

        set_board_single()      # the updated set_board is converted to 1x1 list before user's turn

        try:
            user_choice = int(input('Enter your choice '))
        except ValueError:
            print('You are not entering a valid number')

        while user_choice not in set_board_sing:    # checking whether the user's picking a chosen box
            user_choice = int(input('Either the box has been picked or your choice is out of range. Try again! '))

        update_board('user', user_choice)

        if user_win():
            print('Congratulation! You Win')
            break

        print('computer\'s turn ...')
        time.sleep(3)

        set_board_single()      # the set_board is converted to 1x1 list again before com's turn

        com_choice = randint(1, 10)
        while com_choice not in set_board_sing: # checking whether computer's picking a chosen box
            com_choice = randint(1, 10)

        update_board('com', com_choice)

        if com_win():
            print('You Lose! Better Luck next time')
            break
    else:
        print("It's a Tie")

    reset_board()
    play_again = input('Do you want to play again? Y/N ')

    if play_again == 'Y':
        board(set_board)
    elif play_again == 'N':
        print('Thanks for playing')
        break

    play(play_again)
