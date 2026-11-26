import math

# -------- PRINT BOARD ----------
def print_board(board):
    for r in range(3):
        row = []
        for c in range(3):
            row.append(board[r][c] if board[r][c] != " " else "_")
        print(" ".join(row))
    print()

# -------- EMPTY CELLS ----------
def empty_cells(board):
    cells = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                cells.append((r, c))
    return cells

# -------- CHECK WINNER ----------
def winner(board):
    lines = []

    # rows and columns
    for i in range(3):
        lines.append([board[i][0], board[i][1], board[i][2]]) 
        lines.append([board[0][i], board[1][i], board[2][i]])

    # diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    if ["X","X","X"] in lines:
        return "X"
    if ["O","O","O"] in lines:
        return "O"
    return None

# -------- CHECK WINNER ----------
def winner(board):
    lines = []

    # rows and columns
    for i in range(3):
        lines.append([board[i][0], board[i][1], board[i][2]])
        lines.append([board[0][i], board[1][i], board[2][i]])

    # diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    if ["X","X","X"] in lines:
        return "X"
    if ["O","O","O"] in lines:
        return "O"
    return None

# -------- DRAW CHECK ----------
def is_draw(board):
    return winner(board) is None and len(empty_cells(board)) == 0

# -------- MINIMAX ----------
def minimax(board, is_maximizing):

    w = winner(board)

    if w == "X":   # computer
        return 1
    if w == "O":   # human
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for (r, c) in empty_cells(board):
            board[r][c] = "X"
            score = minimax(board, False)
            board[r][c] = " "
            best = max(best, score)
        return best

    else:
        best = math.inf
        for (r, c) in empty_cells(board):
            board[r][c] = "O"
            score = minimax(board, True)
            board[r][c] = " "
            best = min(best, score)
        return best


# -------- BEST MOVE ----------
def best_move(board):
    best_score = -math.inf
    move = None

    for (r, c) in empty_cells(board):
        board[r][c] = "X"
        score = minimax(board, False)
        board[r][c] = " "

        if score > best_score:
            best_score = score
            move = (r, c)

    return move

    if score > best_score:
            best_score = score
            move = (r, c)

    return move

# -------- MAIN GAME ----------
board = [[" " for _ in range(3)] for _ in range(3)]

print("Tic Tac Toe Game")
print_board(board)

while True:

    r = int(input("Enter row: "))
    c = int(input("Enter col: "))

    if (r, c) not in empty_cells(board):
        print("Invalid move")
        continue

    board[r][c] = "O"
    print("\nAfter your move:")
    print_board(board)

    if winner(board) == "O":
        print("You win")
        break

    if is_draw(board):
        print("Draw")
        break

    mr, mc = best_move(board)
    board[mr][mc] = "X"

    print("Computer move:")
    print_board(board)

    if winner(board) == "X":
        print("Computer wins")
        break

    if is_draw(board):
        print("Draw")
        break