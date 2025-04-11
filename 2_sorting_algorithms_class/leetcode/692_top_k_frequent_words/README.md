# [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

## Requirements

- Return the k most frequent words sorted highest to lowest

## Sort Solution

- Create hash map of word -> frequence
- Store the unique words into a list
- Sort highest to lowest using the frequency then lexicographical order. `lambda x: (-freq[x], x)`
- Return [0-k-1]

## Heap Solution
