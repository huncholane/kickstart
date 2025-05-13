# [241. Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/)

## Solution 1

```text
Build a parse tree
v1+v2*v3-v4...vn+1
n operators, n+1 numbers

num parse trees exponential in n
f(n) = sum(f(i-1)*f(n-1)) [1,n] = nth catalan number
```

## Solution 2

- Add memoization
