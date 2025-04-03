# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        slate, res = [], []

        def dfs(node, target):
            if not (node.left or node.right):
                if node.val == target:
                    slate.append(node.val)
                    res.append(slate[:])
                    slate.pop()
                return
            if node.left:
                slate.append(node.val)
                dfs(node.left, target - node.val)
                slate.pop()
            if node.right:
                slate.append(node.val)
                dfs(node.right, target - node.val)
                slate.pop()

        dfs(root, targetSum)
        return res
