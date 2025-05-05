# [18. 4Sum](https://leetcode.com/problems/4sum/)

## Requirements

- Enumerate all the solutions for 4 numbers to equal target

## Solution 1 - Presort

- Just like 3sum make a two sum function
- Now make a 3sum solution that uses left from outer 4sum loop [left,n-3]
- Loop calling 4sum in range [0,n-4]
