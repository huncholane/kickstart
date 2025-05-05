class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        cost.extend([0, 0])
        # shift right
        for i in range(len(cost) - 2, -1, -1):
            cost[i + 1] = cost[i]
        # 0..cost..0
        cost[0] = 0
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return cost[-1]
