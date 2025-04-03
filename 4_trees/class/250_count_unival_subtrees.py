# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 0

        def dfs(node):
            nonlocal count
            if not (node.left or node.right):
                count += 1
                return True
            unival = True
            if node.left:
                if not dfs(node.left) or node.val != node.left.val:
                    unival = False
            if node.right:
                if not dfs(node.right) or node.val != node.right.val:
                    unival = False
            if unival:
                count += 1
            return unival

        dfs(root)
        return count
