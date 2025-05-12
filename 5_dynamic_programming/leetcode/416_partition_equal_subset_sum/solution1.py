"""
Decision Problem

_ _ _ _ _ _ _ _
Is there a subset summing to k?

DP
f(n,k) = True if subset summing to k
f(n,k) = f(n-1,k) or f(n-1,k-nth num)
         exclude     include
n in [0,n]
k in [0,total/2]

nums=[1,2,3,4], k=5
│   0 1 2 3 4 5
│ 0 T F F F F F
│ 1 T T F F F F
│ 2 T T T T F F
│ 3 T T T T T T
│ 4 T T T T T T


nums[1,2,5], k=4
│   0 1 2 3 4
│ 0 T F F F F
│ 1 T T F F F
│ 2 T T T T F
│ 5 T T T T F
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        n = len(nums)
        k = total // 2

        table = [[True for _ in range(k + 1)] for _ in range(n + 1)]
        for target in range(1, k + 1):
            table[0][target] = False

        for numi in range(1, n + 1):
            row_is_true = True
            for target in range(1, k + 1):
                table[numi][target] = table[numi - 1][target]
                if target >= nums[numi - 1]:
                    table[numi][target] = (
                        table[numi][target] or table[numi - 1][target - nums[numi - 1]]
                    )
                if not table[numi][target]:
                    row_is_true = False
            if row_is_true:
                return True

        return table[n][k]
