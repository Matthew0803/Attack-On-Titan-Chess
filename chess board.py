# Initial board setup (simplified)
board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],  # Black pieces
    ["p", "p", "p", "p", "p", "p", "p", "p"],  # Black pawns
    [None] * 8,  # Empty rows
    [None] * 8,
    [None] * 8,
    [None] * 8,
    ["P", "P", "P", "P", "P", "P", "P", "P"],  # White pawns
    ["R", "N", "B", "Q", "K", "B", "N", "R"]   # White pieces
]
# Lowercase = Black pieces, Uppercase = White pieces

def move_piece(board, start_pos, end_pos):
    """
    Moves a piece from start_pos to end_pos on the board.

    Args:
        board: 2D list representing the chessboard.
        start_pos: Tuple (row, col) for the piece's current position.
        end_pos: Tuple (row, col) for the target position.

    Returns:
        bool: True if the move was successful, False otherwise.
    """
    start_row, start_col = start_pos
    end_row, end_col = end_pos

    # Check if there's a piece at the start position
    if board[start_row][start_col] is None:
        print("No piece at the start position!")
        return False

    # Move the piece
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = None

    return True

# Move a white pawn from (6, 4) to (4, 4)
start = (6, 4)  # Row 6, Column 4
end = (4, 4)    # Row 4, Column 4
if move_piece(board, start, end):
    print("Move successful!")
else:
    print("Move failed!")

# Print updated board
for row in board:
    print(row)

def is_valid_pawn_move(board, start_pos, end_pos, color):
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    direction = -1 if color == "white" else 1  # White moves up (-1), Black moves down (+1)

    # Regular move (1 square forward)
    if end_col == start_col and end_row == start_row + direction:
        return board[end_row][end_col] is None

    # Capture (diagonal move)
    if abs(end_col - start_col) == 1 and end_row == start_row + direction:
        return board[end_row][end_col] is not None

    # Invalid move
    return False