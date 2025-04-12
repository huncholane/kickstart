from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        # Initialize q with all infected
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))

        # Run level order bfs
        minutes = -1
        while q:
            count = len(q)
            minutes += 1
            for _ in range(count):
                x, y = q.popleft()
                if x > 0 and grid[x - 1][y] == 1:
                    grid[x - 1][y] = 2
                    q.append((x - 1, y))
                if x < n - 1 and grid[x + 1][y] == 1:
                    grid[x + 1][y] = 2
                    q.append((x + 1, y))
                if y > 0 and grid[x][y - 1] == 1:
                    grid[x][y - 1] = 2
                    q.append((x, y - 1))
                if y < m - 1 and grid[x][y + 1] == 1:
                    grid[x][y + 1] = 2
                    q.append((x, y + 1))

        # Make sure there are no safe oranges
        for row in grid:
            print(row)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return minutes if minutes > -1 else 0
