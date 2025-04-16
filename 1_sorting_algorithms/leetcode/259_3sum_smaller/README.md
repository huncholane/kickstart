# [259. 3Sum Smaller](https://leetcode.com/problems/3sum-smaller/)

## Requirements

- Find all the 3 sums less than target

## Solution 1 - 3sum template

- Use the 3sum template and deprecate j on >=
- On < increment i and increment result by j-i
  - There will be a solution for every pair in j-i since we presorted
