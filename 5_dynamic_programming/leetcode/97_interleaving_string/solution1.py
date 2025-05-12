"""
Decision Problem

Two cases:
    1. Rightmost came from s1
    2. Rightmost came from s2

f(m,n) = f(i,j-1) if s3[i+j]==s3[j]
         or
         f(i-1,j) if s3[i+j]==s1[i]

abc,de,abdec
│     d e
│   T F F
│ a T T T
│ b F F T
│ c F F T

aabcc,dbbca,aadbbcbcac
│     d b b c a
│   T F F F F F
│ a T F F F F F
│ a T T T T T F
│ b F T T F T F
│ c F F T T T T
│ c F F F T F T
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        table = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        table[0][0] = True
        for i in range(1, m + 1):
            if s3[i - 1] == s1[i - 1]:
                table[i][0] = True
            else:
                break
        for j in range(1, n + 1):
            if s3[j - 1] == s2[j - 1]:
                table[0][j] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if table[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    table[i][j] = True
                if table[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    table[i][j] = True

        return table[m][n]
