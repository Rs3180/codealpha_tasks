from random import randrange

def display_board(board):
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")

def enter_move(board):
    ok = False
    while not ok:
        move = input("Enter your move (1-9): ")
        ok = len(move) == 1 and move >= '1' and move <= '9'
        if not ok:
            print("Bad move - repeat your input!")
            continue
        move = int(move) - 1
        row = move // 3
        col = move % 3
        sign = board[row][col]
        ok = sign not in ['O','X']
        if not ok:
            print("Field already occupied - repeat your input!")
            continue
    board[row][col] = 'O'

def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O','X']:
                free.append((row,col))
    return free

def victory_for(board, sgn):
    if sgn == "X":
        who = 'me'
    elif sgn == "O":
        who = 'you'
    else:
        who = None

    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc][rc] != sgn:   # main diagonal
            cross1 = False
        if board[rc][2 - rc] != sgn:  # anti-diagonal
            cross2 = False
    if cross1 or cross2:
        return who
    return None

def draw_move(board):
    free = make_list_of_free_fields(board)

    # 1. Try to win
    for row, col in free:
        board[row][col] = 'X'
        if victory_for(board, 'X') == 'me':
            return
        board[row][col] = 3 * row + col + 1  # undo

    # 2. Block opponent
    for row, col in free:
        board[row][col] = 'O'
        if victory_for(board, 'O') == 'you':
            board[row][col] = 'X'
            return
        board[row][col] = 3 * row + col + 1  # undo

    # 3. Otherwise random move
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'

# --- Game Loop ---
board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'  # computer starts in the middle
free = make_list_of_free_fields(board)
human_turn = True

while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board,'O')
    else:
        draw_move(board)
        victor = victory_for(board,'X')
    if victor != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
    print("You won!")
elif victor == 'me':
    print("I won!")
else:
    print("Tie!")