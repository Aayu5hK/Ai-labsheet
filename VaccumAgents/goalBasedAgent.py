import random

def main():
    # Get grid size with input validation
    while True:
        try:
            size_input = input("Enter the Size of the Grid (x*y): ")
            x, y = map(int, size_input.replace('*', ' ').replace('x', ' ').replace(',', ' ').split())
            if x <= 0 or y <= 0:
                print("Please enter positive integers for grid size.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space")

    # Initialize grid with random dirt (1) or clean (0)
    grid = [[random.randint(0, 1) for _ in range(y)] for _ in range(x)]
    agent_pos = [random.randint(0, x-1), random.randint(0, y-1)]
    
    # Movement directions (8-connected)
    directions = {
        'up-left': (-1, -1), 'up': (-1, 0), 'up-right': (-1, 1),
        'left': (0, -1), 'right': (0, 1),
        'down-left': (1, -1), 'down': (1, 0), 'down-right': (1, 1)
    }
    
    print("\nInitial grid state:")
    print_grid(grid, agent_pos)
    
    action_sequence = []
    steps = 0
    
    while steps < 100:  # Safety limit to prevent infinite loops
        current_val = grid[agent_pos[0]][agent_pos[1]]
        
        # Action decision
        if current_val == 1:
            action = "suck"
            grid[agent_pos[0]][agent_pos[1]] = 0
        else:
            # Find nearest dirty room
            target = find_nearest_dirty(grid, agent_pos)
            if target:
                action = get_move_direction(agent_pos, target, directions)
                agent_pos = [agent_pos[0] + directions[action][0], 
                            agent_pos[1] + directions[action][1]]
            else:
                action = "terminate (all clean)"
        
        # Record and display action
        steps += 1
        action_sequence.append(action)
        print(f"\nStep {steps}: {action.upper()}")
        print_grid(grid, agent_pos)
        
        if action == "terminate (all clean)":
            break
    
    # Display results
    print("\nACTION SEQUENCE:")
    for i, action in enumerate(action_sequence, 1):
        print(f"Step {i}: {action}")
    
    print("\nFINAL GRID STATE:")
    print_grid(grid, agent_pos)

def print_grid(grid, agent_pos):
    """Display grid with agent position marked as 'P'"""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if [i, j] == agent_pos:
                print('P', end=' ')
            else:
                print(grid[i][j], end=' ')
        print()

def find_nearest_dirty(grid, start):
    """BFS to find nearest dirty room"""
    from collections import deque
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([(start[0], start[1])])
    visited.add((start[0], start[1]))
    
    while queue:
        i, j = queue.popleft()
        if grid[i][j] == 1:
            return (i, j)
        
        for di, dj in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < rows and 0 <= nj < cols and (ni,nj) not in visited:
                visited.add((ni,nj))
                queue.append((ni, nj))
    return None

def get_move_direction(current, target, directions):
    """Determine best move direction toward target"""
    di = target[0] - current[0]
    dj = target[1] - current[1]
    
    # Normalize direction
    di = 1 if di > 0 else (-1 if di < 0 else 0)
    dj = 1 if dj > 0 else (-1 if dj < 0 else 0)
    4
    # Find matching direction
    for name, (ddi, ddj) in directions.items():
        if ddi == di and ddj == dj:
            return name
    return "right"  # default if no match

if __name__ == "__main__":
    main()