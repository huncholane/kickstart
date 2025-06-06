"""Generate All Possible Expressions That Evaluate To The Given Target Value
Given a string s that consists of digits ("0".."9") and target, a non-negative integer, find all expressions that can be built from string s that evaluate to the target.

When building expressions, you have to insert one of the following operators between each pair of consecutive characters in s: join or * or +. For example, by inserting different operators between the two characters of string "12" we can get either 12 (1 joined with 2 or "12") or 2 ("1*2") or 3 ("1+2").

Other operators such as - or ÷ are NOT supported.

Expressions that evaluate to the target but only utilize a part of s do not count: entire s has to be consumed.

Precedence of the operators is conventional: join has the highest precedence, * – medium and + has the lowest precedence. For example, 1 + 2 * 34 = (1 + (2 * (34))) = 1 + 68 = 69.

You have to return ALL expressions that can be built from string s and evaluate to the target.

Example
{
"s": "202",
"target": 4
}
Output:

["2+0+2", "2+02", "2*02"]
Same three strings in any other order are also a correct output.

Notes
Order of strings in the output does not matter.
If there are no expressions that evaluate to target, return an empty list.
Returned strings must not contain spaces or any characters other than "0",..., "9", "*", "+".
All returned strings must start and end with a digit.
Constraints:

1 <= length of s <= 13
1 <= target <= 1013"""


def get_all_number_strings(i, s, slate, res):
    """Get all consecutive number strings. After understanding this we will add the operators and target."""
    if i == len(s):
        if len(slate) > 0:
            res.append("".join([val[1] for val in slate]))
        return
    # Start a new string
    get_all_number_strings(i + 1, s, slate, res)
    if len(slate) > 0 and slate[-1][0] != i - 1:
        return
    slate.append((i, s[i]))
    get_all_number_strings(i + 1, s, slate, res)
    slate.pop()


def generate_all_expressions(s, target):
    if not s:
        return []
    res = []

    def helper(so_far, evaluated, idx, prev):
        if idx == len(s):
            if evaluated == target:
                res.append(so_far)
        for i in range(idx, len(s)):
            curr = s[idx : i + 1]
            curr_int = int(curr)
            if idx == 0:
                helper(so_far + curr, curr_int, i + 1, curr_int)
            else:
                helper(so_far + "+" + curr, evaluated + curr_int, i + 1, curr_int)
                helper(
                    so_far + "*" + curr,
                    (evaluated - prev) + (prev * curr_int),
                    i + 1,
                    prev * curr_int,
                )

    helper("", 0, 0, 0)
    return res


res = generate_all_expressions(**{"s": "202", "target": 4})
print(res)
