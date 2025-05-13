"""
Catalan style trees
End up with recursion to enumerate all possible options

Apply top down memoization to make this a dp problem
"""

# Definition for a binary tree node.
from typing import TYPE_CHECKING


if TYPE_CHECKING:

    class TreeNode:
        def __init__(
            self,
            val: int = 0,
            left: "TreeNode|None" = None,
            right: "TreeNode|None" = None,
        ):
            self.val: int = val
            self.left: TreeNode | None = left
            self.right: TreeNode | None = right


memo: dict[tuple[int, int], list[TreeNode | None]] = {}


def helper(start: int, end: int) -> list[TreeNode | None]:
    if (start, end) in memo:
        return memo[(start, end)]
    if start > end:
        return [None]
    if start == end:
        return [TreeNode(start)]
    result: list[TreeNode | None] = []
    for r in range(start, end + 1):
        left_subtrees = helper(start, r - 1)
        right_subtrees = helper(r + 1, end)
        for lst in left_subtrees:
            for rst in right_subtrees:
                root = TreeNode(r)
                root.left = lst
                root.right = rst
                result.append(root)
    memo[(start, end)] = result
    return result


class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        return helper(1, n)
