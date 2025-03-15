import math
import random
import time


def radixsort(arr):
    low, high = arr[0], arr[0]
    for num in arr:
        if num < low:
            low = num
        elif num > high:
            high = num
    exp = 1
    n = len(arr)
    while high // exp > 0:
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1
        for i in range(n):
            arr[i] = output[i]
        exp *= 10


if __name__ == "__main__":
    n = 5
    arr = [random.randint(0, 300) for i in range(n)]
    print(arr, "\n")

    start = time.time()
    radixsort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
