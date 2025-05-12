"""
Counting Problem

t = target, n = size of nums
f(t) = #ways of constructing amount t using the nums
f(t) = sum(f(t-nums[i])) for i [0,n]
ex nums = [1,2]:
    f(t) = f(t-1) + f(t-2)
"""


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        table = [0] * (target + 1)
        table[0] = 1
        for t in range(1, target + 1):
            for num in nums:
                if t >= num:
                    table[t] += table[t - num]
        return table[target]
