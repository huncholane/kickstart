"""
Build a parse tree
v1+v2*v3-v4...vn+1
n operators, n+1 numbers

num parse trees exponential in n
f(n) = sum(f(i-1)*f(n-1)) [1,n] = nth catalan number
"""

Memo = dict[tuple[int, int], list[int]]


def helper(s: str, i: int, j: int, memo: Memo) -> list[int]:
    if (i, j) in memo:
        return memo[(i, j)]
    if s[i : j + 1].isdigit():
        memo[(i, j)] = [int(s[i : j + 1])]
        return [int(s[i : j + 1])]
    res: list[int] = []
    for idx in range(i, j + 1):
        if not s[idx].isdigit():
            lres = helper(s, i, idx - 1, memo)
            rres = helper(s, idx + 1, j, memo)
            for lval in lres:
                for rval in rres:
                    if s[idx] == "+":
                        res.append(lval + rval)
                    elif s[idx] == "-":
                        res.append(lval - rval)
                    else:
                        res.append(lval * rval)
    memo[(i, j)] = res
    return res


class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo: dict[tuple[int, int], list[int]] = {}
        return helper(expression, 0, len(expression) - 1, memo)
