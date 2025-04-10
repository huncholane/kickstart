from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # Gather even and odd indices O(n)
        odds, evens = [], []
        for i in range(len(nums)):
            if i % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])

        # Sort evens O(nlogn)
        evens.sort()
        # Sort odds O(nlogn)
        odds.sort(reverse=True)

        # Merge O(n)
        res = []
        n_odd = len(odds)
        n_even = len(evens)
        n = max(n_odd, n_even)
        for i in range(n):
            if i < n_even:
                res.append(evens[i])
            if i < n_odd:
                res.append(odds[i])
        return res
