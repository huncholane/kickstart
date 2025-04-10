from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Construct graph
        adj = {}
        for e in prerequisites:
            if e[1] not in adj:
                adj[e[1]] = [e[0]]
            else:
                adj[e[1]].append(e[0])

        # Initialize dfs
        visited = {}
        topsort = []
        timestamp = 0

        # Detect update visited data
        def dfs(node):
            nonlocal timestamp
            visited[node] = {"arrival": timestamp, "departure": None}
            timestamp += 1
            for neighbor in adj.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                else:
                    if visited[neighbor]["departure"] is None:
                        return True
            visited[node]["departure"] = timestamp
            timestamp += 1
            topsort.append(node)
            return False

        # Run dfs and return the reversed topsort
        res = []
        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return []
        topsort.reverse()
        return topsort
