# [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

## Solution 1 - Bottom Up Tabulation

- Make diagonal table of 1s up and 1s diagonal

   ```text
   1
   1 1
   1 0 1
   1 0 0 1
   1 0 0 0 1
   ```

- Faster just to initialize nxn to 1
- Start from 2 and set cell to up + upleft
