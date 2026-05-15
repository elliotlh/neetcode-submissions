class Node:
    def __init__(
        self,
        key: int,
        val: int,
        prev: Optional['Node'] = None,
        next: Optional['Node'] = None,
    ):
        self.key: int = key
        self.val: int = val
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache: Dict[int, int] = {}
        self.capacity = capacity
        # Head and tail are going to be sentinels so they are always there
        self.node_location: Dict[int, Node] = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def mark_existing_node_recently_used(self, key: int) -> None:
        cache_node = self.extract_cache_node(key)
        if not cache_node:
            return
        self.put_node_at_head(cache_node)


    def extract_cache_node(self, key: int) -> Optional[Node]:
        cache_node = self.node_location[key]
        prev_node, next_node = cache_node.prev, cache_node.next
        if not prev_node or not next_node:
            return None
        prev_node.next, next_node.prev = next_node, prev_node
        return cache_node

    def put_node_at_head(self, node: Node):
        head_next_val = self.head.next
        if not head_next_val:
            return
        # Place node at front of list
        self.head.next = node
        # Old head and cache point back to each other
        head_next_val.prev = node
        # Update node in place
        node.next = head_next_val
        node.prev = self.head

    def evict_tail(self) -> int:
        previous_node = self.tail.prev
        if not previous_node:
            return -1
        old = previous_node.prev
        if not old:
            return -1
        old.next = self.tail
        self.tail.prev = old
        return previous_node.key

    def get(self, key: int) -> int:
        """
        1. We need to get the cache node
        2. We extract it by taking the prev and next (guaranteed to exist) and connect them together
        3. We need to move it to the head of the list
            a) Get the current head (will be sentinel)
            b) Take the next value of the head (could be sentinel tail, could be other node)
            c) tmp = head.next; head.next = cache_node; tmp.prev = cache_node; cache_node.prev = head, cache_node.next = tmp;
        """
        if key not in self.cache:
            return -1
        self.mark_existing_node_recently_used(key)
        return self.cache[key]


    def insert(self, key: int, value: int) -> None:
        self.cache[key] = value
        cache_node = Node(key, value)
        self.node_location[key] = cache_node
        self.put_node_at_head(cache_node)
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the LRU data structure
            self.cache[key] = value
            self.mark_existing_node_recently_used(key)
            return
        # Case 2: We can just add it
        if len(self.cache) >= self.capacity:
            evicted_key = self.evict_tail()
            del self.node_location[evicted_key]
            del self.cache[evicted_key]
        self.insert(key, value)
            
        
