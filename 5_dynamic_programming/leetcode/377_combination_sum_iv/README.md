# [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)

```text
Counting Problem

t = target, n = size of nums
f(t) = #ways of constructing amount t using the nums
f(t) = sum(f(t-nums[i])) for i [0,n]
ex nums = [1,2]:
    f(t) = f(t-1) + f(t-2)
```
