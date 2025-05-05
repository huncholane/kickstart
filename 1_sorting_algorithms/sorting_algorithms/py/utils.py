import random


def gen_arr(n):
    return [random.randint(0, n) for _ in n]


def swap(arr, i1, i2):
    tmp = arr[i2]
    arr[i2] = arr[i1]
    arr[i1] = tmp
