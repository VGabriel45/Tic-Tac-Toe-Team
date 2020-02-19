import random


def init_board():

    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    return board


def get_move(user_move, board):

    valid_moves = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2',
                   'C3', 'QUIT']

    typed_move = (0, 0)
    while True:
        if user_move in valid_moves:
            if user_move.upper() == 'A1':
                typed_move = (0, 0)
            elif user_move.upper() == 'A2':
                typed_move = (0, 1)
            elif user_move.upper() == 'A3':
                typed_move = (0, 2)
            elif user_move.upper() == 'B1':
                typed_move = (1, 0)
            elif user_move.upper() == 'B2':
                typed_move = (1, 1)
            elif user_move.upper() == 'B3':
                typed_move = (1, 2)
            elif user_move.upper() == 'C1':
                typed_move = (2, 0)
            elif user_move.upper() == 'C2':
                typed_move = (2, 1)
            elif user_move.upper() == 'C3':
                typed_move = (2, 2)
            else:
                quit()

            if board[typed_move[0]][typed_move[1]] == ' ':
                return typed_move
            else:
                user_move = input(
                    'This place is occupied, please choose another one.').upper()
        else:
            user_move = input('Type a valid move: ').upper()


def mark(board, player, row, col):

    try:
        board[row][col] = player
        print(board)
        return board
    except:
        print('error')


def has_won(board, player):

    if player == board[0][0] and player == board[0][1] and player == board[0][2]:
        return True
    elif player == board[1][0] and player == board[1][1] and player == board[1][2]:
        return True
    elif player == board[2][0] and player == board[2][1] and player == board[2][2]:
        return True
    elif player == board[0][0] and player == board[1][0] and player == board[2][0]:
        return True
    elif player == board[0][1] and player == board[1][1] and player == board[2][1]:
        return True
    elif player == board[0][2] and player == board[1][2] and player == board[2][2]:
        return True
    elif player == board[0][1] and player == board[1][1] and player == board[2][2]:
        return True
    elif player == board[0][2] and player == board[1][1] and player == board[2][0]:
        return True
    else:
        return False


def print_board(board):

    print()
    print('    1   2   3')
    print()
    print('      |   |')
    print('A' + '   ' + board[0][0] + ' | ' +
          board[0][1] + ' | ' + board[0][2])
    print('      |   |')
    print('   -----------')
    print('      |   |')
    print('B' + '   ' + board[1][0] + ' | ' +
          board[1][1] + ' | ' + board[1][2])
    print('      |   |')
    print('   -----------')
    print('      |   |')
    print('C' + '   ' + board[2][0] + ' | ' +
          board[2][1] + ' | ' + board[2][2])
    print('      |   |')
    print()
    # return ' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2]


def is_full(board):
    if board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' ' and board[1][0] != ' ' and board[1][1] != ' ' and board[1][2] != ' ' and board[2][0] != ' ' and board[2][1] != ' ' and board[2][2] != ' ':
        print('It\'s a tie!')
        quit()


def get_ai_move(board, player):
    mission_accomplished = False
    for index, item in enumerate(board):
        print(item[index])
        if mission_accomplished:
            break
        for index1, item1 in enumerate(item):
            if item1 == ' ':
                board[index][index1] = player
                mission_accomplished = True
                break
    return board


def human_vs_ai():

    game_board = init_board()

    print_board(game_board)
    the_player = input('Enter X or O: ').upper()

    while the_player != '0' and the_player != 'X':
        the_player = input('Enter X or O: ').upper()

    if the_player == 'QUIT':
        quit()

    ai_is_moving = False

    while not has_won(game_board, the_player):
        # row = int(input('Row: '))
        # col = int(input('Col: '))
        if not ai_is_moving:
            position = input('Enter position: ').upper()
            move = get_move(position, game_board)

            game_board = mark(game_board, the_player, move[0], move[1])
        else:
            game_board = get_ai_move(game_board, the_player)
        print_board(game_board)
        is_full(game_board)
        if has_won(game_board, the_player):
            print(f'{the_player} WON!')
            break

        if the_player == 'X':
            print('Next enter 0')
            the_player = '0'
        else:
            print('Next enter X')
            the_player = 'X'
        ai_is_moving = not ai_is_moving


def main():
    random = [0, 1, 2, ]

    game_board = init_board()

    print_board(game_board)
    the_player = input('Enter X or O: ').upper()

    while the_player != '0' and the_player != 'X':
        the_player = input('Enter X or O: ').upper()

    if the_player == 'QUIT':
        quit()
    while not has_won(game_board, the_player):
        # row = int(input('Row: '))
        # col = int(input('Col: '))
        position = input('Enter position: ').upper()
        move = get_move(position, game_board)
        game_board = mark(game_board, the_player, move[0], move[1])
        print_board(game_board)
        is_full(game_board)
        if has_won(game_board, the_player):
            print(f'{the_player} WON!')
            break

        if the_player == 'X':
            print('Next enter 0')
            the_player = '0'
        else:
            print('Next enter X')
            the_player = 'X'


if __name__ == '__main__':
    # main()
    human_vs_ai()
