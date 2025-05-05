# [Min Cost Stair Climbing](https://leetcode.com/problems/min-cost-climbing-stairs/)

## Solution 1 - Bottom Up Tabulation

   ```text
               __
            __|
         __|20
      __|15
   __|10

   Example paths:
   10+15+20=45
   10+20=30
   10+15=25
   ```

- Optimal substructure applies
- 0 on left and right for floor below and floor above

  ```text
  Cost array
  0...10 15 20 10 12...0
  ```

1. Accumulate path costs with min(f(i-1), f(i-2))

   ```text
   0...10 15 30 25 37...25
   ```

2. The sum is now the final value in the array

- Psuedocode

```text
def mincost(cost):
   cost.append(0)
   for i in range(2,len(cost)):
      cost[i]+=min(cost[i-1],cost[i-2])
   return cost[-1]
```
