class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        """
        [2,1,3][3,2,4][5,3,5] - Capacity 5
        True
        [2,1,10][3,2,4][5,3,5] - Capacity 5
        False

        Idea:
        Keep track of a heap of (drop_off, capacity)
        Beginning of loop, drain the heap if this trip starts after drop off and free up capacity
        If I can accept the trip, push to heap and subtract capacity
        """

        available_capacity = capacity
        can_free = []
        for required_capacity, from_loc, to_loc in trips:
            while can_free and can_free[0][0] <= from_loc:
                _, freed_capacity = heapq.heappop(can_free)
                available_capacity += freed_capacity
            if required_capacity > available_capacity:
                return False
            
            available_capacity -= required_capacity
            heapq.heappush(can_free, (to_loc, required_capacity))
        return True

        