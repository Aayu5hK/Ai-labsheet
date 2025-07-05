from collections import deque
import copy

# Target configuration
TARGET = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 0]]

# Possible movement directions
DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def manhattan_distance(board):
    """Compute Manhattan distance of tiles from their target positions"""
    distance = 0
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val != 0:
                goal_i, goal_j = (val - 1) // 3, (val - 1) % 3
                distance += abs(goal_i - i) + abs(goal_j - j)
    return distance

def find_empty(board):
    """Locate the empty space (0) position"""
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def is_goal(board):
    """Check if board matches target configuration"""
    return board == TARGET

def get_moves(board):
    """Generate all valid moves from current board state"""
    empty_i, empty_j = find_empty(board)
    moves = []

    for move, (di, dj) in DIRECTIONS.items():
        new_i, new_j = empty_i + di, empty_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_board = copy.deepcopy(board)
            new_board[empty_i][empty_j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[empty_i][empty_j]
            moves.append((move, new_board))
    return moves

def solve_puzzle(start_board):
    """Breadth-First Search to find solution path"""
    queue = deque()
    visited = set()
    queue.append((start_board, []))
    visited.add(tuple(tuple(row) for row in start_board))

    print("Initial State:")
    for row in start_board:
        print(row)
    print(f"Initial Manhattan Distance: {manhattan_distance(start_board)}\n")

    while queue:
        current_board, path = queue.popleft()

        if is_goal(current_board):
            print("Goal reached!")
            return path

        for move, next_board in get_moves(current_board):
            board_tuple = tuple(tuple(row) for row in next_board)
            if board_tuple not in visited:
                visited.add(board_tuple)
                print(f"Explored Move: {move}")
                for row in next_board:
                    print(row)
                print(f"Manhattan Distance: {manhattan_distance(next_board)}\n")
                queue.append((next_board, path + [move]))

    return None

# Example puzzle setup
initial_board = [[1, 2, 3],
                 [4, 0, 5],
                 [7, 8, 6]]

solution_path = solve_puzzle(initial_board)

if solution_path:
    print("Optimal solution path (moves):")
    print(solution_path)
else:
    print("No solution found.")