# [120. Triangle](https://leetcode.com/problems/triangle/)

## Solution 1

- Fill in going down right where `col==0` means only use up and `col==row` means only use up-left
- Return the min value of the last row in the table
- Each cell means the minimum value of paths to get to that cell
