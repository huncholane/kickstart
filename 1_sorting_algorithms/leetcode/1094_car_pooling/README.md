# [1094. Car Pooling](https://leetcode.com/problems/car-pooling/description/)

## Requirements

- Find out if it's possible to make a direct route picking up car poolers

## Solution 1 - Interval Template

- Need a max heap that stores passengers and end for each stop
- When the passengers overflow the capacity return false
- Return true when able to get through all trips
