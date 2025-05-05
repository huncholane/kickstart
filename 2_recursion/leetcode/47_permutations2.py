"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

nums = [1, 1, 2]

slate, res = [], []
n = len(nums)
nums.sort()


def helper(i):
    # Base case
    if i == n:
        res.append(slate[:])
        return
    # Recursive case
    seen = set()
    for pick in range(i, n):
        if nums[pick] in seen:
            continue
        seen.add(nums[pick])
        nums[i], nums[pick] = nums[pick], nums[i]
        slate.append(nums[i])
        helper(i + 1)
        slate.pop()
        nums[i], nums[pick] = nums[pick], nums[i]


helper(0)

for r in res:
    print(r)
