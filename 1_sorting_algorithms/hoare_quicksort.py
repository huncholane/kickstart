import random
import time

from utils import swap


def partition(arr, l, r):
    pi = random.randint(l, r)
    arr[pi], arr[l] = arr[l], arr[pi]
    i, j = l + 1, r
    while i <= j:
        if arr[i] <= arr[l]:
            i += 1
        elif arr[j] > arr[l]:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def helper(arr, l: int, r: int):
    # Leaf node
    if l >= r:
        return
    # Internal node worker
    pi = partition(arr, l, r)
    helper(arr, l, pi - 1)
    helper(arr, pi + 1, r)


def hoare_quicksort(arr):
    """Generally O(nlogn) if the partition is random"""
    helper(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    n = 5
    arr = [random.randint(0, n) for i in range(n)]
    print(arr)

    start = time.time()
    hoare_quicksort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
