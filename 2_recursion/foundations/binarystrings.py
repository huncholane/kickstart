"""
Time: O(2^n)
Space: O(2^n)
Decrease and Conquer
Breadth first search, checks everything at each level
def binarystrings(n):
    if n==1:
        return ["0","1"]
    else: #n>1
        prev = binarystrings(n-1)
        result = []
        for s in prev:
            result.append(s+"0")
            result.append(s+"1")
        return result

Divide and Conquer
Depth first search, goes to the end of each branch first
Time: O(2^n)
Space: O(n)
def binarystrings(n, prefix):
    if n==1:
        print ["0", "1"]
    print "0"+binarystrings(n-1)
    print "1"+binarystrings(n-1)
"""

import click


def helper(slate, n):
    if n == 0:
        print(slate)
        return
    helper(slate + "0", n - 1)
    helper(slate + "1", n - 1)


def binarstrings2(n):
    helper("", n)


def binarystrings(n):
    if n == 1:
        return ["0", "1"]
    prev = binarystrings(n - 1)
    result = []
    for s in prev:
        result.append(s + "0")
        result.append(s + "1")
    return result


@click.command()
@click.argument("n", default=3)
def main(n):
    strings = binarystrings(n)
    for s in strings:
        print(s)
    print(f"{len(strings)} total possible combinations")
    binarstrings2(n)


main()
