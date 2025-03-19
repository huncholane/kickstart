import random


def lbsearch(arr, l, r, val):
    if l > r:
        return r
    mid = (l + r) // 2
    if val <= arr[mid]:
        return lbsearch(arr, l, mid - 1, val)
    else:
        return lbsearch(arr, mid + 1, r, val)


n = 5
find = random.randint(0, 100)
arr = [random.randint(0, 100) for _ in range(n)]
arr.sort()
print(arr)
print(f"Search for {find}")
i = lbsearch(arr, 0, len(arr) - 1, find)
if i is None:
    print(f"No index found for {find}")
else:
    print(f"The closest index to the left of {find} is {i} ({arr[i]})")
