# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False

        def dfs(node, target):
            if not (node.left or node.right):
                if node.val == target:
                    return True
            if node.left and dfs(node.left, target - node.val):
                return True
            if node.right and dfs(node.right, target - node.val):
                return True
            return False

        return dfs(root, targetSum)
