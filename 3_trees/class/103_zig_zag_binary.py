# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q, res = [root], []
        rtol = False
        while q:
            numnodes = len(q)
            slate = []
            for _ in range(numnodes):
                node = q.pop(0)
                slate.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if rtol:
                slate.reverse()
            rtol = not rtol
            res.append(slate)
        return res
