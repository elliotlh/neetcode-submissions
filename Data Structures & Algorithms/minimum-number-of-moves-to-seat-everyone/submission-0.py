class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        """
        1,4,5,9
        1,2,3,6

        1,4,5,9
        1,5,6,10
        """
        seats.sort()
        students.sort()
        cumulative_delta = 0
        for a, b in zip(seats, students):
            cumulative_delta += abs(a - b)
        return cumulative_delta