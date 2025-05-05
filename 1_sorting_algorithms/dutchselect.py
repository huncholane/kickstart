import random


def partition(arr, l, r):
    pivot = arr[random.randint(l, r)]
    i, j, k = l, l, r
    while j <= k:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] == pivot:
            j += 1
        else:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
    return i, k


def helper(arr, l, r, target):
    if l >= r:
        return arr[l]
    pl, pr = partition(arr, l, r)
    if pl <= target <= pr:
        return arr[target]
    elif target < pl:
        return helper(arr, l, pl - 1, target)
    else:
        return helper(arr, pr + 1, r, target)


def dutchselect(arr, k):
    n = len(arr)
    if k > n:
        return
    return helper(arr, 0, n - 1, n - k)


n = 10
k = 11
arr = [random.randint(0, n) for _ in range(n)]
print(arr)
answer = dutchselect(arr, k)
print("Answer:", answer)
arr.sort()
print(arr)
print("Correct:", arr[len(arr) - k])
