"""
Counting Problem

f(a,i) = sum(f(a-c*coins[i],i-1))

amount=5, coins=[1,2,5]
│   0 1 2 3 4 5
│ 0 1 0 0 0 0 0
│ 1 1 1 1 1 1 1
│ 2 1 1 2 2 3 3
│ 5 1 1 2 2 3 4
"""


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        table = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        for row in range(n + 1):
            table[row][0] = 1
        for i in range(1, n + 1):
            for a in range(1, amount + 1):
                maxcopies = a // coins[i - 1]
                for c in range(maxcopies + 1):
                    table[i][a] += table[i - 1][a - c * coins[i - 1]]

        return table[n][amount]
