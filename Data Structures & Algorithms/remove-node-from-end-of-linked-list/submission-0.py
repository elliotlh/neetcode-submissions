# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1. To find the nth node, we can use 3 pointers. We iterate the first pointer by n
                then we iterate all pointers by 1 until the head is at the end. Our remaining
                2 pointers should be the previous value and the actual value
        """
        if not head:
            return None
        dummy = ListNode(-1, head)
        # Iterate curr n positions
        curr = head
        for i in range(n):
            if not curr:
                return head
            curr = curr.next
            
        # Now we iterate to the end of the list
        prev_tail = dummy
        tail = head
        while curr:
            curr = curr.next
            prev_tail = tail
            tail = tail.next
        
        prev_tail.next = tail.next
        return dummy.next
        