class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        inf = 2**32
        table = [inf] * (amount + 1)
        table[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    table[i] = min(table[i], table[i - c])
            table[i] += 1
        print(amount, table[amount], inf)
        if table[amount] > inf:
            return -1
        return table[amount]
