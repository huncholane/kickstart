class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m == 0:
            return n
        if n == 0:
            return m
        table = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            table[i][0] = i
        for j in range(1, n + 1):
            table[0][j] = j
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                insertion = table[row][col - 1] + 1
                deletion = table[row - 1][col] + 1
                replacement = table[row - 1][col - 1]
                if word1[row - 1] != word2[col - 1]:
                    replacement += 1
                table[row][col] = min(insertion, deletion, replacement)
        return table[m][n]
