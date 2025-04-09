from typing import List
import random


class Solution:
    """Uses quick select with a 3 way partition to combat repetitive numbers and
    a random pivot to combat already in order."""

    def findKthLargest(self, nums: List[int], k: int) -> int:
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
                else:
                    nums[j], nums[k] = nums[k], nums[j]
                    k -= 1
            return i, k

        target = len(nums) - k

        def qs(l, r):
            pl, pr = part3(l, r)
            if target < pl:
                return qs(l, pl - 1)
            elif target > pr:
                return qs(pr + 1, r)
            else:
                # All the numbers in range [pl,pr] are the same
                return nums[pl]

        # Quick select
        return qs(0, len(nums) - 1)
