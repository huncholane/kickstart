from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if not n or not m:
            return 0

        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

        count = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    count = max(count, dfs(r, c))
        return count
