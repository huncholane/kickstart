# [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

## Requirements

- Return the k most frequent words sorted highest to lowest

## Solution 1 - Sort with Timsort

- Create hash map of word -> frequence
- Store the unique words into a list
- Sort highest to lowest using the frequency then lexicographical order. `lambda x: (-freq[x], x)`
- Return [0,k-1]

## Solution 2 - Quickselect and Sort

- Create hash map of word -> frequence
- Overwrite unique values into original array
- Move to the needed values into [0,k-1] using quickselect
- Sort the good values and return [0,k-1]
