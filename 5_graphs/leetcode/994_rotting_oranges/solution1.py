from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Make get adj function
        n, m = len(grid), len(grid[0])

        def get_adj(x, y):
            adj = []
            if x > 0:
                adj.append((x - 1, y))
            if x < n - 1:
                adj.append((x + 1, y))
            if y > 0:
                adj.append((x, y - 1))
            if y < m - 1:
                adj.append((x, y + 1))
            return adj

        # Simplify grid access
        def get_grid(x, y):
            return grid[x][y]

        def set_grid(x, y, val):
            grid[x][y] = val

        # Loop through all and mark newly infected as 3 to prevent marking all on first round
        def infect():
            changed = False
            has_uninfected = False
            for i in range(n):
                for j in range(m):
                    if get_grid(i, j) == 2:
                        for neighbor in get_adj(i, j):
                            if get_grid(*neighbor) == 1:
                                changed = True
                                set_grid(*neighbor, 3)
                    if get_grid(i, j) == 1:
                        has_uninfected = True
            return changed, has_uninfected

        # Now mark as 2
        def update():
            for i in range(n):
                for j in range(m):
                    if get_grid(i, j) == 3:
                        set_grid(i, j, 2)

        minutes = 0
        while True:
            changed, has_uninfected = infect()
            if changed:
                minutes += 1
                update()
            elif has_uninfected:
                return -1
            else:
                return minutes
