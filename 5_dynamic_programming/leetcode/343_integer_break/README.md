# [343. Integer Break/Rod Cutting](https://leetcode.com/problems/integer-break/)

- **Optimization Problem**

## Breakdown

```text
2 -> 1+1                1X1=1
3 -> 1+1+1|2+1          2*1=2
4 -> 1+1+1+1|1+1+2|2+2  2*2=4
5 -> 1+1+1+1+1|1+1+1+2| 2*2*1=4
     1+2+2

f(i) = best of the previous multiplications or itself
for example on 10:
0 -> 0
1 -> 1
2 -> 2
3 -> 3|1*2 -> 3
4 -> 4|1*3|2*2 -> 4
5 -> 5|1*4|2*3 -> 6
6 -> 6|1*6|2*4|3*3 -> 9 # use results, not the actual index
7 -> 7|1*9|2*6|3*4 -> 12
8 -> 8|1*12|2*9|3*6|4*4 -> 18
9 -> 9|1*18|2*12|3*9|4*6 -> 27
10 -> 9|1*27|2*18|3*12|4*9|6*6 -> 36 # first best = n-1, special case
```
