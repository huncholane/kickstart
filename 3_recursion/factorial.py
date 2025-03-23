"""Used in permutations"""


def fact(n):
    """O(n)"""
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def fact_iter(n):
    """O(n)"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(fact(6))
print(fact_iter(5))
