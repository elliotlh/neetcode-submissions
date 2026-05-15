class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        counter = collections.defaultdict(int)
        longest_substring = 0
        for right in range(len(s)):
            # expand window
            counter[s[right]] += 1
            while left < right and counter[s[right]] > 1:
                counter[s[left]] -= 1
                left += 1
            longest_substring = max(longest_substring, right + 1 - left)
        return longest_substring
            
        