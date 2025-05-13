"""
Getting full trees instead of catalan
"""

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
        return [TreeNode(0)]
    result: list[TreeNode | None] = []
    for r in range(start + 1, end):
        left_subtrees = helper(start, r - 1)
        right_subtrees = helper(r + 1, end)
        for lst in left_subtrees:
            for rst in right_subtrees:
                root = TreeNode(0)
                root.left = lst
                root.right = rst
                result.append(root)
    memo[(start, end)] = result
    return result


class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        return helper(1, n)
