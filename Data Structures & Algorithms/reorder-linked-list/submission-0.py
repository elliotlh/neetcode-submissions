# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head
        # get everything onto a stack
        while curr:
            stack.append(curr)
            curr = curr.next
        print(len(stack))
        half, remainder = divmod(len(stack), 2)
        print(half, remainder)
        curr = head
        for i in range(half):
            # phase 1: capture the next node
            next_node = curr.next
            # phase 2: get the tail node (e.g. 6)
            tail_node = stack.pop()
            if i == half - 1 and remainder == 0:
                tail_node.next = None
            else:
                tail_node.next = next_node
            # (e.g. 0 --> 6)
            curr.next = tail_node
            # curr = 1
            curr = next_node
        if remainder == 1:
            last = stack.pop()
            last.next = None

