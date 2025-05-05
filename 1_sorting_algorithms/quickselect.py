import random

"""
def partition(arr, l, r):
    pivot = arr[random.randint(l, r - 1)]
    i, j = l - 1, r + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
"""




def lumoto_partition(arr, l, r):
    p = random.randint(l, r)
    arr[l], arr[p] = arr[p], arr[l]
    i = l
    for j in range(l + 1, r + 1):
        if arr[j] < arr[l]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[i] = arr[i], arr[l]
    return i


def hoare_partition(arr, l, r):
    pivot = arr[random.randint(l, r)]
    i, j = l - 1, r + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quickselect(arr, l, r, target):
    if l >= r:
        return arr[l]
    pi = lumoto_partition(arr, l, r)
    if pi == target:
        return arr[pi]
    elif target < pi:
        return quickselect(arr, l, pi - 1, target)
    else:
        return quickselect(arr, pi + 1, r, target)


def kth_largest(arr, k):
    """Also known as quick select"""
    target = len(arr) - k
    return quickselect(arr, 0, len(arr) - 1, target)


n = 10
k = 2
arr = [random.randint(0, n) for _ in range(n)]
print(arr)
answer = kth_largest(arr, k)
print("Answer:", answer)
arr.sort()
print(arr)
print("Correct:", arr[len(arr) - k])
