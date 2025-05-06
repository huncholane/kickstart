class Solution:
    def straight(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        table = [0] + nums
        table[2] = max(table[:3])
        for i in range(2, n + 1):
            table[i] = max(table[i - 1], table[i - 2] + table[i])
        return table[n]

    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        case1 = self.straight(nums[2:-1]) + nums[0]
        case2 = self.straight(nums[1:])
        print(case1, case2)
        return max(case1, case2)
