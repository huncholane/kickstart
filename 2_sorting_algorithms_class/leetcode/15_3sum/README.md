# [15. 3Sum](https://leetcode.com/problems/3sum/)

## Requirements

- Get all the pairs of numbers that will sum to 0 with no duplicates

## Decrease and Conquer Solution with Presorting

- Presort the array
- Make a two sum function that returns all the pairs for a range that add up to a target with no duplicates
  - Slide to skip duplicates going left to right
- Iterate the array and run two sum on the range [i+1,n-3] based on the compliment of the current index's value
- Add the current value to each solution from the two sum call
- Slide to skip duplicates for the current value
