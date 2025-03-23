def power(n, k):
    if k == 0:
        return 1
    elif k % 2 == 0:
        half = power(n, k // 2)
        return half * half
    else:
        return n * power(n, k - 1)


def power_iter(n, k):
    result = 1
    for i in range(1, k + 1):
        result *= n
    return result


print(power(2, 3))
print(power_iter(2, 3))
