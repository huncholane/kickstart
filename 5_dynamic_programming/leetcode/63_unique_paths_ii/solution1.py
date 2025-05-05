class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # top-left base case
        if grid[0][0] == 1:
            return 0
        else:
            grid[0][0] = 1

        # first row and first col: set 1s until unreachable
        # then set to 0s
        for i in range(1, m):
            if grid[i][0] == 1:
                for x in range(i, m):
                    grid[x][0] = 0
                break
            grid[i][0] = 1
        for j in range(1, n):
            if grid[0][j] == 1:
                for y in range(j, n):
                    grid[0][y] = 0
                break
            grid[0][j] = 1

        # accumulate and set obstacles to 0
        for row in range(1, m):
            for col in range(1, n):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                else:
                    left = grid[row][col - 1]
                    up = grid[row - 1][col]
                    grid[row][col] = left + up
        return grid[m - 1][n - 1]
