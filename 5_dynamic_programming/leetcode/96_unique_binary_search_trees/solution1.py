"""
Counting Problem
Same as well formed parenthesis problem

f(n) = #structurally unique BSTs build out of n
       consecutive integers
f(n) = sum(f(i-1)*f(n-i))
f(n) = f(0)*f(n-1)+f(1)*f(n-2)+...+f(n-1)*f(0)

n=5
│ 1 1 2 5
"""


class Solution:
    def numTrees(self, n: int) -> int:
        table = [0] * (n + 1)
        table[0] = 1
        for i in range(1, n + 1):
            for root in range(1, i + 1):
                table[i] += table[root - 1] * table[i - root]
        return table[n]
