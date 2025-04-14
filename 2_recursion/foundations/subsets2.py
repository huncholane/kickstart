import click


def subsetshelper(slate, arr, result):
    if len(arr) == 0:
        result.append(slate)
    else:
        subsetshelper(slate, arr[1:], result)
        subsetshelper(slate + [arr[0]], arr[1:], result)


def subsets(n):
    result = []
    subsetshelper([], list(range(n)), result)
    return result


@click.command()
@click.argument("n", default=3)
def main(n):
    result = subsets(n)
    for subset in result:
        print(subset)
    print(len(result), "subsets found")


main()
