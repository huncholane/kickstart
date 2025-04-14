import random
import time


def countingsort(arr):
    # init the array
    low = arr[0]
    high = arr[0]
    n = len(arr)
    for i in range(n):
        if arr[i] < low:
            low = arr[i]
        if arr[i] > high:
            high = arr[i]

    # make array start from 0
    for i in range(n):
        arr[i] -= low
    k = high - low
    aux = [0] * (k + 1)

    # init the auxilary count array
    for i in range(n):
        aux[arr[i]] += 1

    # cummulate the sums to index correctly
    for i in range(1, k + 1):
        aux[i] += aux[i - 1]

    # init output aux
    output = [0] * n

    # put into place in reverse to keep original order
    i = n - 1
    while i >= 0:
        output[aux[arr[i]] - 1] = arr[i]
        aux[arr[i]] -= 1
        i -= 1

    # copy output into original array
    arr[:] = output[:]

    # fix the array back to original values
    for i in range(n):
        arr[i] += low


if __name__ == "__main__":
    n = 10
    arr = [random.randint(-10, n) for i in range(n)]
    print(arr)

    start = time.time()
    countingsort(arr)
    print(time.time() - start, "seconds")
    print(arr)
