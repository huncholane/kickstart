import math
import random
import time


def radixsort(arr):
    l = arr[0]
    r = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < l:
            l = arr[i]
        elif arr[i] > r:
            r = arr[i]
    d = int(math.log(r, 10)) + 1
    for di in range(d):
        aux = [[] for _ in range(10)]
        for num in arr:
            num -= l
            lsd = int(num / math.pow(10, di)) % 10
            aux[lsd].append(num)
        i = 0
        for nums in aux:
            for num in nums:
                arr[i] = num + l
                i += 1


if __name__ == "__main__":
    n = 5
    arr = [random.randint(-300, 300) for i in range(n)]
    print(arr)

    start = time.time()
    radixsort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
