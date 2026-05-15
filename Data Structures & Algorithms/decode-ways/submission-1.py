from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        return self.doDecodings(s, 0)

    def canDoGroupedDecoding(self, s: str, i: int) -> bool:
        # we are already at the end
        if i >= len(s) - 1:
            return False
        if int(s[i]) == 0:
            return False
        # we have a 1 and are not at the end, can always group
        if int(s[i]) == 1:
            return True
        return int(s[i]) == 2 and int(s[i + 1]) < 7
    
    @cache
    def doDecodings(self, s: str, i: int) -> int:
        if i > len(s):
            return 0
        if i == len(s):
            return 1
        # this is an impossible path, 0 can only be part of a bigger number
        if s[i] == '0':
            return 0
        
        grouped_decode = 0
        if self.canDoGroupedDecoding(s, i):
            grouped_decode = self.doDecodings(s, i + 2)
        return self.doDecodings(s, i + 1) + grouped_decode
        