# [265 Paint House II](https://leetcode.com/problems/paint-house-ii/)

- **Optimization Problem**

## Solution 1 - O(nk^2)

```text
Ex:
1 5 3 -> 1       5       3       -> 1 5  3
2 9 4    2+5|2+3 1+9|3+9 4+1|4+5    5 10 5
min(table[-1])=5

Objective Function:
f(n,c) = minimum cost to paint houses 0..i with the last house colored with c
```

## Solution 2 - O(nk)

```text
Same as before but only need the last 2 minimums and pick the one that has a different j index
```
