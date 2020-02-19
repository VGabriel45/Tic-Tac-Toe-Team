def init_board():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    return board


def get_move(user_move, board):
    valid_moves = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    # user = input('Type a move: ')
    while user_move not in valid_moves:
        user_move = input('Type a valid move: ')
    if user_move == 'A1':
        return (0, 0)
    elif user_move == 'A2':
        return (0, 1)
    elif user_move == 'A3':
        return (0, 2)
    elif user_move == 'B1':
        return (1, 0)
    elif user_move == 'B2':
        return (1, 1)
    elif user_move == 'B3':
        return (1, 2)
    elif user_move == 'C1':
        return (2, 0)
    elif user_move == 'C2':
        return (2, 1)
    elif user_move == 'C3':
        return (2, 2)
    else:
        return 'error'


def mark(board, player, row, col):
    # while board[row][col] != ' ':
    #     print('You already have an element in this position')
    #     return 'You already have an element in this position'
    board[row][col] = player
    print(board)
    return board


def has_won(board, player):
    if player == board[0][0] and player == board[0][1] and player == board[0][2]:
        return True
        return (f'{player} WON!')
    elif player == board[1][0] and player == board[1][1] and player == board[1][2]:
        return True
        print(f'{player} WON!')
    elif player == board[2][0] and player == board[2][1] and player == board[2][2]:
        return True
        print(f'{player} WON!')
    elif player == board[0][0] and player == board[1][0] and player == board[2][0]:
        return True
        print(f'{player} WON!')
    elif player == board[0][1] and player == board[1][1] and player == board[2][1]:
        return True
        print(f'{player} WON!')
    elif player == board[0][2] and player == board[1][2] and player == board[2][2]:
        return True
        print(f'{player} WON!')
    elif player == board[0][0] and player == board[1][1] and player == board[2][2]:
        return True
        print(f'{player} WON!')
    elif player == board[0][2] and player == board[1][1] and player == board[2][0]:
        return True
        print(f'{player} WON!')
    else:
        return False


def print_board(board):
    print()
    print(' 1   2   3')
    print()
    print('   |   |')
    print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])
    print('   |   |')
    print()
    return ' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2]


def is_full(board):
    if board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' ' and board[1][0] != ' ' and board[1][1] != ' ' and board[1][2] != ' ' and board[2][0] != ' ' and board[2][1] != ' ' and board[2][2] != ' ':
        print('It\'s a tie!')
        exit()


def print_result(player):
    return f'{player} has won!'


def main():
    game_board = init_board()

    print_board(game_board)
    the_player = input('Enter X or O: ')

    while len(the_player) > 1:
        print('Player must be X or 0 !')
        the_player = input('Enter X or O: ')
    if the_player == 'quit':
        quit()
    while not has_won(game_board, the_player):
        # row = int(input('Row: '))
        # col = int(input('Col: '))
        position = input('Enter position: ')
        move = get_move(position, game_board)
        game_board = mark(game_board, the_player, move[0], move[1])
        print_board(game_board)
        is_full(game_board)
        game_board = init_board()

        if has_won(game_board, the_player):
            print(print_result(the_player))
            break

        # board=mark(board, player, row, col)
        if the_player == 'X':
            print('Next enter 0')
            the_player = '0'
        else:
            print('Next enter X')
            the_player = 'X'


if __name__ == '__main__':
    main()
