from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        def dfs(node, parent, right):
            nonlocal root
            oldleft = node.left
            oldright = node.right
            node.left = right
            node.right = parent
            # base case
            if not (oldleft or oldright):
                root = node
            # recursive case
            if oldleft:
                dfs(oldleft, node, oldright)

        dfs(root, None, None)
        return root
