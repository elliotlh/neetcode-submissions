class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results: List[str] = []
        def backtrack(remaining_open: int, remaining_closed: int, curr: str) -> None:
            if remaining_open == 0 and remaining_closed == 0:
                results.append(curr)
                return
            # Do we have the option to close up an earlier choice? Lets take it
            if remaining_open < remaining_closed:
                backtrack(remaining_open, remaining_closed - 1, curr + ')')
            if remaining_open > 0:
                backtrack(remaining_open - 1, remaining_closed, curr + '(')
        backtrack(n, n, '')
        return results
