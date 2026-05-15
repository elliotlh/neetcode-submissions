class Solution:
    def explodeOut(self, s: str, i: int, j: int) -> int:
        palindromic_substrings = 0
        while i > -1 and j < len(s):
            if s[i] == s[j]:
                palindromic_substrings += 1
                i -= 1
                j += 1
            else:
                break
        return palindromic_substrings

    def countSubstrings(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            total += self.explodeOut(s, i, i)
            total += self.explodeOut(s, i, i+1)
        return total
        