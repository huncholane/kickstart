from typing import List
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counts = {}
        # Gather counts O(n)
        for i in range(n):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1
        nums = [num for num in counts.keys()]

        # Lomuto partition to put higher count on the left
        def partition(l, r):
            pi = random.randint(l, r)
            nums[l], nums[pi] = nums[pi], nums[l]
            i = l
            for j in range(l + 1, r + 1):
                if counts[nums[j]] > counts[nums[l]]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[i] = nums[i], nums[l]
            return i

        # Quick select to get target, not a full sort
        # O(n) on average
        target = k - 1

        def qs(l, r):
            pi = partition(l, r)
            if target < pi:
                qs(l, pi - 1)
            elif target > pi:
                qs(pi + 1, r)
            else:
                return

        qs(0, len(nums) - 1)
        return nums[:k]
