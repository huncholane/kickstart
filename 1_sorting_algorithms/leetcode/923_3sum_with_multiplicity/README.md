# [923. 3Sum With Multiplicity](https://leetcode.com/problems/3sum-with-multiplicity/) ✅

## Requirements

- Count the 3sums including duplicates

## Solution 1 - 3sum Template

- Use the template
  - Deprecate j on less than; nothing else
  - Increment i on greater than; nothing else
  - Two cases for == target
    - If ival == jval, do n choose 2 on j-i+1
    - Else, multiple the count of ival and count of jval
- Don't forget to spam all operations with mod 10^9+7

## Solution 2 - Full Blown combinatorics

- Use combinatorics over the range of 100 in definition
