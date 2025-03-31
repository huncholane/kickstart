class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

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
                return helper(node.left)
            else:
                return helper(node.right)

        return helper(self.mid)

    def insert(self, key, val):
        """Works but doesn't gaurentee even tree length"""
        new_node = Node(key, val)
        if self.mid is None:
            self.mid = new_node
            return

        def helper(node: Node):
            if node is None:
                return new_node
            if key == node.key:
                node.val = val
            elif key < node.key:
                node.left = helper(node.left)
            else:
                node.right = helper(node.right)
            return node

        self.mid = helper(self.mid)

    def value_list(self):
        """Returns array of values in correct order using reversed dfs"""
        slate, res = [], []

        def helper(node: Node):
            if node is None:
                for i in range(len(slate) - 1, -1, -1):
                    res.append(slate[i])
                return
            slate.append(node.val)
            helper(node.left)
            slate.clear()
            helper(node.right)
            slate.clear()

        helper(self.mid)
        return res

    def __str__(self):
        """Creates json using reversed dfs"""
        if self is None:
            return "{}"
        slate, res = [], ["{"]

        def helper(node: Node, last: Node):
            if node is None:
                for i in range(len(slate) - 1, -1, -1):
                    res.append(slate[i])
                return
            slate.append(node.key_val_str())
            helper(node.left, node)
            slate.clear()
            helper(node.right, node)
            slate.clear()

        helper(self.mid, None)
        res.append("}")
        return "\n".join(res)


b = BST()
b.insert("d", "1st d value")
b.insert("a", "1st a value")
b.insert("g", "1st g value")
b.insert("i", "1st i value")
b.insert("d", "2nd d value")
b.insert("e", "1st e value")
b.insert("b", "1st b value")
print(b.search("i"))
# b.insert("z", "1st z value")
# b.insert("gbui", "new val")
print(b)
