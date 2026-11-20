# 0/1 Knapsack Problem - Dynamic Programming (Tabulation)

## Aim
The aim of this program is to solve the classic **0/1 Knapsack Problem** using a straightforward Dynamic Programming approach. 

Given a knapsack (backpack) with a maximum weight capacity, and a set of items (each with its own weight and value), the goal is to determine the maximum total value you can carry. The "0/1" means you cannot break an item into pieces—you either leave it behind (0) or take the whole thing (1).

## How It Works (The Logic)
This program uses the **Bottom-Up Tabulation** method, which mimics solving the problem manually on a piece of paper using a grid.

1. **Setting up the Grid:** 
   We create a 2D table (`dp`) where the rows represent the items we can choose from, and the columns represent every possible weight capacity from `0` up to our maximum limit `W`.
2. **Filling the Grid:** 
   We loop through every cell in the table. For each cell, we make a choice:
   * **Exclude the item:** We skip it, meaning our best value is simply the best value from the row directly above it.
   * **Include the item:** We add the item's value, but we subtract its weight from our current capacity. We then look at the row above to see the best value we could get with the *remaining* weight.
   * We compare both choices and write the strictly higher number into our grid.
3. **The Answer:** 
   Once the grid is full, the maximum possible value is always found in the very last box (bottom-right corner).
4. **Tracing Backwards (Finding the Items):**
   To find out *which* items gave us that maximum value, we start at the bottom-right corner and move upwards. If the value in our current box is different from the box directly above it, it means we must have packed that item. We then subtract its weight and shift left to find the remaining items.

## Complexities
* **Time Complexity: O(n * W)**
  Where `n` is the number of items and `W` is the maximum capacity of the knapsack. The program uses a nested loop to fill out a grid of size `(n+1) x (W+1)`, meaning the time it takes grows proportionally to the number of items multiplied by the weight limit.
* **Space Complexity: O(n * W)**
  We are storing a 2D list (matrix) of size `(n+1)` rows by `(W+1)` columns to hold all of our sub-problem answers.

## Conclusion
By using a 2D table to store the results of smaller sub-problems, this Dynamic Programming approach avoids calculating the same combinations over and over again. It turns what would be an extremely slow, exponential-time guessing game (recursion) into a fast, organized, and predictable grid-filling exercise.