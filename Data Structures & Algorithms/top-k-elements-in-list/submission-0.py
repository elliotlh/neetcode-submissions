class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. Easy solution: use Python's counter class and return most_frequent
        2. To keep k frequent elements, this makes me think of a heap
        3. We could do a 2 pass approach where we get the counter, and
                then iterate over the count dictionary and keep a heap
                where the frequency is the sorting property. We will keep a min
                heap. The top element of the heap will be on the chopping block. 
                We will then heappushpop. Our heap will be our return
        """
        counts = collections.Counter(nums)
        return [x[0] for x in counts.most_common(k)]
        