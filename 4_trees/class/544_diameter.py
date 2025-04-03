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
        res = 0

        def dfs(node):
            nonlocal res
            if not (node.left or node.right):
                return 0
            l, r = 0, 0
            diameter = 0
            if node.left:
                l = dfs(node.left)
                diameter += l + 1
            if node.right:
                r = dfs(node.right)
                diameter += r + 1
            res = max(diameter, res)
            return max(l, r) + 1

        dfs(root)
        return res
