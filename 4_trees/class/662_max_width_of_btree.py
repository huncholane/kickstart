from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        q, maxwidth = [(0, root)], 0
        while q:
            count = len(q)
            first_i = q[0][0]
            right_i = 0
            for _ in range(count):
                node_i, node = q.pop(0)
                i = node_i - first_i
                right_i = max(right_i, i)
                if node.left:
                    q.append((2 * i + 1, node.left))
                if node.right:
                    q.append((2 * i + 2, node.right))
            maxwidth = max(maxwidth, right_i + 1)
        return maxwidth
