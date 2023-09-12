import csv
import doctest

def print_board(board, c):
    
    """
    print a c*c array
    """
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    output = ''
    for i in range(c):
        print('   ', i+1, end='')
    output += "\n"+' '+'─────'*c
    output += ('\n')
    for i in range(c):
        output += (rows[i] + '║')
        output += ('  ')
        for j in range(c):
            if board[i][j] == '0':
                output += ('  │  ')
            else:
                output += (board[i][j]+" │  ")
        output += ('\n')
    output += (' '+'─────'*c)
    print(output)


def is_valid_location(board, col, row1):
    """
    check whether or not the selected column is full 
    """
    return board[row1][col] == '0'


def get_next_open_row(board, col):
    """
    search for the first available row
    """
    for r in range(c):
        if board[r][col] != '0':
            return r-1
    return c-1


def drop_piece(board, c, col, piece):
    """
    place the piece in the desired position
    """
    board[c][col] = piece


def winning_move(board):
    """
    check if there is a win in one of the four cases (horizontally, vertically, diagonally) and return a tuple
    with the winning piece, the row, the column and the win case
    """
    results = False
    tup = ('pppp',)
    # check horizontally
    for i in range(c):
        for j in range(c-3):
            if board[i][j] != '0' and board[i][j+1] == board[i][j] and board[i][j+2] == board[i][j] and board[i][j+3] == board[i][j]:
                tup2 = (board[i][j], i, j, 1)
                tup = tuple(tup2)
                board[i][j], board[i][j+1], board[i][j + 2], board[i][j+3] = "*", "*", "*", "*"

    # check verticaly
    for i in range(c-3):
        for j in range(c):
            if board[i][j] != '0' and board[i+1][j] == board[i][j] and board[i+2][j] == board[i][j] and board[i+3][j] == board[i][j]:
                tup2 = (board[i][j], i, j, 2)
                tup = tuple(tup2)
                board[i][j], board[i+1][j], board[i +2][j], board[i+3][j] = "*", "*", "*", "*"

    # check diagonally up
    for i in range(3, c):
        for j in range(c-3):
            if board[i][j] != '0' and board[i-1][j+1] == board[i][j] and board[i-2][j+2] == board[i][j] and board[i-3][j+3] == board[i][j]:
                tup2 = (board[i][j], i, j, 3)
                tup = tuple(tup2)
                board[i][j], board[i-1][j+1], board[i-2][j + 2], board[i-3][j+3] = "*", "*", "*", "*"

    # check diagonally down
    for i in range(c-3):
        for j in range(c-3):
            if board[i][j] != '0' and board[i+1][j+1] == board[i][j] and board[i+2][j+2] == board[i][j] and board[i+3][j+3] == board[i][j]:
                tup2 = (board[i][j], i, j, 4)
                tup = tuple(tup2)
                board[i][j], board[i+1][j+1], board[i+2][j +2], board[i+3][j+3] = "*", "*", "*", "*"

    return tup


def load_game():
    """
    save the array to a csv file
    """
    global board
    global score1
    global score2
    global c

    board = []
    
    filename = input('File name: ').strip()
    with open(f'{filename}', 'r') as file:
        tupder = csv.tupder(file)
        for row in tupder:
            board.append(row)

    score2 = (board.pop(-1))
    score1 = (board.pop(-1))
    score1 = int(score1[0])
    score2 = int(score2[0])

    c = len(board)
    for i in range(c):
        for j in range(c):
            copy_board = int(board[i][j])
            if copy_board == 0:
                board[i][j] = '0'
            elif copy_board == 1:
                board[i][j] ='X'
            elif copy_board == 2:
                board[i][j] = 'O'




# MAIN BODY

print('Welcome!')
decision = input('Start new game (N) or load game from file (S)?')


if decision == 'N' or decision == "n":
    ls = []
    board = []
    c = int(input("Choose number of columns (5-10): "))

    while c < 5 or c > 10:
        print('Option is out of bounds. Try again (5-10).')
        c = int(input("Number of columns: "))

    for i in range(c):
        ls.append([])
        for j in range(c):
            ls[i].append("0")

    board += ls

    print_board(board, c)



    score1, score2 = 0, 0
elif decision == 'S' or decision == 's':
    load_game()
    print_board(board, c)

row1 = 0
turn = 0

game_over = False


while not game_over:

    full_board = True
    for i in range(c):
        if board[0][i] == '0':
            full_board = False
            break

    if full_board == True:
        print('The board is full. Game over.')
        game_over = True
        break

# player 1
    if turn == 0:
        b = False
        while b == False:
            col = int(input("Player 1 choose a position: "))
            while col > c and col<=0:
                print("That's impossible.")
                col = int(input("Try again:"))
            if is_valid_location(board, col-1, row1):
                row = get_next_open_row(board, col-1)
                drop_piece(board, row, col-1, "X")
                b = True
            else:
                print('Occupied position.')

# player 2
    else:
        b = False
        while b == False:
            col = int(input("Player 2 choose a position: "))
            while col > c and col<=0:
                print("That's impossible.")
                col = int(input("Try again:"))
            if is_valid_location(board, col-1, row1):
                row = get_next_open_row(board, col-1)
                drop_piece(board, row, col-1, "O")
                b = True
            else:
                print('Occupied position.')

    print_board(board, c)
    details = winning_move(board)
    if details[0] != 'X':
        winning_move(board)

    for i in range(c):
        for j in range(c):
            if board[i][j] == '*':
                print_board(board, c)
                break
        if board[i][j] == '*':
            break

    if len(details) > 1:

        if details[0] == 'X':
            score1 += 1
            print('Player 1 won!!!')
        elif details[0] == 'O':
            score2 += 1
            print('Player 2 won!!!')
        print('The score is ', score1, '-', score2)

        if details[3] == 1:
            if details[2] == c-4:
                g = 4
            else:
                g = 5
            for i in range(details[2], details[2]+g):
                for m in range(c - details[1]+1):
                    board[details[1]-m][i] = board[details[1]-(m+1)][i]
            for i in range(details[2]+g):
                board[0][i] = '0'

        elif details[3] == 2:
            for i in range(details[1]+4):
                board[i][details[2]] = '0'

        elif details[3] == 3:
            if details[2] == c-4:
                g = 4
            else:
                g = 5
            m = 0
            for j in range(details[2], details[2]+g):
                for i in range(details[1]-m, 0, -1):
                    board[i][j] = board[i-1][j]
                board[0][j] = '0'
                m += 1

        elif details[3] == 4:
            if details[2] == c-4:
                g = 4
            else:
                g = 5
            m = 0
            for j in range(details[2], details[2]+g):
                for i in range(details[1]+m, 0, -1):
                    board[i][j] = board[i-1][j]
                board[0][j] = '0'
                if m < 3:
                    m += 1

    turn += 1

    turn = turn % 2
    if turn==0:
        print('Press enter to continue.','\n','To pause the game and save it to a file type "S":')
        cont = input()
        if cont == 'S' or cont == "s":
            for i in range(c):
                for j in range(c):
                    copy_board = board[i][j]
                    if copy_board == '0':
                        board[i][j] = 0
                    elif copy_board == 'X':
                        board[i][j] = 1
                    else:
                        board[i][j] = 2
            
            board.append(str(score1))
            board.append(str(score2))

            filename = input('File name: ').strip()
            with open(f'{filename}', 'w', newline= '') as file:
                writer = csv.writer(file)
                for i in range(c+2):
                    writer.writerow(board[i])
            break