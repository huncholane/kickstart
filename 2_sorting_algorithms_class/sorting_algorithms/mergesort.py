import random
import time

from test import test_sorting


def helper(arr, l, r):
    if l == r:
        return
    mid = (l + r) // 2
    helper(arr, l, mid)
    helper(arr, mid + 1, r)
    aux = []
    i, j = l, mid + 1
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            aux.append(arr[i])
            i += 1
        else:
            aux.append(arr[j])
            j += 1
    while i <= mid:
        aux.append(arr[i])
        i += 1
    while j <= r:
        aux.append(arr[j])
        j += 1
    arr[l : r + 1] = aux


def mergesort(arr):
    helper(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    n = 5
    arr = [random.randint(0, 100) for i in range(n)]
    print(arr)

    start = time.time()
    mergesort(arr)
    print(time.time() - start, "seconds")
    try:
        test_sorting(mergesort)
        print(f"\033[32mSuccess\033[0m")
    except AssertionError as e:
        print(f"\033[31mFailed: {e}\033[0m")
