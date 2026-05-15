# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def getValAndCarry(self, total: int, carry: bool) -> Tuple[int, bool]:
        if carry:
            total += 1
        if total >= 10:
            return total - 10, True
        else:
            return total, False

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 65 + 65
        # 130
        """
      1 1
        6 5
        6 5
    ------------
        3 0
        """
        dummy = ListNode()
        curr = dummy
        carry = False
        while l1 and l2:
            candidate_sum = l1.val + l2.val
            val, carry = self.getValAndCarry(candidate_sum, carry)
            curr.next = ListNode(val)
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        while l1:
            candidate_sum = l1.val
            val, carry = self.getValAndCarry(candidate_sum, carry)
            curr.next = ListNode(val)
            l1 = l1.next
            curr = curr.next
        while l2:
            candidate_sum = l2.val
            val, carry = self.getValAndCarry(candidate_sum, carry)
            curr.next = ListNode(val)
            l2 = l2.next
            curr = curr.next
        if carry:
            curr.next = ListNode(1)
        return dummy.next

    
        








        