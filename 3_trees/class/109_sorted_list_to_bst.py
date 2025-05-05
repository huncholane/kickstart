from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_middle(head):
    if not (head or head.next):
        return head
    slow, fast, prev_slow = head, head, None
    while fast and fast.next:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next
    if prev_slow:
        prev_slow.next = None
    return slow


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def dfs(head):
            if not head:
                return
            if not head.next:
                return TreeNode(head.val)
            mid = get_middle(head)
            root = TreeNode(mid.val)
            r = mid.next
            mid.next = None
            root.left = dfs(head)
            root.right = dfs(r)
            return root

        return dfs(head)
