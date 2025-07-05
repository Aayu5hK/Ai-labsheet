**Simple Reflex Agent**
  Implement a simple reflex vacuum cleaning agent that selects actions based solely on the current percept (whether the current cell is dirty or clean). If the cell is dirty, the agent sucks the dirt; otherwise, it moves to a random adjacent cell.
  Input: Current cell state (dirty or clean).
  Output: Action (suck, move up, move down, move left, move right).
  Requirement: Simulate the agent's behavior for 20 steps and display the grid state after each step.

**Output**
![image](https://github.com/user-attachments/assets/0b9c8db0-9020-4f28-9b6b-2f2532bd32cd)
![image](https://github.com/user-attachments/assets/580f81e2-ba36-4416-a009-4000491225df)

**Goal-Based Agent**
  Implement a goal-based vacuum cleaning agent that maintains an internal model of the grid to track which cells are dirty. The agent aims to clean all dirty cells and stops when the entire grid is clean. Use a simple search strategy (e.g., moving to the nearest dirty cell).
  Input: Current cell state and agent’s internal model of the grid.
  Output: Sequence of actions to achieve a clean grid.
  Requirement: Display the sequence of actions and the final grid state.

**Output**
![image](https://github.com/user-attachments/assets/c23fa07e-05eb-46f6-bf7d-7593a22d84ab)
![image](https://github.com/user-attachments/assets/d188d5b7-293e-482c-b7e3-4d403456b326)
![image](https://github.com/user-attachments/assets/1c84728c-2866-41c4-949f-b3e364805678)

**Utility-Based Agent**
  Implement a utility-based vacuum cleaning agent that assigns a utility score to actions based on cleanliness and movement efficiency (e.g., minimize movement steps). Define a utility function (e.g., +5 for cleaning a dirty cell, -1 for each move). The agent selects actions to maximize cumulative utility.
  Input: Current cell state and internal model of the grid.
  Output: Sequence of actions optimizing utility.
  Requirement: Display the actions, final grid state, and total utility score.


**Output**
![image](https://github.com/user-attachments/assets/d52ec19e-ee38-48f3-a6df-16806030fcae)
![image](https://github.com/user-attachments/assets/95c9d8d3-a221-4906-9a44-0fe969d72a43)
![image](https://github.com/user-attachments/assets/775980a3-6135-4c74-8a55-b9d664eb9aa2)




