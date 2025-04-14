nums = [1, 2, 3]

slate, res = [], []
n = len(nums)


def helper(i):
    if i == n:
        res.append(slate[:])
        return
    for pick in range(i, n):
        nums[i], nums[pick] = nums[pick], nums[i]
        slate.append(nums[i])
        helper(i + 1)
        slate.pop()
        nums[i], nums[pick] = nums[pick], nums[i]


helper(0)

for r in res:
    print(r)
