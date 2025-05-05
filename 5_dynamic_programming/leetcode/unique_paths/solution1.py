class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[1 for _ in range(n)] for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                left = table[row][col - 1]
                up = table[row - 1][col]
                table[row][col] = left + up
        for row in table:
            print(row)
        return table[m - 1][n - 1]
