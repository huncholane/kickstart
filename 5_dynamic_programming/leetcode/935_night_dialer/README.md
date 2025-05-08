# [935. Knight Dialer](https://leetcode.com/problems/knight-dialer/)

- Counting Problem
- Remember to mod 10^9+7

## Breakdown

```text
Keypad:
1 2 3
4 5 6
7 8 9
  0

Neighbors:
0: 4, 6
1: 6, 8
2: 7, 9
3: 4, 8
4: 0, 3, 9
5: 
6: 0, 1, 7
7: 2, 6
8: 1, 3
9: 2, 4

f(i, d) = # numbers of length i ending with digit d
10N unique subproblems
f(i,0)+f(i,1)+f(i,2)...f(i,9)
```
