class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        ())**
        paren_stack: []
        star_stack: []
        # process paren problem normally
        [(] []
        [(,(] []
        [(,(] [*]
        [(,(] [*, *]
        [(] [*, *]

        1. Push open parenthesis to the stack
        2. If I encounter a star, push it to the star stack
        3. If I encounter a close, pop from open paren stack if available
                if not available, pop from star stack
                if not available, return False
        return len(paren_stack) == 0
        """
        paren_stack: List[int] = []
        star_stack: List[int] = []
        for i, char in enumerate(s):
            if char == '(':
                paren_stack.append(i)
            elif char == '*':
                star_stack.append(i)
            else:
                if len(paren_stack) > 0:
                    paren_stack.pop()
                elif len(star_stack) > 0:
                    star_stack.pop()
                else:
                    return False
        
        while paren_stack and star_stack:
            if paren_stack[-1] > star_stack[-1]:
                return False
            paren_stack.pop()
            star_stack.pop()
            
        return len(paren_stack) == 0