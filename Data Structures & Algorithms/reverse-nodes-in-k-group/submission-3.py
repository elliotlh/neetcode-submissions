# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Tuple

class Solution:
    def reverseKNodes(self, head: Optional[ListNode], k: int) -> Tuple[Optional[ListNode], Optional[ListNode]]:
        if not head:
            return None, None
        stack = []
        curr = head
        i = 0
        while curr and i < k:
            stack.append(curr)
            i += 1
            curr = curr.next
        # if there weren't k, leave unreversed
        if i != k:
            return head, None
        new_head, new_tail = stack[-1], stack[0]
        # The new tail needs to point to the next pointer
        new_tail.next = new_head.next
        curr = stack.pop()
        while stack:
            curr.next = stack[-1]
            curr = stack.pop()
        return new_head, new_tail

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head, new_tail = self.reverseKNodes(head, k)
        while new_tail:
            next_batch = new_tail.next
            adjusted_head, adjusted_tail = self.reverseKNodes(next_batch, k)
            new_tail.next = adjusted_head
            new_tail = adjusted_tail

        return new_head
        