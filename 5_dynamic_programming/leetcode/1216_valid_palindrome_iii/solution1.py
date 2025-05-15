class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        table = [[0] * n for _ in range(n)]
        for i in range(len(s)):
            table[i][i] = 1
        for row in range(n - 1, -1, -1):
            for col in range(row + 1, n):
                if s[row] == s[col]:
                    table[row][col] = table[row + 1][col - 1] + 2
                else:
                    table[row][col] = max(table[row + 1][col], table[row][col - 1])
        return table[0][n - 1] >= n - k
