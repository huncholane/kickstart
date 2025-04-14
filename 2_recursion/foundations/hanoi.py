import click


def helper(n, src, dst, aux):
    if n == 1:
        print(f"Move from {src} to {dst}")
        return 1
    else:
        result = helper(n - 1, src, aux, dst)
        print(f"Move from {src} to {dst}")
        result += helper(n - 1, aux, dst, src)
        return result + 1


def hanoi(n):
    return helper(n, 1, 2, 3)


@click.command()
@click.argument("n", default=2)
def main(n):
    print(f"{hanoi(n)} total moves")


main()
