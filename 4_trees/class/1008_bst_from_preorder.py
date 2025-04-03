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
            return
        n = len(preorder)

        def dfs(l, r):
            if l > r:
                return  # makes the left or right node none
            val = preorder[l]  # the root of the current tree
            root = TreeNode(val)
            mid = l + 1
            while mid <= r and preorder[mid] < val:
                mid += 1  # Find the first val bigger than root
            root.left = dfs(l + 1, mid - 1)
            root.right = dfs(mid, r)
            return root

        return dfs(0, n - 1)
