import click


def dsrhelper(slate, n, result):
    """Permutations with repitition"""
    if n == 0:
        result.append(slate)
    else:
        for i in range(10):
            dsrhelper(slate + str(i), n - 1, result)


def dsrep(n):
    """Permutations with repitition"""
    result = []
    dsrhelper("", n, result)
    return result


def dsnrhelper(slate, arr, result):
    """Permutations without repitition"""
    if len(arr) == 0:
        result.append(slate)
    else:
        for i in range(len(arr)):
            dsnrhelper(slate + str(arr[i]), arr[:i] + arr[i + 1 :], result)


def dsnorep(n):
    """Permutations without repitition"""
    result = []
    dsnrhelper("", list(range(n)), result)
    return result


@click.command()
@click.argument("n", default=3)
def main(n):
    # strings = dsrep(n)
    # for string in strings:
    #     print(string)
    # print(len(strings), "strings found")
    strings = dsnorep(n)
    for string in strings:
        print(string)
    print(len(strings), "strings found")


main()
