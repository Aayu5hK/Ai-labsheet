import random
import time

def main():
    # Get grid size from user
    x, y = map(int, input("Enter the Size of the Grid (x*y): ").split())
    grid = [[random.randint(0, 1) for _ in range(y)] for _ in range(x)]
    
    print("Randomly assigned grid states:")
    for row in grid:
        print(' '.join(map(str, row)))
    
    # Set initial position randomly
    initial_pos = [random.randrange(x), random.randrange(y)]
    print(f"\nInitial Position in the Grid: Room[{initial_pos[0]}, {initial_pos[1]}] => {grid[initial_pos[0]][initial_pos[1]]}")
    
    # Possible movement directions (8-way)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    steps = 0
    
    while True:
        if grid[initial_pos[0]][initial_pos[1]] == 1:
            grid[initial_pos[0]][initial_pos[1]] = 0
            steps += 1
            print(f"Step {steps}: Room[{initial_pos[0]}, {initial_pos[1]}] was dirty. Cleaned it.")
        else:
            moved = False
            # Check adjacent cells first
            for dx, dy in directions:
                ni, nj = initial_pos[0] + dx, initial_pos[1] + dy
                if 0 <= ni < x and 0 <= nj < y and grid[ni][nj] == 1:
                    initial_pos = [ni, nj]
                    steps += 1
                    print(f"Step {steps}: Current room clean. Moved to dirty neighbor Room[{ni}, {nj}].")
                    moved = True
                    break
            
            if not moved:
                # Search for any dirty room
                found = False
                for i in range(x):
                    for j in range(y):
                        if grid[i][j] == 1:
                            initial_pos = [i, j]
                            steps += 1
                            print(f"Step {steps}: No dirty neighbor. Moving to Room[{i}, {j}].")
                            found = True
                            break
                    if found:
                        break
                
                if not found:
                    print(f"\nAll rooms are clean! Cleaning completed in {steps} steps.")
                    break
    
    # Display final grid
    print("\nFinal grid state:")
    for i in range(x):
        for j in range(y):
            if [i, j] == initial_pos:
                print("P", end=' ')
            else:
                print(grid[i][j], end=' ')
        print()
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()