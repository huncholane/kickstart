# [256. Paint House](https://leetcode.com/problems/paint-house/)

## Solution 1 - Bottom Up Tabulation

- Calculate the min it can cost for each color at each index accumulating
- So at row one green for example, add the minimum of the previous red and blue
- At the end, pick the cheapest color to end with
