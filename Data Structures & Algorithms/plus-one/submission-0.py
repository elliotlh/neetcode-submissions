class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        We need to
        1. Iterate over digits backwards.
        2. If there is a carryover, we apply that. If this in itself produces a carryover, we will continue applying it
        3. Special case: if there is still carryover after the full loop, we need to insert a 1 at the beginning of the list
        """
        i = len(digits) - 1
        carry = 1
        while i > - 1:
            total = digits[i] + carry
            if total == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = total
                carry = 0
            i -= 1
        if carry > 0:
            digits.insert(0, 1)
        return digits
        