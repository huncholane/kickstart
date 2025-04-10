import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def part3(l, r):
            pivot = nums[random.randint(l, r)]
            i, j, k = l, l, r
            while j <= k:
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                elif nums[j] == pivot:
                    j += 1
                else:  # nums[j]>pivot
                    nums[j], nums[k] = nums[k], nums[j]
                    k -= 1
            return i, k

        def helper(l, r):
            if l >= r:
                return
            pl, pr = part3(l, r)
            helper(l, pl - 1)
            helper(pr + 1, r)

        helper(0, len(nums) - 1)
        return nums
