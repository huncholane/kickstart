from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return

        def dfs(node):
            smallest, largest = node.val, node.val
            if node.left:
                s, l, b = dfs(node.left)
                if not b or l >= node.val:
                    return 0, 0, False
                smallest = min(smallest, s)
                largest = max(largest, l)
            if node.right:
                s, l, b = dfs(node.right)
                if not b or s <= node.val:
                    return 0, 0, False
                smallest = min(smallest, s)
                largest = max(largest, l)
            return smallest, largest, True

        return dfs(root)[2]
