"""
Two words with m and n lengths

Reward for match = 1
mismatch         = 0
insertion        = 0
deletion         = 0

f(i,j) = length of LCS of x1...xi and y1...yj
    | f(i-1,j)
max | f(i,j-1)
    | f(i-1,j-1) + 1 if xi==yi

ex frog and dog:
    f r o g
  0 0 0 0 0
d 0 0 0 0 0
o 0 0 0 1 0
g 0 0 0 1 2

ex abcde and ace
    a b c d e
  0 0 0 0 0 0
a 0 1 1 1 1 1
c 0 1 1 2 2 2
e 0 1 1 1 1 3
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        table = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                table[i][j] = max(
                    table[i - 1][j],
                    table[i][j - 1],
                    table[i - 1][j - 1] + 1 if text1[i - 1] == text2[j - 1] else 0,
                )
        return table[m][n]
