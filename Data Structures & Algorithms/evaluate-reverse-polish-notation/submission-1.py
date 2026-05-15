class Solution:
    def isNumeric(self, token: str) -> bool:
        try:
            int(token)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.isNumeric(token):
                stack.append(int(token))
            else:
                b, a = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    res = a / b
                    if res < 0:
                        stack.append(math.ceil(res))
                    else:
                        stack.append(math.floor(res))
        return stack[0]