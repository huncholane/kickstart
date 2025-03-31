class Node:
    def __init__(self, val):
        self.val = val
        self.next: Node = None
        self.prev: Node = None

    def __str__(self):
        return str(self.val)


root = Node(4)
root.next = Node(5)
root.prev = Node(2)
root.prev.prev = Node(1)
root.prev.next = Node(3)
root.next.next = Node(7)

slate, res = [], []


def helper(node):
    if node is None:
        for i in range(len(slate) - 1, -1, -1):
            res.append(slate[i])
        return
    slate.append(node.val)
    helper(node.prev)
    slate.clear()
    helper(node.next)
    slate.clear()


helper(root)
print(res)
