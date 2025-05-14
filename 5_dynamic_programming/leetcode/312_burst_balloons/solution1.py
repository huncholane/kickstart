class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        n = len(nums)
        table = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    table[i][j] = max(
                        table[i][j],
                        table[i][k] + table[k][j] + nums[i] * nums[j] * nums[k],
                    )
        return table[0][n - 1]
