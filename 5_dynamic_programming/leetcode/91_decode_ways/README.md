# [91. Decode Ways](https://leetcode.com/problems/decode-ways/)

```text
Counting Problem

Keep track of numbers with possible for each step and accumulate

0 means not valid and 27+ means not valid

Cases for last digit:
    - Encoded by itself if [1,9]
    - Encoded with previous if previous is 1
    - Encoded with previous if previous is 2 and last digit is [1,6]

f(n) = Count of #valid decodings of string of length n
f(n) = f(n-1) if last digit [1,9] +
       f(n-2) if penultimate is 1 and last is [0-9] or penultimate is 2 and last is [0-6]


Example 11106:
  1 1 1 0 6
1 1 2 3 2 2


Example 121025763:
  1 2 1 0 2 5 7 6 3
1 1 2 3 2 2 4 4 4 4


Example 540432034:
  5 4 0 4 3 2 0 3 4
1 1 1 0 0 0 0 0 0 0
```
