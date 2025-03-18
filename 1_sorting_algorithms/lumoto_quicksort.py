import random
import time


def partition(arr, l, r):
    pi = random.randint(l, r)
    arr[pi], arr[l] = arr[l], arr[pi]
    i, j = l, l + 1
    for j in range(l + 1, r + 1):
        if arr[j] < arr[l]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[l] = arr[l], arr[i]
    return i


def helper(arr, l, r):
    if l >= r:
        return
    pi = partition(arr, l, r)
    helper(arr, l, pi - 1)
    helper(arr, pi + 1, r)


def lumoto_quicksort(arr):
    helper(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    n = 10
    arr = [random.randint(0, n) for i in range(n)]
    print(arr)

    start = time.time()
    lumoto_quicksort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
