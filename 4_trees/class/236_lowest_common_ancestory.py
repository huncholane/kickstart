# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return
        lca = None

        def dfs(node):
            nonlocal lca
            pfound, qfound = node == p, node == q
            if node.left:
                pf, qf = dfs(node.left)
                pfound = pf or pfound
                qfound = qf or qfound
            if node.right:
                pf, qf = dfs(node.right)
                pfound = pf or pfound
                qfound = qf or qfound
            if pfound and qfound and not lca:
                lca = node
            return pfound, qfound

        dfs(root)
        return lca
