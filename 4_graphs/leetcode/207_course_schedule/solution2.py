from typing import List


class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        # Build graph so that course b goes into course a
        # in-degree increments the opposite way
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        # q is a queue of courses with no in-degree
        q = [i for i in range(n) if indegree[i] == 0]
        count = len(q)
        while q:
            node = q.pop(0)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    count += 1
                    q.append(neighbor)

        # We prove that all classes can be taken if there are no nodes with an indegree still
        return count == n
