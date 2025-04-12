from typing import List


class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]
    ) -> List[int]:
        def intersect2(arr1, arr2):
            i, j = 0, 0
            res = []
            while i < len(arr1) and j < len(arr2):
                if arr1[i] == arr2[j]:
                    res.append(arr1[i])
                    i += 1
                    j += 1
                elif arr1[i] > arr2[j]:
                    j += 1
                else:
                    i += 1
            return res

        res = intersect2(arr1, arr2)
        res = intersect2(res, arr3)
        return res
