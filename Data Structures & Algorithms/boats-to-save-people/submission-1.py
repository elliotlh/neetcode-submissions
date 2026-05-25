class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Option 1:
        We could code this up like house robber and try making
        a decision for every set of indexes

        Option 2:
        We could try a greedy where we take our biggest person,
        put them in a boat, and then bin pack them repeatedly
        # limit 5
        4,4,3,3,3,2,2,2,2,1
        """
        people.sort(reverse=True)
        left, right = 0, len(people) - 1
        num_boats = 0
        while left <= right:
            available = limit - people[left]
            left += 1
            if people[right] <= available:
                right -= 1
            num_boats += 1
        return num_boats

            



        