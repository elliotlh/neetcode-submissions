class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        requires = {'}': '{', ']': '[', ')': '('}
        for char in s:
            if char not in requires:
                stack.append(char)
                continue
            if not stack:
                return False
            opening = stack.pop()
            if opening != requires[char]:
                return False
        return len(stack) == 0
            