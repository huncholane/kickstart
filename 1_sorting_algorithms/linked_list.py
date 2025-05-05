class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


def insert(n1, n2):
    tmp = n1.next
    n2.next = n1.next
    n1.next = n2


l1 = Node(0)
node = l1
for i in range(1, 6):
    node.next = Node(i)
    node = node.next

node = l1
while node:
    print(node.value)
    node = node.next
