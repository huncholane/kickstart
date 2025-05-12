# [97. Interleaving String](https://leetcode.com/problems/interleaving-string/)

```text
Decision Problem

Two cases:
    1. Rightmost came from s1
    2. Rightmost came from s2

f(m,n) = f(i,j-1) if s3[i+j]==s3[j]
         or
         f(i-1,j) if s3[i+j]==s1[i]

abc,de,abdec
│     d e
│   T F F
│ a T T T
│ b F F T
│ c F F T

aabcc,dbbca,aadbbcbcac
│     d b b c a
│   T F F F F F
│ a T F F F F F
│ a T T T T T F
│ b F T T F T F
│ c F F T T T T
│ c F F F T F T
```
