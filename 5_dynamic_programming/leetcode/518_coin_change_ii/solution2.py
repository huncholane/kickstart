"""
Space optimized

amount=5,coins=[1,2,5]
│ 1 1 2 2 3 4
"""


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        table = [0] * (amount + 1)
        table[0] = 1
        for i in range(1, n + 1):
            for a in range(1, amount + 1):
                if a >= coins[i - 1]:
                    table[a] += table[a - coins[i - 1]]
        return table[amount]
