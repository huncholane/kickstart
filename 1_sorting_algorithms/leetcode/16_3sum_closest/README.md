# [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)

## Requirements

- Find the sum that is closest to the target
- Always 1 solution

## Solution 1 - Presort

- Presort the array
- Init closest distance to infinity
- Init an answer
- Use the threesum template
- On the equal case, return sum
- On the less than case try to update closest distance as sum-target and update answer
- On the greater case try to update closest distance as target-sum and update answer
