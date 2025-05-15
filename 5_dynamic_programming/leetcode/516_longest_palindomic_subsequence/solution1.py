class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        table = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            table[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    table[i][j] = table[i + 1][j - 1] + 2
                else:
                    left = table[i][j - 1]
                    down = table[i + 1][j]
                    table[i][j] = max(left, down)
        return table[0][n - 1]
