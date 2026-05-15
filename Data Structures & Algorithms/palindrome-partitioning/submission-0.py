class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        results: List[List[str]] = []
        def split(i: int, curr_word: str, curr_partitions: List[str]) -> None:
            # If I'm at the end, lets goooo
            if i == len(s):
                if curr_word != '':
                    return
                cloned = curr_partitions.copy()
                results.append(cloned)
                return
            # this letter could be part of a bigger palindrome
            new_word = curr_word + s[i]
            split(i + 1, new_word, curr_partitions)
            # Or this word could be its own palindrome
            if self.isPalindrome(new_word):
                curr_partitions.append(new_word)
                split(i + 1, '', curr_partitions)
                curr_partitions.pop()
        split(0, '', [])
        return results
        