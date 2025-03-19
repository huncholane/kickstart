import random


def bsearch(arr, l, r, val):
    if l > r:
        return
    mid = (l + r) // 2
    if arr[mid] == val:
        return mid
    elif val < arr[mid]:
        return bsearch(arr, l, mid - 1, val)
    else:
        return bsearch(arr, mid + 1, r, val)


n = 10
find = 8
arr = [random.randint(0, n) for _ in range(n)]
arr.sort()
print(arr)
print(f"Search for {find}")
i = bsearch(arr, 0, len(arr) - 1, find)
if i is None:
    print(f"No index found for {find}")
else:
    print(f"The index for {find} is {i}")
