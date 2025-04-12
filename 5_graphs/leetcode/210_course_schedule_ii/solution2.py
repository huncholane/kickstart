from typing import List


class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1  # b points to a

        taken = [i for i in range(n) if indegree[i] == 0]
        topsort = taken[:]
        while taken:
            node = taken.pop(0)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1  # take prereq class
                if indegree[neighbor] == 0:
                    taken.append(neighbor)
                    topsort.append(neighbor)
        if len(topsort) == n:
            return topsort
        return []
