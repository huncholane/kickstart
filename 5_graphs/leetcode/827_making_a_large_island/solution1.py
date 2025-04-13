from typing import List
from collections import defaultdict


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        islands = defaultdict(int)
        index = 2  # 2 and up won't cause problems

        def dfs(r, c):
            nonlocal index
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = index
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

        # Label each island and store size
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    islands[index] = dfs(r, c)
                    index += 1

        # Lookup neighbors for each 0
        largest = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    area = 1
                    seen = set()
                    for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] in seen:
                            continue
                        seen.add(grid[i][j])
                        area += islands.get(grid[i][j], 0)
                    largest = max(area, largest)
        return largest if largest else n * n
