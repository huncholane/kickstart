class Node:
    def __init__(self, val):
        self.val = val
        self.left: Node = None
        self.right: Node = None

    def __str__(self):
        return str(self.val)


root = Node(4)
root.left = Node(2)
root.left.right = Node(3)
root.left.left = Node(1)
root.right = Node(10)
root.right.left = Node(7)
root.right.left.left = Node(6)


def bfs(root):
    q = [root]
    res = []
    maxlen = 0
    while q:
        numnodes = len(q)
        if numnodes > maxlen:
            maxlen = numnodes
        slate = []
        for _ in range(numnodes):
            node = q.pop(0)
            slate.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(slate)
    return res, maxlen


levels, maxlen = bfs(root)
print(" " * maxlen, levels[0][0], " " * maxlen, sep="")
print(" " * (maxlen // 3 + 1), "/", " " * (maxlen // 3), "\\", sep="")
