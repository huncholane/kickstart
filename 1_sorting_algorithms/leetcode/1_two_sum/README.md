# [1. Two Sum](https://leetcode.com/problems/two-sum/)

## Requirements

- Return indices of the first instance to create a compliment for the target

## Solution 1 - Compliment Hashmap

- Iterate the numbers while maintaining a hashmap of the numbers to index
- Eventually we run into the compliment when target-num is in the map
- This is in place O(n) with O(n) space complexity
