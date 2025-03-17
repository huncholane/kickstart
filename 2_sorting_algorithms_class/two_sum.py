import random


def brute_force(arr: list, target: int) -> bool:
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return True
    return False


def two_pointer_pass(arr: list, target: int) -> bool:
    """O(nlogn)
    In-place"""
    # presort
    arr.sort()
    n = len(arr)
    i, j = 0, n - 1
    while i < j:
        total = arr[i] + arr[j]
        if total == target:
            return True
        elif total < target:
            i += 1
        else:
            j -= 1
    return False


def hash_map(arr: list, target: int) -> bool:
    """O(n)
    Uses aux"""
    # Hash map
    m = set()
    for num in arr:
        if target - num in m:
            return True
        else:
            m.add(num)
    return False


nums = [random.randint(0, 10) for _ in range(5)]
target = random.randint(0, 10)
print("Target:", target)
print("Nums:", nums)
print("Brute Force:", brute_force(nums, target))
print("Two pointer:", two_pointer_pass(nums.copy(), target))
print("Hash Map:", hash_map(nums.copy(), target))
