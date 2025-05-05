from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Gather compliments using a hash map O(n)
        # We know the compliment will show up eventually
        # Do it in place to prevent duplicates
        cmap = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in cmap:
                return [i, cmap[c]]
            cmap[nums[i]] = i
