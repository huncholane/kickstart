def ispalindrome(s: str) -> bool:
    n = len(s)
    i, j = 0, n - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            if s[i] != s[j]:
                return ispalindrome(s[i + 1 : j + 1]) or ispalindrome(s[i:j])
            else:
                i += 1
                j -= 1
        return True
