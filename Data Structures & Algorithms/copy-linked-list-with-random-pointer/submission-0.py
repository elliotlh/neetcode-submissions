"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        1. Traverse list normally (ignore random) to get full list generated
            a. Ensure that we have a dictionary mapping original --> cloned equivalent
        2. Traverse list a second time, this time setting the random pointers for the new list
            a. cloned.random = original_to_cloned[original.random]
        """
        if not head:
            return None
        dummy_head = Node(-1)
        current_original_node = head
        current_cloned_node = dummy_head
        original_to_cloned_node_mapping = {}
        # step 1: traverse through list normally creating cloned list
        while current_original_node:
            clone = Node(current_original_node.val)
            current_cloned_node.next = clone
            original_to_cloned_node_mapping[current_original_node] = clone
            current_original_node = current_original_node.next
            current_cloned_node = current_cloned_node.next
        
        # step 2: traverse through list again, this time handling random pointers using our dictionary
        current_original_node = head
        current_cloned_node = dummy_head.next
        while current_original_node:
            if current_original_node.random is not None:
                current_cloned_node.random = original_to_cloned_node_mapping[current_original_node.random]
            current_original_node = current_original_node.next
            current_cloned_node = current_cloned_node.next
        return dummy_head.next
        