import click


@click.command()
@click.argument("n", default=4)
def main(n):
    slate, result = [], []
    seen_cols = set()
    seen_d1 = set()
    seen_d2 = set()

    def create_solution():
        mat = []
        for queen in slate:
            row = ""
            for col in range(n):
                if col == queen:
                    row += "Q"
                else:
                    row += "."
            mat.append(row)
        return mat

    def helper(row):
        if len(slate) == n:
            result.append(create_solution())
            return
        for col in range(n):
            d1 = row - col
            d2 = row + col
            if col in seen_cols or d1 in seen_d1 or d2 in seen_d2:
                continue

            slate.append(col)
            seen_cols.add(col)
            seen_d1.add(d1)
            seen_d2.add(d2)

            helper(row + 1)

            slate.pop()
            seen_cols.remove(col)
            seen_d1.remove(d1)
            seen_d2.remove(d2)

    helper(0)

    for res in result:
        for row in res:
            print(row)
        print("-" * n * 2)
    print(len(result), "total combinations")


main()
