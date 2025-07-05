import random
import sys

def abs_val(a):
    return -a if a < 0 else a

def main():
    # Get grid dimensions
    while True:
        try:
            x, y = map(int, input("Enter the Size of the Grid (x*y): ").split())
            if x <= 0 or y <= 0:
                print("Please enter positive integers.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")

    # Initialize grid with random dirt (1 = dirty, 0 = clean)
    grid = [[random.randint(0, 1) for _ in range(y)] for _ in range(x)]
    
    print("\nInitial grid state:")
    for row in grid:
        print(' '.join(map(str, row)))
    
    # Random starting position
    pos_x, pos_y = random.randint(0, x-1), random.randint(0, y-1)
    steps = 0
    
    print(f"\nInitial Position: Room[{pos_x}, {pos_y}]")

    while True:
        if grid[pos_x][pos_y] == 1:
            grid[pos_x][pos_y] = 0
            steps += 1
            print(f"Step {steps}: Cleaned Room[{pos_x}, {pos_y}].")
        else:
            # Find nearest dirty room using Manhattan distance
            min_dist = sys.maxsize
            target_x, target_y = -1, -1
            
            for i in range(x):
                for j in range(y):
                    if grid[i][j] == 1:
                        dist = abs_val(i - pos_x) + abs_val(j - pos_y)
                        if dist < min_dist:
                            min_dist = dist
                            target_x, target_y = i, j
            
            if target_x == -1:  # All rooms clean
                break
            
            # Move one step toward target (Manhattan path)
            if target_x > pos_x:
                pos_x += 1
            elif target_x < pos_x:
                pos_x -= 1
            elif target_y > pos_y:
                pos_y += 1
            elif target_y < pos_y:
                pos_y -= 1
            
            steps += 1
            print(f"Step {steps}: Moved to Room[{pos_x}, {pos_y}].")

    print(f"\nAll rooms clean! Total steps = {steps}")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()