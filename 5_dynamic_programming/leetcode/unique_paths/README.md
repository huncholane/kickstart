# [Count Unique Paths](https://leetcode.com/problems/unique-paths/)

## Solution 1 - Dynamic Programming

- How many paths to reach the bottom-right corner in a 2d grid

```text
1  1  1  1  1
1  2  3  4  5
1  3  6  10 15
1  4  10 20 35
1  5  15 35 70
```

- Add directly left and directly up flowing down and right

```text
def f(m,n):
   table = 2d array of size m x n
   for i in [0, m-1]:
      table[i][0] = 1
   for j in [0, n-1]:
      table[0][j] = 1
   for row in [1, m-1]:
      for col in [1, n-1]:
         table[row][col] = up + left
   return table[m-1][n-1]
```

- T(m,n) = O(mn)
- S(m,n) = O(mn)
- Can optimize space complexity to **O(n) OR O(m)** with current and previous row instead of 2d grid
