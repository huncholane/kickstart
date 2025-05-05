class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        for i in range(1, n):
            for j in range(i + 1):
                if i == j:
                    triangle[i][j] += triangle[i - 1][j - 1]
                elif j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        return min(triangle[-1])
