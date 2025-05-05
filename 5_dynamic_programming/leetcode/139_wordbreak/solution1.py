class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        word_set = {w for w in wordDict}
        # call table f to force myself to think of this as a f(n)
        f = [False] * (n + 1)
        f[0] = True
        for i in range(1, n + 1):
            for j in range(1, i):
                # Go backwords to improve speed
                if f[i - j] and s[i - j : i] in word_set:
                    f[i] = True
                    break
            if s[:i] in word_set:
                f[i] = True
        return f[n]
