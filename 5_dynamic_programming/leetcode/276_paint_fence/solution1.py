class Solution:
    def numWays(self, n: int, k: int) -> int:
        same = [0] * (n + 1)
        different = [0] * (n + 1)
        total = [0] * (n + 1)

        same[1] = 0
        different[1] = k
        total[1] = k

        for i in range(2, n + 1):
            same[i] = different[i - 1]
            different[i] = total[i - 1] * (k - 1)
            total[i] = same[i] + different[i]
        return total[n]
