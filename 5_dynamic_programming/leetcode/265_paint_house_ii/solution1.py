class Solution:
    def minCostII(self, costs: list[list[int]]) -> int:
        n, k = len(costs), len(costs[0])
        costs.insert(0, [0] * k)
        for i in range(2, n + 1):
            for j in range(k):
                costs[i][j] += min(costs[i - 1][:j] + costs[i - 1][j + 1 :])
        return min(costs[n])
