from typing import List


class Solution:
    """Template solution using bfs to count connected components"""

    def numIslands(self, grid: List[List[str]]) -> int:
        width, height = len(grid), len(grid[0])

        def get_adj(x, y):
            adj = []
            if x > 0 and grid[x - 1][y] == "1":
                adj.append((x - 1, y))
            if x < width - 1 and grid[x + 1][y] == "1":
                adj.append((x + 1, y))
            if y > 0 and grid[x][y - 1] == "1":
                adj.append((x, y - 1))
            if y < height - 1 and grid[x][y + 1] == "1":
                adj.append((x, y + 1))
            return adj

        visited = [[False] * height for _ in range(width)]

        def bfs(s):
            visited[s[0]][s[1]] = True
            q = [s]
            while q:
                v = q.pop(0)
                adj = get_adj(v[0], v[1])
                for w in get_adj(v[0], v[1]):
                    if not visited[w[0]][w[1]]:
                        visited[w[0]][w[1]] = True
                        q.append(w)

        islands = 0
        for x in range(width):
            for y in range(height):
                if not visited[x][y] and grid[x][y] == "1":
                    bfs((x, y))
                    islands += 1
        return islands
