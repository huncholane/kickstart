class Solution:
    def minCostII(self, costs: list[list[int]]) -> int:
        n, k = len(costs), len(costs[0])
        costs.insert(0, [0] * k)
        INF = 2**31 - 1
        prev_min1, prev_min2 = (0, INF), (0, INF)
        for j in range(k):
            if costs[1][j] < prev_min1[1]:
                prev_min2 = prev_min1
                prev_min1 = (j, costs[1][j])
            elif costs[1][j] < prev_min2[1]:
                prev_min2 = (j, costs[1][j])
        for i in range(2, n + 1):
            min1, min2 = (0, INF), (0, INF)
            for j in range(k):
                if prev_min1[0] == j:
                    costs[i][j] += prev_min2[1]
                else:
                    costs[i][j] += prev_min1[1]
                if costs[i][j] < min1[1]:
                    min2 = min1
                    min1 = (j, costs[i][j])
                elif costs[i][j] < min2[1]:
                    min2 = (j, costs[i][j])
            prev_min1, prev_min2 = min1, min2
        return min(costs[-1])
