# [72. Edit Distance](https://leetcode.com/problems/edit-distance/)

- Minimize the alignment cost

```text
f(i,j) = min cost of editing/aligning X[1...i] with Y[1...j]
f(i,j) = min(f(i-1,j-1) + (0 if xi=yj or 1), f(i,j-1) + cost of yj, f(i-1,j) + cost of xi)
f(m,n) = f(m-1,n-1)+f(m-1,n)+f(m,n-1)
```

- table is a 2d array of edit distance x0..xi and y0..yj
- Base case is accumulation on row[0] and col[0]

```text
horse and ros example
    r o s
  0 1 2 3
h 1 1 2 3
o 2 2 1 2
r 3 2 2 2
s 4 3 3 2
e 5 4 4 3
```

## Solution 1

- Initialize to (m+1) x (n+1) array to all 0
- Compare with the alignment function above
