import random


def helper(arr, l, r, target):
    if l > r:
        return
    mid = (l + r) // 2
    if arr[mid] == target:
        return mid
    elif target < mid:
        return helper(arr, l, mid - 1, target)
    else:
        return helper(arr, mid + 1, r, target)


def bsearch(arr, target):
    """O(nlogn)"""
    return helper(arr, 0, len(arr) - 1, target)


n = 10
target = random.randint(0, n)
arr = [random.randint(0, n) for i in range(n)]
arr.sort()
print(arr)
i = bsearch(arr, target)
print(f"found {target} at index {i}")
