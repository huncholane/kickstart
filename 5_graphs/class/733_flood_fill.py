from typing import List


class Solution:
    """BFS based solution using visited template"""

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        width, height = len(image), len(image[0])

        # Gets left,right,up,down if in bounds
        def get_adj(x, y):
            adj = []
            if x > 0:
                adj.append((x - 1, y))
            if x < width - 1:
                adj.append((x + 1, y))
            if y > 0:
                adj.append((x, y - 1))
            if y < height - 1:
                adj.append((x, y + 1))
            return adj

        # Perform bfs on everything with the original color
        visited = [[False] * height for _ in range(width)]
        oc = image[sr][sc]
        q = [(sr, sc)]
        while q:
            v = q.pop(0)
            image[v[0]][v[1]] = color  # captured so change color
            for w in get_adj(v[0], v[1]):
                if (
                    not visited[w[0]][w[1]] and image[w[0]][w[1]] == oc
                ):  # perform bfs if same color
                    q.append(w)
                    visited[w[0]][w[1]] = True  # mark visited
        return image
