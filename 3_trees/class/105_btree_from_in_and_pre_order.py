from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        inorder_map = {inorder[i]: i for i in range(len(inorder))}

        def helper(pl, pr, il, ir):
            if pl > pr:
                return
            if pl == pr:
                return TreeNode(preorder[pl])
            i = inorder_map[preorder[pl]]
            node = TreeNode(preorder[pl])
            leftsize = i - il
            node.left = helper(pl + 1, pl + leftsize, il, il + leftsize)
            node.right = helper(pl + leftsize + 1, pr, i + 1, ir)
            return node

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
