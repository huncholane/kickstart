from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q, m = [(root, 0)], {}
        l, r = 0, 0
        while q:
            count = len(q)
            for _ in range(count):
                node, col = q.pop(0)
                l = min(l, col)
                r = max(r, col)
                if col in m:
                    m[col].append(node.val)
                else:
                    m[col] = [node.val]
                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))
        res = []
        for i in range(l, r + 1):
            if i in m:
                res.append(m[i])
        return res
