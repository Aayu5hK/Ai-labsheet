import random

def main():
    # Get grid size with better input handling
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

    # Initialize grid
    grid = [[random.randint(0, 1) for _ in range(y)] for _ in range(x)]
    
    print("\nRandomly assigned grid states:")
    for row in grid:
        print(' '.join(map(str, row)))
    
    # Random initial position
    initial_pos = [random.randint(0, x-1), random.randint(0, y-1)]
    print(f"\nInitial Position: Room[{initial_pos[0]}, {initial_pos[1]}] => {grid[initial_pos[0]][initial_pos[1]]}")
    
    # Possible movement directions (8-connected)
    directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],          [0, 1],
        [1, -1],  [1, 0], [1, 1]
    ]
    
    steps = 0
    while True:
        current_room = grid[initial_pos[0]][initial_pos[1]]
        
        # If current room is dirty, clean it
        if current_room == 1:
            grid[initial_pos[0]][initial_pos[1]] = 0
            steps += 1
            print(f"\nStep {steps}: Cleaned Room[{initial_pos[0]}, {initial_pos[1]}]")
            continue
        
        # Check neighboring rooms for dirt
        moved = False
        for dx, dy in directions:
            ni, nj = initial_pos[0] + dx, initial_pos[1] + dy
            if 0 <= ni < x and 0 <= nj < y and grid[ni][nj] == 1:
                initial_pos = [ni, nj]
                steps += 1
                print(f"\nStep {steps}: Moved to dirty neighbor Room[{ni}, {nj}]")
                moved = True
                break
        
        if not moved:
            # Search for any dirty room in the grid
            found = False
            for i in range(x):
                for j in range(y):
                    if grid[i][j] == 1:
                        initial_pos = [i, j]
                        steps += 1
                        print(f"\nStep {steps}: No dirty neighbors. Jumped to Room[{i}, {j}]")
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

if __name__ == "__main__":
    main()