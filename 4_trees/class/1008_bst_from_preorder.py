from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return []

        def helper(l, r):
            if l > r:
                return
            root = TreeNode(preorder[l])
            mid = l + 1
            while mid <= r and preorder[mid] < preorder[l]:
                mid += 1
            root.left = helper(l + 1, mid - 1)
            root.right = helper(mid, r)
            return root

        return helper(0, len(preorder) - 1)
