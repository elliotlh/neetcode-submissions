class Solution:
    def buildSequence(self, start, counts, size: int) -> bool:
        print('before', counts)
        for key in range(start, start + size):
            if counts.get(key, 0) == 0:
                print('after', counts)
                return False
            counts[key] -= 1
        print('after', counts)
        return True


    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        1,2,3,4,5,6,7,8
        0,1,2,3,4,5

        - Sort the list
        - Store all the frequencies in a hash map
        - For k / groupSize:
            take first unclaimed element (must be start of sequence)
            see if I can build a sequence from it
            return false otherwise
        """
        k = len(hand)
        if k % groupSize != 0:
            return False
        hand.sort()
        counts = collections.Counter(hand)
        for num in hand:
            if counts[num] > 0 and not self.buildSequence(num, counts, groupSize):
                return False
        return True
