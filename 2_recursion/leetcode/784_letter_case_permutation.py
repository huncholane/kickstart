"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.



Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]


Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
"""

s = "a1b2"

slate, res = [], []
n = len(s)


def helper(i):
    if i == n:
        res.append("".join(slate))
        return
    if s[i].isalpha():
        slate.append(s[i].upper())
        helper(i + 1)
        slate.pop()
        slate.append(s[i].lower())
        helper(i + 1)
        slate.pop()
    else:
        slate.append(s[i])
        helper(i + 1)
        slate.pop()


helper(0)

for r in res:
    print(r)
