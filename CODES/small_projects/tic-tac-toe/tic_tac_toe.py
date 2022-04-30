import time
# not a complete game
board = {'topL': ' ', 'topM': ' ', 'topR': ' ',
         'midL': ' ', 'midM': ' ', 'midR': ' ',
         'lowL': ' ', 'lowM': ' ', 'lowR': ' '}

moves = {1: 'topL', 2: 'topM', 3: 'topR',
         4: 'midL', 5: 'midM', 6: 'midR',
         7: 'lowL', 8: 'lowM', 9: 'lowR'}


def toPlay():
    print("NOTE: OPEN CONSOLE TO FULL LENGTH taaki sab msg dikhe...")
    time.sleep(2)
    print("TIC TAC TOE")
    print("Player 1:  X")
    print("Player 2:  O")
    print("Press following number to make your move in that block!")
    print(' ' + '1' + ' | ' + '2' + ' | ' + '3' + ' ')
    print('---' + '|---|' + '---')
    print(' ' + '4' + ' | ' + '5' + ' | ' + '6' + ' ')
    print('---' + '|---|' + '---')
    print(' ' + '7' + ' | ' + '8' + ' | ' + '9' + ' ')
    print()
    time.sleep(4)
    print('Game starting in 3 seconds', end='')
    for i in range(3):
        print('.', end='')
        time.sleep(1)
    print()


def print_board():
    print(' ' + board['topL'] + ' | ' + board['topM'] + ' | ' + board['topR'] + ' ')
    print('---' + '|---|' + '---')
    print(' ' + board['midL'] + ' | ' + board['midM'] + ' | ' + board['midR'] + ' ')
    print('---' + '|---|' + '---')
    print(' ' + board['lowL'] + ' | ' + board['lowM'] + ' | ' + board['lowR'] + ' ')


toPlay()
player = 1
turn = "X"
try:
    for i in range(9):
        print_board()
        print("Player 1:  X")
        print("Player 2:  O")
        move = int(input(f"Enter move (Player {player}): "))
        board[moves[move]] = turn
        if turn == 'X':
            turn = 'O'
            player = 2
        else:
            turn = "X"
            player = 1
except ValueError:
    print("DON'T PRESS X/O!!!\nYou should enter number between 1 to 9 to make a move")