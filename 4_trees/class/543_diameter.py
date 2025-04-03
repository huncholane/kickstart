# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0  # global diameter

        def dfs(node):
            nonlocal res
            if not (node.left or node.right):
                return 0  # leaf has 0 edges
            l, r, d = 0, 0, 0  # left height, right height, current diameter
            if node.left:
                l = dfs(node.left)
                d += 1 + l
            if node.right:
                r = dfs(node.right)
                d += 1 + r
            res = max(res, d)
            return max(l, r) + 1

        dfs(root)
        return res
