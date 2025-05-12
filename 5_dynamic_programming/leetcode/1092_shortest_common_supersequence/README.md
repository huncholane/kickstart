# [1092. Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/)

```text
Add remaining characters from lcs to longest string (don't need to add characters from lcs)
Traceback after lcs


Example 1:
abac
cab
    c a b
  0 0 0 0
a 0 0 1 1
b 0 0 1 2
a 0 0 1 2
c 0 1 1 2

Path:
│     c a b
│   * c 0 0
│ a 0 0 a 1
│ b 0 0 1 b
│ a 0 0 1 a
│ c 0 1 1 c

Alignment:
_ a b a c
c a b _ _

Result: cabac


Example 2:
bbbaaaba
bbababbb
    b b a b a b b b
  0 0 0 0 0 0 0 0 0
b 0 1 1 1 1 1 1 1 1
b 0 1 2 2 2 2 2 2 2
b 0 1 2 2 3 3 3 3 3
a 0 1 2 3 3 4 4 4 4
a 0 1 2 3 3 4 4 4 4
a 0 1 2 3 3 4 4 4 4
b 0 1 2 3 4 4 5 5 5
a 0 1 2 3 3 5 5 5 5

Path:
│     b b a b a b b b
│   * 0 0 0 0 0 0 0 0
│ b 0 b 1 1 1 1 1 1 1
│ b 0 1 b a 2 2 2 2 2
│ b 0 1 2 2 b 3 3 3 3
│ a 0 1 2 3 3 a 4 4 4
│ a 0 1 2 3 3 a 4 4 4
│ a 0 1 2 3 3 a 4 4 4
│ b 0 1 2 3 4 4 b b b
│ a 0 1 2 3 4 5 5 5 a

Alignment:
b b _ b a a a b _ _ a
b b a b _ _ _ b b b _

Result: bbabaaabbba
```
