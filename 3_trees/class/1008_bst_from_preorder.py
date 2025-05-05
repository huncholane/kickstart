from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = 0

        def dfs(l, h):
            nonlocal i
            if i == len(preorder):
                return
            val = preorder[i]
            if not l <= val <= h:
                return
            root = TreeNode(val)
            i += 1
            root.left = dfs(l, val - 1)
            root.right = dfs(val + 1, h)
            return root

        return dfs(float("-inf"), float("inf"))
