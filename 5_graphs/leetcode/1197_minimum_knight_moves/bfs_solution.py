class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        def get_adj(x, y):
            return [
                (x - 2, y - 1),
                (x - 2, y + 1),
                (x + 2, y - 1),
                (x + 2, y + 1),
                (x - 1, y - 2),
                (x - 1, y + 2),
                (x + 1, y - 2),
                (x + 1, y + 2),
            ]

        visited = {(0, 0): 0}
        q = [(0, 0)]
        search_for = (x, y)
        while q:
            node = q.pop(0)
            if node == search_for:
                return visited[node]
            for neighbor in get_adj(*node):
                if neighbor not in visited:
                    visited[neighbor] = visited[node] + 1
                    q.append(neighbor)
