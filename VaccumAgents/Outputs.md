# Vacuum Cleaning Agent Simulations

Three types of intelligent agents were implemented to solve the vacuum cleaning problem:

---

## 🧹 Simple Reflex Agent
**Behavior**: Reacts only to current cell state  
**Decision Making**:  
- If dirty → Sucks  
- If clean → Moves randomly  

### Output Screenshots
![Simple Reflex Agent Step 1](https://github.com/user-attachments/assets/0b9c8db0-9020-4f28-9b6b-2f2532bd32cd)  
*Initial grid state with agent position*

![Simple Reflex Agent Step 20](https://github.com/user-attachments/assets/580f81e2-ba36-4416-a009-4000491225df)  
*Final state after 20 steps*

---

## 🎯 Goal-Based Agent 
**Behavior**: Maintains world model to achieve complete cleanliness  
**Features**:  
- Tracks all dirty cells  
- Moves systematically to nearest dirty cell  
- Stops when all clean  

### Output Screenshots
![Goal-Based Initial State](https://github.com/user-attachments/assets/c23fa07e-05eb-46f6-bf7d-7593a22d84ab)  
*Initial grid with multiple dirty cells*

![Goal-Based Mid Process](https://github.com/user-attachments/assets/d188d5b7-293e-482c-b7e3-4d403456b326)  
*Agent moving toward dirty cells*

![Goal-Based Final State](https://github.com/user-attachments/assets/1c84728c-2866-41c4-949f-b3e364805678)  
*Fully cleaned grid*

---

## 📊 Utility-Based Agent
**Behavior**: Maximizes performance measure  
**Utility Function**:  
- +5 for cleaning  
- -1 per move  
- -2 for idling  
- -1 per remaining dirty cell  

### Output Screenshots
![Utility Agent Decision](https://github.com/user-attachments/assets/d52ec19e-ee38-48f3-a6df-16806030fcae)  
*Agent evaluating action utilities*

![Utility Agent Progress](https://github.com/user-attachments/assets/95c9d8d3-a221-4906-9a44-0fe969d72a43)  
*Optimal path selection*

![Utility Final Score](https://github.com/user-attachments/assets/775980a3-6135-4c74-8a55-b9d664eb9aa2)  
*Final utility score display*

---
