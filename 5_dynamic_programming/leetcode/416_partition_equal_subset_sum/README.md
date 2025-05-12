# [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

- Decision Problem

## Solution 1

```text
Decision Problem

Recursion
     o
   e/ \i
   /   \
  o     o
e/ \i e/ \i
o   o o   o

_ _ _ _ _ _ _ _
Is there a subset summing to k?

DP
f(n,k) = True if subset summing to k
f(n,k) = f(n-1,k) or f(n-1,k-nth num)
         exclude     include
n in [0,n]
k in [0,total/2]

nums=[1,2,3,4], k=5
│   0 1 2 3 4 5
│ 0 T F F F F F
│ 1 T T F F F F
│ 2 T T T T F F
│ 3 T T T T T T
│ 4 T T T T T T


nums[1,2,5], k=4
│   0 1 2 3 4
│ 0 T F F F F
│ 1 T T F F F
│ 2 T T T T F
│ 5 T T T T F
```
