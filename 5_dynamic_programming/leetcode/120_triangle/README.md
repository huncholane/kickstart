# [120. Triangle](https://leetcode.com/problems/triangle/)

## Solution 1

- Fill in going down right where `col==0` means only use up and `col==row` means only use up-left
  - Get the min val + current cell while doing this
  - Python will get you with negative indexing if you don't account for `col==0`
- Return the min value of the last row in the table
- Each cell means the minimum value of paths to get to that cell
