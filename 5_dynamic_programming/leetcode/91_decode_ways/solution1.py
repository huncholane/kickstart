"""
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
│   1 1 1 0 6
│ 1 1 2 3 2 2


Example 121025763:
│   1 2 1 0 2 5 7 6 3
│ 1 1 2 3 2 2 4 4 4 4


Example 540432034:
│   5 4 0 4 3 2 0 3 4
│ 1 1 1 0 0 0 0 0 0 0
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        table = [0] * (n + 1)
        table[0] = 1
        table[1] = 0 if s[0] == "0" else 1
        for i in range(2, n + 1):
            last = int(s[i - 1])
            penultimate = int(s[i - 2])
            if last > 0:
                table[i] += table[i - 1]
            if (penultimate == 1 and 0 <= last <= 9) or (
                penultimate == 2 and 0 <= last <= 6
            ):
                table[i] += table[i - 2]
        print(" ", " ".join(s))
        print(" ".join([str(num) for num in table]))
        return table[n]
