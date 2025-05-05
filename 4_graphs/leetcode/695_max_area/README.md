# [695. Max Area of island](https://leetcode.com/problems/max-area-of-island/)

## Requirements

- Find the area of the largest island

## Solution 1 - BFS with Visited Map

- Iterate all unseen islands while performing bfs updating visited
- Compare number captured from each bfs call
- Return the max

## Solution 2 - DFS Changing Cells

### How

- This dfs will simply mark cells as 0 instead of maintaining a visited array

### Improvements

- Check at the beginning of dfs if the cell is valid instead of after getting the neighbors. Also deal with out of bounds here. It needs to be here anyways since 1s and 0s can change in the middle of recursion.
- Hardcode all 4 options instead of getting a list and iterating that list
