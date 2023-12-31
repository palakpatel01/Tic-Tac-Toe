import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def minimax(board, depth, is_maximizing):
    if check_win(board, "X"):
        return -1
    if check_win(board, "O"):
        return 1
    if len(get_empty_cells(board)) == 0:
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "O"
            score = minimax(board, depth + 1, False)
            board[row][col] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "X"
            score = minimax(board, depth + 1, True)
            board[row][col] = " "
            best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -float("inf")
    best_move = None
    for row, col in get_empty_cells(board):
        board[row][col] = "O"
        score = minimax(board, 0, False)
        board[row][col] = " "
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        player_row, player_col = map(int, input("Enter your move (row col): ").split())
        if board[player_row][player_col] == " ":
            board[player_row][player_col] = "X"
        else:
            print("Invalid move. Try again.")
            continue

        if check_win(board, "X"):
            print_board(board)
            print("Congratulations! You win!")
            break

        if len(get_empty_cells(board)) == 0:
            print_board(board)
            print("It's a tie!")
            break

        print_board(board)
        print("Computer's turn...")
        
        computer_row, computer_col = find_best_move(board)
        board[computer_row][computer_col] = "O"

        if check_win(board, "O"):
            print_board(board)
            print("Computer wins!")
            break

        if len(get_empty_cells(board)) == 0:
            print_board(board)
            print("It's a tie!")
            break

        print_board(board)

if __name__ == "__main__":
    play_game()
