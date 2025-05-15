class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 + 7
        table = [[0] * 10 for _ in range(n + 1)]
        for i in range(10):
            table[1][i] = 1
        for i in range(2, n + 1):
            table[i][0] = (table[i - 1][4] + table[i - 1][6]) % mod
            table[i][1] = (table[i - 1][6] + table[i - 1][8]) % mod
            table[i][2] = (table[i - 1][7] + table[i - 1][9]) % mod
            table[i][3] = (table[i - 1][4] + table[i - 1][8]) % mod
            table[i][4] = (table[i - 1][0] + table[i - 1][3] + table[i - 1][9]) % mod
            table[i][5] = 0
            table[i][6] = (table[i - 1][0] + table[i - 1][1] + table[i - 1][7]) % mod
            table[i][7] = (table[i - 1][2] + table[i - 1][6]) % mod
            table[i][8] = (table[i - 1][1] + table[i - 1][3]) % mod
            table[i][9] = (table[i - 1][2] + table[i - 1][4]) % mod
        return sum(table[-1]) % mod
