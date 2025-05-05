# Definition for a Node.
from typing import List, Optional


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []
        q, res = [root], []
        while q:
            numnodes = len(q)
            res.append([])
            for _ in range(numnodes):
                node = q.pop(0)
                res[-1].append(node.val)
                for child in node.children:
                    q.append(child)
        return res
