import random
import time


def countingsort(arr):
    # Initialize aux
    k = max(arr)
    aux = [0] * (k + 1)
    for num in arr:
        aux[num] += 1
    # Copy aux into arr
    i = 0
    for num in range(k + 1):
        while aux[num] > 0:
            arr[i] = num
            i += 1
            aux[num] -= 1


if __name__ == "__main__":
    n = 5
    arr = [random.randint(0, 5) for i in range(n)]

    start = time.time()
    countingsort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
