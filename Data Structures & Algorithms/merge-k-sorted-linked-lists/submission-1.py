# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from typing import Tuple, Self, Optional
import heapq
import itertools

class ComparableListNode:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other: Self) -> bool:
        return self.node.val < other.list_node().val

    def list_node(self) -> ListNode:
        return self.node

    def val(self) -> int:
        return self.node.val

    def next_node(self) -> Optional[ListNode]:
        return self.node.next

class ListFrontier:
    def __init__(self):
        self.counter = itertools.count()
        self.min_heap: List[ComparableListNode] = []

    def add(self, node: ListNode) -> None:
        heapq.heappush(self.min_heap, ComparableListNode(node))

    def empty(self) -> bool:
        return len(self.min_heap) == 0

    def pop_next_minimums(self) -> List[ListNode]:
        if len(self.min_heap) == 0:
            return []
        min_node = heapq.heappop(self.min_heap)
        minimums: List[ListNode] = [min_node.list_node()]
        if min_node.next_node():
            heapq.heappush(self.min_heap, ComparableListNode(min_node.next_node()))
        while len(self.min_heap) > 0 and self.min_heap[0].val() == minimums[0].val:
            min_node = heapq.heappop(self.min_heap)
            minimums.append(min_node.list_node())
            if min_node.next_node():
                heapq.heappush(self.min_heap, ComparableListNode(min_node.next_node()))
        return minimums

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        frontier = ListFrontier()
        for head in lists:
            if head:
                frontier.add(head)
        dummy = ListNode()
        curr = dummy
        while not frontier.empty():
            minimums = frontier.pop_next_minimums()
            for node in minimums:
                curr.next = node
                curr = curr.next
        return dummy.next
        