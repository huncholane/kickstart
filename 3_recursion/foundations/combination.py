import click
from timer import timeit


def helper(n, k):
    # Edge of pascals triangle
    if n <= 1 or k == 0 or k == n:
        return 1
    return helper(n - 1, k) + helper(n - 1, k - 1)


@timeit
def c(n, k):
    return helper(n, k)


@click.command()
@click.argument("n", default=1)
@click.argument("k", default=1)
def main(n, k):
    print(c(n, k))


main()
