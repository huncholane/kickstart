from typing import List


class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        width, height = len(grid), len(grid[0])

        def get_adj(x, y):
            adj = []
            if x > 0 and grid[x - 1][y] == 1:
                adj.append((x - 1, y))
            if x < width - 1 and grid[x + 1][y] == 1:
                adj.append((x + 1, y))
            if y > 0 and grid[x][y - 1] == 1:
                adj.append((x, y - 1))
            if y < height - 1 and grid[x][y + 1] == 1:
                adj.append((x, y + 1))
            return adj

        visited = [[False] * height for _ in range(width)]

        def bfs(s):
            visited[s[0]][s[1]] = True
            q = [s]
            captured = 0
            while q:
                v = q.pop(0)
                captured += 1
                for w in get_adj(v[0], v[1]):
                    if not visited[w[0]][w[1]]:
                        visited[w[0]][w[1]] = True
                        q.append(w)
            return captured

        largest = 0
        for x in range(width):
            for y in range(height):
                if not visited[x][y] and grid[x][y] == 1:
                    largest = max(largest, bfs((x, y)))
        return largest
