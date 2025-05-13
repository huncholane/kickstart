# [894. All Possible Full Binary Trees](https://leetcode.com/problems/all-possible-full-binary-trees/)

## Solution 1

- Same as [95](../95_unique_binary_search_trees_ii/README.md)
- Do not include start and end in the inner loop

## Solution 2

- Slight optimization by skipping evens
```text
Problem size must be odd
0    2n   n
1    2n-1 y
2    2n-2 n
3    2n-3 y
4    2n-4 n
2n-1 1    y
2n   0    n
f(2n+1) = nth catalan number
Bail early when start is odd
```
