import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Build the heap O(nlogn)
        heap = []
        i = 0
        for l in lists:
            while l:
                heapq.heappush(heap, (l.val, i, l))
                l = l.next
                i += 1

        # Build the sorted list
        head = ListNode()
        p = head
        while heap:
            _, _, node = heapq.heappop(heap)
            p.next = node
            p = node
        return head.next
