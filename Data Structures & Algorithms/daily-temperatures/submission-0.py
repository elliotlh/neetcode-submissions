class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        At any given point, I need to know what my next
        warmest day is. In other words, I need to remember
        when I've got to a temperature I haven't processed yet
        and update it

        The canonical solution to this problem is the monotic stack
        """

        decreasing_stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while decreasing_stack and temp > decreasing_stack[-1][0]:
                _, idx = decreasing_stack.pop()
                result[idx] = i - idx
            # if I have no stack items or this satisfies the monotonic decreasing property
            if not decreasing_stack or temp <= decreasing_stack[-1][0]:
                decreasing_stack.append((temp, i))
        return result

            
            
        