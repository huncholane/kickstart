# [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

## Requirements

- Rotton oranges infect the oranges around it
- Determine when there will still be some fresh ones

## Solution 1

- Make a function that returns the adjacent cells
- Make BFS function that takes a cell and starting minute
  - Recursively call on all adjacent cells and get the sum
  - Return -1 if there are no adjacent 1s
- Do this for every connected component
- Return the max amount of minutes
