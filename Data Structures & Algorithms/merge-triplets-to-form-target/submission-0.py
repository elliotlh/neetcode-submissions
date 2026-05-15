class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        [1,5,3] <-- Candidate for target[b]
        [7,1,1] <-- Candidate for target[a]
        [3,2,4] <-- Candidate for target[c]
        [7,10,10] <-- Candidate for target[0]


        Target == [7,5,4]

        [7,5,3]
        [7,5,4]

        What are we trying to do:
        1. When we analyze a triplet, we need to determine its validity for future max merges
        2. It can only be valid if other numbers in triplet are <= target value
            2a. if < target, only position is valid
            2b. if == target, alt position could also be valid
        3. Return true if candidates for all positions are found
        """
        spot_a = False
        spot_b = False
        spot_c = False
        for a,b,c in triplets:
            # 1. Do spot_a check
            if a == target[0] and b <= target[1] and c <= target[2]:
                spot_a = True
            if b == target[1] and a <= target[0] and c <= target[2]:
                spot_b = True
            if c == target[2] and a <= target[0] and b <= target[1]:
                spot_c = True
        return spot_a and spot_b and spot_c
        