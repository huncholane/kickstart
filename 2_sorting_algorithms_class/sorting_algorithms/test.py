import random


def assert_in_order(arr):
    pnum = arr[0]
    for num in arr[1:]:
        assert pnum <= num
        pnum = num


def test_sorting(f, times=10, size=10):
    for _ in range(times):
        arr = [random.randint(0, 10) for _ in range(size)]
        f(arr)
        assert_in_order(arr)
