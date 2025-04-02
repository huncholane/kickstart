import queue


class TreeNode:
    def __init__(self, key, val=None):
        self.key: int = key
        self.val = val  # ignore for now
        self.left: TreeNode = None
        self.right: TreeNode = None

    def __str__(self):
        return f"Key: {self.key}, Val: {self.val}"


def search(root: TreeNode, key: int):
    if root is None:
        return None
    curr = root
    while curr is not None:
        if key == curr.key:
            return curr
        elif key < curr.key:
            curr = curr.left
        else:
            curr = curr.right
    return None


def skewed_insert(root: TreeNode, key: int, val=None):
    newnode = TreeNode(key, val)
    if root is None:
        print(f"\nINSERT Set the root to {key}")
        return newnode
    curr, prev = root, None
    while curr is not None:
        prev = curr
        if key == curr.key:
            raise Exception("Key already exists")
        elif key < curr.key:
            curr = curr.left
        else:
            curr = curr.right
    if key < prev.key:
        print(f"INSERT {key} to the left of {prev.key}")
        prev.left = newnode
    else:
        print(f"INSERT {key} to the right of {prev.key}")
        prev.right = newnode
    return root


def tree_min(root: TreeNode):
    if root is None:
        return None
    curr = root
    while curr.left is not None:
        curr = curr.left
    return curr


def tree_max(root: TreeNode):
    if root is None:
        return None
    curr = root
    while curr.right is not None:
        curr = curr.right
    return curr


def successor(root: TreeNode, p: TreeNode):
    """Find successor for p node"""
    if root is None:
        return None
    if p.right is not None:
        curr = p.right
        while curr.left is not None:
            curr = curr.left
        return curr
    # Search for p from root, last left will be the answer
    ancestor = None
    curr = root
    while curr.key != p.key:
        if p.key < curr:
            ancestor = curr
            curr = curr.left
        else:
            curr = curr.right
    return ancestor


def predeccessor(root: TreeNode, p: TreeNode):
    if root is None:
        return None
    if p.left is not None:
        curr = p.left
        while curr.right is not None:
            curr = curr.right
        return curr
    ancestor = None
    curr = root
    while curr.key != p.key:
        if p.key > curr:
            ancestor = curr
            curr = curr.right
        else:
            curr = curr.left
    return ancestor


def delete(root: TreeNode, key: int):
    curr = root
    prev = None
    while curr is not None:
        if key == curr.key:
            break
        elif key < curr.key:
            prev = curr
            curr = curr.left
        else:
            prev = curr
            curr = curr.right
    # Edge case 1: Not found
    if curr is None:
        print(f"DELETE {key} not found")
        return root

    # Case 1: Node is a leaf
    if curr.left is None and curr.right is None:
        if prev is None:
            print(f"DELETE leaf case, {curr.key} is the last node")
            return None
        if curr.key == prev.left.key:
            print(f"DELETE leaf case, {key} to the left of {prev.key}")
            prev.left = None
        else:
            print(f"DELETE leaf case, {key} to the right of {prev.key}")
            prev.right = None
        return root

    # Case 2: Node has one child
    child = None
    if curr.right is not None and curr.left is None:
        child = curr.right
    if curr.left is not None and curr.right is None:
        child = curr.left
    if child is not None:
        if prev is None:
            root = child
            print(f"DELETE one child case, moving {child.key} into root")
            return root
        if prev.left.key == curr.key:
            print(
                f"DELETE one child case, move children of {key} to the left of {prev.key}"
            )
            prev.left = child
        else:
            print(
                f"DELETE one child case, move children of {key} to the right of {prev.key}"
            )
            prev.right = child
        return root

    # Case 3: Node has two children
    if curr.left is not None and curr.right is not None:
        succ = curr.right
        succ_prev = curr
        while succ.left is not None:
            succ_prev = succ
            succ = succ.left
        curr.key = succ.key
        curr.val = succ.val
        if succ.key == succ_prev.left.key:
            succ_prev.left = succ.right
        else:
            succ_prev.right = succ.right
        return root


def levelorder(root: TreeNode):
    """Prints bfs one level at a time"""
    if root is None:
        return
    q = queue.Queue()
    q.put((0, root))
    last_level = 0
    while not q.empty():
        level, node = q.get()
        if level != last_level:
            print()
            last_level = level
        print(node.key, end=" ")
        level += 1
        for child in [node.left, node.right]:
            if child is not None:
                q.put((level, child))
    print()


def dfs(root: TreeNode, order="inorder", printplease=False):
    res = []

    def helper(root):
        if root is None:
            return

        # pre order print
        if order == "preorder":
            res.append(root)
            if printplease:
                print(root.key, end="")
        helper(root.left)
        # in order print
        if order == "inorder":
            res.append(root)
            if printplease:
                print(root.key, end=" ")
        helper(root.right)
        # post order print
        if order == "postorder":
            res.append(root)
            if printplease:
                print(root.key, end=" ")

    helper(root)
    if printplease:
        print()
    return res


def max_height(node: TreeNode, h=0):
    if node is None:
        return h - 1
    return max(max_height(node.left, h + 1), max_height(node.right, h + 1))


def print_tree(root: TreeNode):
    h = max_height(root)
    print(h, "longest path")
    print(root)


root = skewed_insert(None, 44)
assert root.key == 44
assert root.right is None
assert root.left is None
root = delete(root, 44)
assert root is None
root = skewed_insert(root, 44)
root = skewed_insert(root, 16)
assert root.left.key == 16
root = delete(root, 16)
assert root.key == 44
assert root.left is None
root = skewed_insert(root, 16)
root = skewed_insert(root, 8)
assert root.left.left.key == 8
root = delete(root, 16)
assert root.left.key == 8
assert root.key == 44
root = skewed_insert(root, 4)
root = skewed_insert(root, 16)
assert root.left.left.key == 4
assert root.left.right.key == 16
root = delete(root, 8)
assert root.left.key == 16
assert root.left.right is None
root = skewed_insert(root, 18)
assert root.left.right.key == 18
root = skewed_insert(root, 17)
root = skewed_insert(root, 19)
assert root.left.right.left.key == 17
assert root.left.right.right.key == 19
root = delete(root, 16)
assert root.left.key == 17
assert root.left.right.key == 18
assert root.left.right.left is None
assert root.left.right.right.key == 19
assert root.left.left.key == 4
root = delete(root, 44)
assert root.key == 17
root = delete(root, 100)
assert root.key == 17
root = skewed_insert(root, 88)

root = skewed_insert(None, 44)
root = skewed_insert(root, 17)
root = skewed_insert(root, 8)
root = skewed_insert(root, 32)
root = skewed_insert(root, 28)
root = skewed_insert(root, 29)
root = skewed_insert(root, 88)
root = skewed_insert(root, 65)
root = skewed_insert(root, 97)
root = skewed_insert(root, 56)
root = skewed_insert(root, 82)
root = skewed_insert(root, 93)
root = skewed_insert(root, 76)
root = skewed_insert(root, 68)
root = skewed_insert(root, 80)
root = delete(root, 97)

print("Tree stayed in tact!")
levelorder(root)
dfs(root, printplease=True)
