class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        mod = 10**9 + 7
        ft = [0] * (n + 1)
        ft[1], ft[2] = 1, 2
        lt = [0] * (n + 1)
        lt[1], lt[2] = 1, 2
        ut = [0] * (n + 1)
        ut[1], ut[2] = 1, 2
        for i in range(3, n + 1):
            ft[i] = (ft[i - 1] + ft[i - 2] + lt[i - 2] + ut[i - 2]) % mod
            lt[i] = (ft[i - 1] + ut[i - 1]) % mod
            ut[i] = (ft[i - 1] + lt[i - 1]) % mod
        return ft[n]
