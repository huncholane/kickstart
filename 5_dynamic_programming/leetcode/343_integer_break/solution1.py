class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        table = [0] * (n + 1)
        table[1] = 1
        table[2] = 2
        for i in range(3, n + 1):
            if i == n:
                best = n - 1
            else:
                best = i
            for j in range(1, i // 2 + 1):
                if table[j] * table[i - j] > best:
                    best = table[j] * table[i - j]
            table[i] = best
        return table[n]
