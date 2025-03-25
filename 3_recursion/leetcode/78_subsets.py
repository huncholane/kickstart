"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

nums = [1, 2, 3]

slate, res = [], []
n = len(nums)


def helper(i):
    # Base case
    if i == n:
        res.append(slate[:])
        return
    # exclude
    helper(i + 1)
    # include
    slate.append(nums[i])
    helper(i + 1)
    slate.pop()


helper(0)

for r in res:
    print(r)
