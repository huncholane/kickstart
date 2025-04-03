from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        n = len(inorder)
        imap = {inorder[i]: i for i in range(n)}

        def helper(pl, pr, il, ir):
            if pl > pr:
                return
            val = postorder[pr]
            node = TreeNode(val)
            i = imap[val]
            leftsize = i - il
            node.left = helper(pl, pl + leftsize - 1, il, i - 1)
            node.right = helper(pl + leftsize, pr - 1, i + 1, ir)
            return node

        return helper(0, n - 1, 0, n - 1)
