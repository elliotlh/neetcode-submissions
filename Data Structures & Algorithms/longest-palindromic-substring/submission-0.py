class Solution:
    def expandOut(self, s: str, left: int, right: int) -> Tuple[int, int]:
        while left > -1 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right

    def longestPalindrome(self, s: str) -> str:
        biggest = ''
        for i in range(len(s)):
            l, r = self.expandOut(s, i, i + 1)
            biggest = max(biggest, s[l:r], key=len)
            l, r = self.expandOut(s, i, i)
            biggest = max(biggest, s[l:r], key=len)
        return biggest
        