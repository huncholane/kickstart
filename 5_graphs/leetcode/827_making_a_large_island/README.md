# [827. Making a Large Island](https://leetcode.com/problems/making-a-large-island/)

## Requirements

- Allowed to change 1 0 to a 1
- Like making a bridge of 1 length
- Figure out how to make the largest island

## Solution 1

- Initialize a variable for index to 2; this avoids conficts with 1 and 0
- We are going to label each cell with a unique index
- Run dfs as usual and store the resulting area into the island area map and increment global index
- Mark grid cell with the index instead of using a visited map
- Initialize largest to 0
- Do another loop and at each grid cell with a 0
  - Create a seen set
  - Initialize area to 1
  - For each neighbor
    - Add to seen
    - Use the island area map and cell value to add to area
  - Update largest
- Return largest or the grid size if largest is still 0
