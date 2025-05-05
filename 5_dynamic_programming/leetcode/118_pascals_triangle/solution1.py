class Solution:
    def generate(self, n: int) -> list[list[int]]:
        if n == 1:
            return [[1]]
        if n == 2:
            return [[1], [1, 1]]
        table = [[1 for _ in range(n)] for _ in range(n)]
        res = [[1], [1, 1]]
        for i in range(2, n):
            for j in range(1, i):
                upleft = table[i - 1][j - 1]
                up = table[i - 1][j]
                table[i][j] = upleft + up
            res.append(table[i][: i + 1])
        return res
