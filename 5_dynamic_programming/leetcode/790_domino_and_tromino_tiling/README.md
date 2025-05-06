# [790. Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling/)

## Solution 1 - 3 Dynamic Tables

- Just think of each table as caching the result for each function along the way
  - f(n) which covers the case where all tiles are filled
    - `f(n) = f(n-1) + f(n-2) + l(n-2) + u(n-2)`
  - l(n) which covers the case where all tiles plus a lower right tile are filled
    - `l(n) = f(n-1) + l(n-1)`
  - u(n) which covers the case where all tiles plus an upper right tile are filled
    - `u(n) = f(n-1) + l(n-1)`
