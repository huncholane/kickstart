"""
Build a parse tree
v1+v2*v3-v4...vn+1
n operators, n+1 numbers

num parse trees exponential in n
f(n) = sum(f(i-1)*f(n-1)) [1,n] = nth catalan number
"""


def helper(s: str, i: int, j: int) -> list[int]:
    if s[i : j + 1].isdigit():
        return [int(s[i : j + 1])]
    res: list[int] = []
    for idx in range(i, j + 1):
        if not s[idx].isdigit():
            lres = helper(s, i, idx - 1)
            rres = helper(s, idx + 1, j)
            for lval in lres:
                for rval in rres:
                    if s[idx] == "+":
                        res.append(lval + rval)
                    elif s[idx] == "-":
                        res.append(lval - rval)
                    else:
                        res.append(lval * rval)
    return res


class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        return helper(expression, 0, len(expression) - 1)
