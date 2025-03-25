"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

nums = [1, 2, 2]

slate, res = [], []
n = len(nums)


def helper(i):
    if i == n:
        res.append(slate[:])
        return
    j, count = i, 0
    while j < n and nums[j] == nums[i]:
        count += 1
        j += 1
    # exclude
    helper(i + count)
    # include
    for _ in range(count):
        slate.append(nums[i])
        helper(i + count)
    for _ in range(count):
        slate.pop()


helper(0)

for r in res:
    print(r)
