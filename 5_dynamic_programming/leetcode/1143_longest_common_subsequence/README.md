# [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

- **Maximization Problem**

```text
Two words with m and n lengths

Reward for match = 1
mismatch         = 0
insertion        = 0
deletion         = 0

f(i,j) = length of LCS of x1...xi and y1...yj
    | f(i-1,j)
max | f(i,j-1)
    | f(i-1,j-1) + 1 if xi==yi

ex frog and dog:
    f r o g
  0 0 0 0 0
d 0 0 0 0 0
o 0 0 0 1 0
g 0 0 0 1 2

ex abcde and ace
    a b c d e
  0 0 0 0 0 0
a 0 1 1 1 1 1
c 0 1 1 2 2 2
e 0 1 1 1 1 3
```

## Solution 1 - O(mn)
