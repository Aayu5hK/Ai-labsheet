import random
from collections import deque

class UtilityAgent:
    def __init__(self, grid_size):
        self.grid = [[random.randint(0, 1) for _ in range(grid_size[1])] for _ in range(grid_size[0])]
        self.position = [random.randint(0, grid_size[0]-1), random.randint(0, grid_size[1]-1)]
        self.utility_score = 0
        self.action_history = []
        self.directions = {
            'up-left': (-1, -1), 'up': (-1, 0), 'up-right': (-1, 1),
            'left': (0, -1), 'right': (0, 1),
            'down-left': (1, -1), 'down': (1, 0), 'down-right': (1, 1)
        }
        # Utility weights
        self.weights = {
            'clean': 10,       # Reward for cleaning
            'move': -1,        # Cost for moving
            'idle': -5,        # Penalty for doing nothing
            'remaining_dirt': -2  # Penalty per remaining dirty square
        }

    def print_grid(self):
        """Display current grid state"""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if [i, j] == self.position:
                    print('P', end=' ')
                else:
                    print(self.grid[i][j], end=' ')
            print()

    def calculate_utility(self, action):
        """Calculate utility of possible actions"""
        if action == "suck":
            return self.weights['clean']
        elif action.startswith("move"):
            return self.weights['move']
        elif action == "idle":
            return self.weights['idle']
        return 0

    def find_best_action(self):
        """Evaluate all possible actions and choose the one with highest utility"""
        current_val = self.grid[self.position[0]][self.position[1]]
        possible_actions = []
        
        # Always clean if current room is dirty (highest utility)
        if current_val == 1:
            return "suck"
        
        # Evaluate movement options
        best_move = None
        max_utility = float('-inf')
        
        # Find nearest dirty room using BFS
        target = self.find_nearest_dirty()
        if target:
            move_dir = self.get_move_direction(target)
            move_utility = self.calculate_utility(f"move {move_dir}")
            if move_utility > max_utility:
                max_utility = move_utility
                best_move = f"move {move_dir}"
        
        # If no good moves, consider idle
        if best_move is None:
            idle_utility = self.calculate_utility("idle")
            if idle_utility > max_utility:
                return "idle"
        
        return best_move if best_move else "terminate"

    def execute_action(self, action):
        """Execute the chosen action and update utility"""
        utility = 0
        
        if action == "suck":
            self.grid[self.position[0]][self.position[1]] = 0
            utility = self.weights['clean']
            self.action_history.append("SUCK")
        elif action.startswith("move"):
            direction = action.split()[1]
            dx, dy = self.directions[direction]
            self.position[0] += dx
            self.position[1] += dy
            utility = self.weights['move']
            self.action_history.append(f"MOVE {direction.upper()}")
        elif action == "idle":
            utility = self.weights['idle']
            self.action_history.append("IDLE")
        
        # Penalty for remaining dirt
        dirt_count = sum(sum(row) for row in self.grid)
        utility += dirt_count * self.weights['remaining_dirt']
        
        self.utility_score += utility
        return action == "terminate"

    def find_nearest_dirty(self):
        """BFS to find nearest dirty room"""
        rows, cols = len(self.grid), len(self.grid[0])
        visited = set()
        queue = deque([(self.position[0], self.position[1])])
        visited.add((self.position[0], self.position[1]))
        
        while queue:
            i, j = queue.popleft()
            if self.grid[i][j] == 1:
                return (i, j)
            
            for di, dj in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < rows and 0 <= nj < cols and (ni,nj) not in visited:
                    visited.add((ni,nj))
                    queue.append((ni, nj))
        return None

    def get_move_direction(self, target):
        """Determine move direction toward target"""
        di = target[0] - self.position[0]
        dj = target[1] - self.position[1]
        di = 1 if di > 0 else (-1 if di < 0 else 0)
        dj = 1 if dj > 0 else (-1 if dj < 0 else 0)
        
        for name, (ddi, ddj) in self.directions.items():
            if ddi == di and ddj == dj:
                return name
        return "right"

def main():
    # Get grid size
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

    agent = UtilityAgent((x, y))
    steps = 0
    
    print("\nInitial grid state:")
    agent.print_grid()
    
    while steps < 100:  # Prevent infinite loops
        steps += 1
        action = agent.find_best_action()
        
        print(f"\nStep {steps}:")
        print(f"Possible Action: {action.upper()}")
        
        should_terminate = agent.execute_action(action)
        print(f"Chosen Action: {agent.action_history[-1]}")
        print(f"Current Utility: {agent.utility_score}")
        agent.print_grid()
        
        if should_terminate or all(all(cell == 0 for cell in row) for row in agent.grid):
            print("\nTermination condition met!")
            break
    
    # Final results
    print("\nACTION SEQUENCE:")
    for i, action in enumerate(agent.action_history, 1):
        print(f"Step {i}: {action}")
    
    print("\nFINAL GRID STATE:")
    agent.print_grid()
    print(f"\nTOTAL UTILITY SCORE: {agent.utility_score}")
    print(f"TOTAL STEPS: {steps}")

if __name__ == "__main__":
    main()