"""
Final optimization - avoid coins > amount

amount=5,coins=[1,2,5]
│ 1 1 2 2 3 4
"""


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        table = [0] * (amount + 1)
        table[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                table[i] += table[i - coin]
        return table[amount]
