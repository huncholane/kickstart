class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        table = [False] * (n + 1)
        table[0] = True
        for i in range(1, n + 1):
            for j in range(i, -1, -1):
                if table[j] and s[j:i] in wordDict:
                    table[i] = True
                    break
        return table[n]
