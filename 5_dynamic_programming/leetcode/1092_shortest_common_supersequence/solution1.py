"""
Add remaining characters from lcs to longest string (don't need to add characters from lcs)
Traceback after lcs


Example 1:
abac
cab
    c a b
  0 0 0 0
a 0 0 1 1
b 0 0 1 2
a 0 0 1 2
c 0 1 1 2

Path:
│     c a b
│   * c 0 0
│ a 0 0 a 1
│ b 0 0 1 b
│ a 0 0 1 a
│ c 0 1 1 c

Alignment:
_ a b a c
c a b _ _

Result: cabac


Example 2:
bbbaaaba
bbababbb
    b b a b a b b b
  0 0 0 0 0 0 0 0 0
b 0 1 1 1 1 1 1 1 1
b 0 1 2 2 2 2 2 2 2
b 0 1 2 2 3 3 3 3 3
a 0 1 2 3 3 4 4 4 4
a 0 1 2 3 3 4 4 4 4
a 0 1 2 3 3 4 4 4 4
b 0 1 2 3 4 4 5 5 5
a 0 1 2 3 3 5 5 5 5

Path:
│     b b a b a b b b
│   * 0 0 0 0 0 0 0 0
│ b 0 b 1 1 1 1 1 1 1
│ b 0 1 b a 2 2 2 2 2
│ b 0 1 2 2 b 3 3 3 3
│ a 0 1 2 3 3 a 4 4 4
│ a 0 1 2 3 3 a 4 4 4
│ a 0 1 2 3 3 a 4 4 4
│ b 0 1 2 3 4 4 b b b
│ a 0 1 2 3 4 5 5 5 a

Alignment:
b b _ b a a a b _ _ a
b b a b _ _ _ b b b _

Result: bbabaaabbba
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                s = 1 if str1[row - 1] == str2[col - 1] else 0
                table[row][col] = max(
                    table[row - 1][col],
                    table[row][col - 1],
                    table[row - 1][col - 1] + s,
                )
        strtable: list[list[str]] = []
        for i, row in enumerate(table):
            strrowlist = [str(num) for num in row]
            rowstr = " ".join(strrowlist)
            if i == 0:
                print(" ", rowstr)
            else:
                print(str1[i - 1], rowstr)
            strtable.append(strrowlist)

        # traceback
        result: list[str] = []
        row, col = m, n
        while row > 0 and col > 0:
            if table[row][col] == table[row - 1][col]:
                result.append(str1[row - 1])
                row -= 1
            elif table[row][col] == table[row][col - 1]:
                result.append(str2[col - 1])
                col -= 1
            else:
                result.append(str1[row - 1])
                row -= 1
                col -= 1
        while row > 0:
            result.append(str1[row - 1])
            row -= 1
        while col > 0:
            result.append(str2[col - 1])
            col -= 1

        result.reverse()
        return "".join(result)
