class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        R, B, G = 0, 1, 2
        for i in range(1, len(costs)):
            costs[i][R] = costs[i][R] + min(costs[i - 1][B], costs[i - 1][G])
            costs[i][B] = costs[i][B] + min(costs[i - 1][R], costs[i - 1][G])
            costs[i][G] = costs[i][G] + min(costs[i - 1][R], costs[i - 1][B])
        return min(costs[-1])
