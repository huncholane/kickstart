def subsets(n):
    """O(n) with 2*subsets(n-1), subsets(n-1)+subsets(n-1) = O(n2)"""
    if n == 0:
        return 1
    else:
        return 2 * subsets(n - 1)


def subsets_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= 2
    return result


print(subsets(50))
print(subsets_iter(50))
