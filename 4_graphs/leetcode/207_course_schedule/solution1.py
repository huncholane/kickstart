from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build directed graph
        adj = {}
        for e in prerequisites:
            if e[1] in adj:
                adj[e[1]].append(e[0])
            else:
                adj[e[1]] = [e[0]]

        # Initialize dfs with book keeping
        visited = set()
        arrival = {}
        departure = {}
        timestamp = 0

        # Define function to detect cycles
        def dfs(node):
            nonlocal timestamp
            arrival[node] = timestamp
            timestamp += 1
            visited.add(node)
            for neighbor in adj.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                else:
                    # Seen, back edge if dst does not have departure set
                    if neighbor not in departure:
                        return True
            departure[node] = timestamp
            timestamp += 1
            return False

        # Detect there are no cycles
        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return False
        return True
