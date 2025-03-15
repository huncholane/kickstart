import random
import time


def countingsort(arr):
    # Initialize aux
    l = arr[0]
    r = arr[0]
    for i in range(len(arr)):
        if arr[i] < l:
            l = arr[i]
        elif arr[i] > r:
            r = arr[i]
    k = r - l
    aux = [0] * (k + 1)
    for num in arr:
        aux[num - l] += 1
    # Copy aux into arr
    i = 0
    for num in range(k + 1):
        while aux[num] > 0:
            arr[i] = num - l
            i += 1
            aux[num] -= 1


if __name__ == "__main__":
    n = 5
    arr = [random.randint(0, 5) for i in range(n)]

    start = time.time()
    countingsort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
