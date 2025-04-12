from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort O(nlogn)
        nums.sort()
        n = len(nums)

        # Function that gets all the two sums within range [l,r] O(n)
        def two_sum(l, r, target):
            res = []
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            return res

        # Iterate array and join two sums for the compliment of index O(n2)
        res = []
        i = 0
        while i < n - 2:
            for pair in two_sum(i + 1, n - 1, -nums[i]):
                res.append([nums[i]] + pair)
            i += 1
            while i < n - 2 and nums[i] == nums[i - 1]:
                i += 1
        return res
