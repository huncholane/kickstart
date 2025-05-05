import queue
from typing import List


class TreeNode:
    def __init__(self, key: int, val=None):
        self.key = key
        self.val = val
        self.children: List[TreeNode] = []  # instead of left and right


def levelorder(root: TreeNode):
    if root is None:
        return
    q = queue.Queue()
    last_level = 0
    q.put((last_level, root))
    while not q.empty():
        level, node = q.get()
        if level != last_level:
            last_level = level
        print("  " * level, node.key)
        level += 1
        for child in node.children:
            q.put((level, child))


def dfs(root: TreeNode, level=0):
    """Use preorder dfs"""
    if root is None:
        return
    print("  " * level, root.key)
    for child in root.children:
        dfs(child, level + 1)


root = TreeNode("Table of Contents")
ch1 = TreeNode("Chapter 1")
sec1_1 = TreeNode("Sec 1.1")
sec1_2 = TreeNode("Sec 1.2")
sec1_3 = TreeNode("Sec 1.3")
ch1.children = [sec1_1, sec1_2, sec1_3]
ch2 = TreeNode("Chapter 2")
sec2_1 = TreeNode("Sec 2.1")
sec2_2 = TreeNode("Sec 2.2")
sec2_1_1 = TreeNode("Sec 2.1.1")
sec2_1_2 = TreeNode("Sec 2.1.2")
sec2_1.children = [sec2_1_1, sec2_1_2]
ch2.children = [sec2_1, sec2_2]
root.children = [ch1, ch2]
dfs(root)
