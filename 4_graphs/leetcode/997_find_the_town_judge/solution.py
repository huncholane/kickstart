from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Create graph and initialize indegree O(n)
        outdegree = [0] * (n + 1)
        indegree = [0] * (n + 1)
        for a, b in trust:
            indegree[b] += 1
            outdegree[a] += 1

        # Judge candidate will be the person with the highest indegree O(n)
        judge, highest_trust = 1, 0
        for i in range(n + 1):
            trust = indegree[i]
            if trust > highest_trust:
                judge = i
                highest_trust = trust

        # Check if judge trusts anyone O(1)
        if outdegree[judge] > 0:
            return -1

        # Check if judge is trusted by n-1 people
        if indegree[judge] != n - 1:
            return -1

        return judge
