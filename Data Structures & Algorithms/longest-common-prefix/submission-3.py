class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        longest = strs[0]
        for option in strs[1:]:
            i = 0
            for j in range(min(len(longest), len(option))):
                if option[j] == longest[j]:
                    i = j + 1
                else:
                    break
            longest = longest[:i]
            if len(longest) == 0:
                return ''
        return ''.join(longest)
            
        