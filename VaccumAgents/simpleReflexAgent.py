import random

def main():
    # Get grid size from user
    x, y = map(int, input("Enter the Size of the Grid (x*y): ").split())
    grid = [[random.randint(0, 1) for _ in range(y)] for _ in range(x)]
    agent_pos = [random.randrange(x), random.randrange(y)]
    
    # Possible movement directions (4-way for clarity)
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    
    print("Initial grid state:")
    print_grid(grid, agent_pos)
    
    for step in range(1, 21):  # Simulate for exactly 20 steps
        print(f"\nStep {step}:")
        
        if grid[agent_pos[0]][agent_pos[1]] == 1:
            grid[agent_pos[0]][agent_pos[1]] = 0
            print("Action: suck")
        else:
            # Find nearest dirty room using BFS
            target = find_nearest_dirty(grid, agent_pos)
            if target:
                path = get_move_direction(agent_pos, target)
                if path:
                    dx, dy = directions[path[0]]
                    agent_pos[0] += dx
                    agent_pos[1] += dy
                    print(f"Action: move {path[0]}")
            else:
                print("Action: no dirty rooms found (idle)")
        
        print_grid(grid, agent_pos)
        
        # Early exit if all clean
        if all(all(cell == 0 for cell in row) for row in grid):
            print("\nAll rooms cleaned!")
            break

def print_grid(grid, agent_pos):
    """Print grid with agent position marked as 'P'"""
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
    queue = deque([(start[0], start[1], [])])
    
    while queue:
        i, j, path = queue.popleft()
        if grid[i][j] == 1:
            return (i, j)
        
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < rows and 0 <= nj < cols and (ni,nj) not in visited:
                visited.add((ni,nj))
                queue.append((ni, nj, path + [(di,dj)]))
    return None

def get_move_direction(current, target):
    """Get movement sequence from current to target"""
    path = []
    i, j = current
    ti, tj = target
    
    while i != ti or j != tj:
        if i < ti:
            path.append('down')
            i += 1
        elif i > ti:
            path.append('up')
            i -= 1
        elif j < tj:
            path.append('right')
            j += 1
        elif j > tj:
            path.append('left')
            j -= 1
    return path

if __name__ == "__main__":
    main()