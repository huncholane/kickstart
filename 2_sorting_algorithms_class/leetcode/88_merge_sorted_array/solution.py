from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Sort the array in place O(n)
        # Do in reverse order to add to the back of the first array
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            back_i = i + j + 1
            if nums1[i] > nums2[j]:
                nums1[back_i] = nums1[i]
                i -= 1
            else:
                nums1[back_i] = nums2[j]
                j -= 1

        # Handle leftovers
        while j >= 0:
            nums1[j] = nums2[j]
            j -= 1
