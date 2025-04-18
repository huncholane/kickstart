
# [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/description/)

## Requirements
- Merge overlapping intervals 

## Solution 1 - Interval Template
- Presort
- Make a make heap
- Append new intervals
- Update end time for max when popping the heap

## Solution 2 - Line Sweep
- This problem is simple enough to not use a heap
- Presort and update the last result's end time on each iteration
