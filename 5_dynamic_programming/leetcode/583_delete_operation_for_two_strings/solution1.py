class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        m by n table
        m+n = inserts + deletes + 2*matches + 2*mismatches

        right -> insert from string 2 -> 1
        down -> delete from string 1 -> 1
        diag -> substitute or match -> 0 or INF

        Minimize insertions and deletions, no substitutions
        or make the cost of substitution unreasonably high
        so the algorithm ignores it

        Think of insert as a reverse delete

            s e a
          0 1 2 3
        e 1 2 1 2
        a 2 3 2 1
        t 3 4 3 2

            l e e t
          0 1 2 3 4
        b 1 2 3 4 5
        e 2 3 2 3 4
        a 3 4 3 4 5
        t 4 5 4 5 4
        """
        m, n = len(word1), len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                insert = table[i][j - 1] + 1
                delete = table[i - 1][j] + 1
                table[i][j] = min(insert, delete)
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = min(table[i][j], table[i - 1][j - 1])
        return table[m][n]
