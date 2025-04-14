# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q, res = [root], []
        while q:
            numnodes = len(q)
            res.append([])
            for _ in range(numnodes):
                node = q.pop(0)
                res[-1].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        res.reverse()
        return res
