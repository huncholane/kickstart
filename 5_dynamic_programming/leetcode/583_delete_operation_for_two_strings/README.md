# [583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)

- **Minimization Problem**

```text
  m by n table
  m+n = inserts + deletes + 2*matches + 2*mismatches

  right -> insert from string 2 -> 1
  down -> delete from string 1 -> 1
  diag -> substitute or match -> 0 or INF

  Minimize insertions and deletions, no substitutions
  or make the cost of substitution unreasonably high
  so the algorithm ignores it

  Think of insert as a reverse delete

      s e a
    0 1 2 3 
  e 1 2 1 2
  a 2 3 2 1
  t 3 4 3 2

      l e e t
    0 1 2 3 4
  b 1 2 3 4 5
  e 2 3 2 3 4
  a 3 4 3 4 5
  t 4 5 4 5 4
```

## Solution 1 - O(nm)
