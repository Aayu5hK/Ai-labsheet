def calculate_misplaced_blocks(current, target):
    """Count how many blocks are in incorrect positions"""
    return sum(1 for i in range(len(current)) if current[i] != target[i])

def generate_swapped_neighbors(state):
    """Generate all possible states by swapping adjacent blocks"""
    neighboring_states = []
    for i in range(len(state) - 1):
        new_state = state.copy()
        new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
        neighboring_states.append((new_state, f"swap({i}, {i+1})"))
    return neighboring_states

def solve_block_arrangement(start, goal):
    """Hill Climbing algorithm for block arrangement problem"""
    current = start
    current_score = calculate_misplaced_blocks(current, goal)
    solution_path = []

    print(f"Initial Stack: {current}")
    print(f"Initial Heuristic: {current_score}\n")

    while True:
        neighbors = generate_swapped_neighbors(current)
        best_neighbor = None
        best_score = current_score

        # Evaluate all neighboring states
        for state, move in neighbors:
            score = calculate_misplaced_blocks(state, goal)
            print(f"Evaluating: {state} | Heuristic: {score}")

        print()

        # Select best neighbor
        for state, move in neighbors:
            score = calculate_misplaced_blocks(state, goal)
            if score < best_score:
                best_score = score
                best_neighbor = (state, move)

        # Terminate if no better neighbor found
        if best_neighbor is None:
            print("Stuck at local minimum or reached goal.")
            break

        # Move to best neighbor
        current, move = best_neighbor
        current_score = best_score
        solution_path.append(move)
        print(f"Move: {move}")
        print(f"Current Stack: {current}")
        print(f"Current Heuristic: {current_score}\n")

        # Check for goal state
        if current_score == 0:
            break

    if current_score == 0:
        print("Goal reached!")
        print("Solution path:", solution_path)
    else:
        print("Hill Climbing got stuck. Best state found:")
        print("Final Stack:", current)
        print("Path tried:", solution_path)

# Example usage
if __name__ == "__main__":
    initial_arrangement = ['C', 'A', 'D', 'B']
    target_arrangement = ['A', 'B', 'C', 'D']

    solve_block_arrangement(initial_arrangement, target_arrangement)