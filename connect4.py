import math
import random

# Board dimensions and players
ROWS = 6;
COLS = 7;

EMPTY = 0;
PLAYER = 1;
AI = 2

# Determin if the game is over (win or draw)
def is_terminal_node(board):
    return check_winner(board, PLAYER) or check_winner(board, AI) or len(get_valid_moves(board)) == 0

# Remove the most recent piece from the column
def undo_move(board, col):
    for row in range(ROWS):
        if board[row][col] != EMPTY:
            board[row][col] = EMPTY
            break

 # Evaluate a slice of 4 cells and assign score       
def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER if piece == AI else AI
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 10   
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 5
    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 80
    return score

# Score the board based on potential advantages for the give piece
def score_position(board, piece):
    score = 0
    center_array = [board[r][COLS // 2] for r in range(ROWS)]
    center_count = center_array.count(piece)
    score += center_count * 6
    for row in range(ROWS):
        for col in range(COLS - 3):
            window = [board[row][col + i] for i in range(4)]
            score += evaluate_window(window, piece)
    for col in range(COLS):
        for row in range(ROWS - 3):
            window = [board[row + i][col] for i in range(4)]
            score += evaluate_window(window, piece)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            window = [board[row + i][col + i] for i in range(4)]
            score += evaluate_window(window, piece)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            window = [board[row - i][col + i] for i in range(4)]
            score += evaluate_window(window, piece)
    return score

# Minimax algorithm with a alpha-beta pruning to decide the AI's move
def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_moves(board)
    is_terminal = is_terminal_node(board)

    if depth == 0 or is_terminal:
        if is_terminal:
            if check_winner(board, AI):
                return (None, 1_000_000)
            elif check_winner(board, PLAYER):
                return (None, -1_000_000)
            else: return(None, 0)
        else:
            return (None, score_position(board, AI))
    
    if maximizingPlayer:
        value = -math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row, _ = make_move(board, col, AI)
            new_score = minimax(board, depth -1, alpha, beta, False) [1]
            undo_move(board, col)
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value
    else:
        value = math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row, _ = make_move(board, col, PLAYER)
            new_score = minimax(board, depth -1, alpha, beta, True) [1]
            undo_move(board, col)
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value

# Create an empty game board
def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

# Display the current state of the board in terminal
def print_board(board):
    for row in board:
        print(" | ".join(str(cell) for cell in row))
    print("-" * (COLS * 4 - 1))
    print("    ".join(str(i) for i in range(COLS)))

# Place a piece in the specified column
def make_move(board, col, piece):
    for row in reversed(range(ROWS)):
        if board[row][col] == EMPTY:
            board[row][col] = piece
            return row, col

# Check if a player has 4 in a row (horizontal, vertical, or diagonal)
def check_winner(board, piece):
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == piece for i in range(4)):
              return True
    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == piece for i in range(4)):
              return True
    for row in range(ROWS - 3):
        for col in range(COLS -3):
            if all(board[row + i][col + i] == piece for i in range(4)):
                return True
    
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row-i][col+i] == piece for i in range(4)):
                return True
    return False

# Get list of valid columns where a move can be made
def get_valid_moves(board):
    return [col for col in range(COLS) if board[0][col] == EMPTY]

def ai_move(board):
    valid_cols = get_valid_moves(board)
    return random.choice(valid_cols)

# Main game loop
board = create_board();
game_over = False
turn = 0 #0 = Human, 1 = AI

print_board(board)

while not game_over:
    if turn == 0:
        try:
            player_col = int(input("Choose a column (0-6): "))
            if player_col not in get_valid_moves(board):
                print("Invalid move. Try again.")
                continue
            make_move(board, player_col, PLAYER)
        except ValueError:
            print("Please enter a valid number.")
            continue
    else:
        print("AI is thinking...")
        ai_col, _ = minimax(board, depth=4, alpha=-math.inf, beta=math.inf, maximizingPlayer=True)
        make_move(board, ai_col, AI)
        print("AI chose column: ", ai_col)

    print_board(board)


    # Check for win or draw
    if check_winner(board, PLAYER):
      print("🎉 You win!")
      game_over = True
    elif check_winner(board, AI):
      print("🤖 AI wins!")
      game_over = True
    elif len(get_valid_moves(board)) == 0:
        print("It's a draw!")
        game_over = True
    
    # Alternate turns
    turn = (turn + 1) % 2