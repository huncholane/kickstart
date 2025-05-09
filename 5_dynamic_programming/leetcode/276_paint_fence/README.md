# [276. Paint Fence](https://leetcode.com/problems/paint-fence/)

## Breakdown

```text
f(i, k) = number of ways to paint the same as last time and not last time
f(i, k) = s(i, k)+d(i, k)

Secondary functions
s(i, k) = d(i-1, k)
d(i, k) = f(i-1, k)*(k-1)
```
