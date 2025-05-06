class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        nums.append(0)
        for i in range(len(nums) - 2, -1, -1):
            nums[i + 1] = nums[i]
        nums[0] = 0
        for i in range(2, n + 1):
            nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])
        return nums[n]
