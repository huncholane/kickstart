import argparse

import click


def memo_helper(n, memo):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    result = memo_helper(n - 2, memo) + memo_helper(n - 1, memo)
    memo[n] = result
    return result


def fib_memo(n):
    """Cache results into map"""
    memo = {}
    return memo_helper(n, memo)


def add_helper(n, b1, b2):
    if n == 0:
        return b1
    return add_helper(n - 1, b2, b1 + b2)


def fib_add(n):
    """Additive O(n) with no aux"""
    return add_helper(n, 0, 1)


@click.command()
@click.argument("n", default=5)
def main(n):
    print(fib_memo(n))
    print(fib_add(n))


main()
