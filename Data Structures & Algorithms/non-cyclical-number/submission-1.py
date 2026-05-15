
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        seen: Set[int] = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.getReplacement(n)
            if n == 1:
                return True
        return False

    def getReplacement(self, n: int) -> int:
        digits = [int(digit) for digit in list(str(n))]
        return sum([digit ** 2 for digit in digits])