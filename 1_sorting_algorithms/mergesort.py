import random
import time


def mergesort_helper(arr, start, end):
    # Leaf node
    if start == end:
        return
    # Internal node worker
    mid = int((start + end) / 2)
    mergesort_helper(arr, start, mid)
    mergesort_helper(arr, mid + 1, end)
    i, j = start, mid + 1
    aux = []
    while i <= mid and j <= end:
        if arr[j] <= arr[i]:
            aux.append(arr[j])
            j += 1
        else:
            aux.append(arr[i])
            i += 1
    # Gather phase
    while i <= mid:
        aux.append(arr[i])
        i += 1
    while j <= end:
        aux.append(arr[j])
        j += 1
    # Copy phase
    for i, num in enumerate(aux):
        arr[start + i] = num


def mergesort(arr):
    """O(nlogn) very fast but requires extra memory"""
    mergesort_helper(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    n = 50000000
    arr = [random.randint(0, n) for i in range(n)]

    start = time.time()
    mergesort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
