import random
import time


def partition(arr, l, r):
    pi = random.randint(l, r)
    arr[r], arr[pi] = arr[pi], arr[r]
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def helper(arr, l, r):
    if l >= r:
        return
    pi = partition(arr, l, r)
    helper(arr, l, pi - 1)
    helper(arr, pi + 1, r)


def lumoto_quicksort(arr):
    n = len(arr)
    helper(arr, 0, n - 1)


if __name__ == "__main__":
    n = 10
    arr = [random.randint(0, n) for i in range(n)]
    print(arr)

    start = time.time()
    lumoto_quicksort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
