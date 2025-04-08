from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack, res = [(root, None)], []
        while stack:
            node, zone = stack[-1]
            if not zone:
                stack[-1] = (node, "arrival")
                if node.left:
                    stack.append((node.left, None))
            elif zone == "arrival":
                stack[-1] = (node, "interim")
                if node.right:
                    stack.append((node.right, None))
            else:
                res.append(node.val)
                stack.pop()
        return res
