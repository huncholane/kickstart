class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def key_val_str(self):
        return f'  "{self.key}": "{self.val}"'

    def __str__(self):
        return f"Key: {self.key}, Val: {self.val}"


class BST:
    def __init__(self):
        self.mid = None

    def search(self, key):
        def helper(node: Node):
            if node is None:
                return
            if node.key == key:
                return node
            elif key < node.key:
                return helper(node.prev)
            else:
                return helper(node.next)

        return helper(self.mid)

    def insert(self, key, val):
        node = Node(key, val)
        if self.mid is None:
            self.mid = node
            return
        # TODO insert something after node

    def value_list(self):
        """Returns array of values in correct order using reversed dfs"""
        slate, res = [], []

        def helper(node: Node):
            if node is None:
                for i in range(len(slate) - 1, -1, -1):
                    res.append(slate[i])
                return
            slate.append(node.val)
            helper(node.prev)
            slate.clear()
            helper(node.next)
            slate.clear()

        helper(self.mid)
        return res

    def __str__(self):
        """Creates json using reversed dfs"""
        if self is None:
            return "{}"
        slate, res = [], ["{"]

        def helper(node: Node):
            if node is None:
                for i in range(len(slate) - 1, -1, -1):
                    res.append(slate[i])
                return
            slate.append(f'  "{node.key}": "{node.val}"')
            helper(node.prev)
            slate.clear()
            helper(node.next)
            slate.clear()

        helper(self.mid)
        res.append("}")
        return "\n".join(res)


b = BST()
b.insert("d", "asdv")
print(b)
