# [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

## Requirements

- Rotton oranges infect the oranges around it
- Determine when there will still be some fresh ones

## Solution

- Make a function that returns the adjacent cells
- Run BFS and infect oranges with a depth map
- Do this for every connected component
- Return the max amount of minutes
