class LetterCounts:
    def __init__(self, word: str):
        self.counts = collections.Counter(word)
        self.required_chars = len(word)

    def processed_substring(self) -> bool:
        return self.required_chars <= 0

    def mark_seen(self, char: str):
        if char not in self.counts:
            return
        if self.counts[char] > 0:
            self.required_chars -= 1
        self.counts[char] -= 1

    def remove_seen(self, char: str):
        if char not in self.counts:
            return
        if self.counts[char] >= 0:
            self.required_chars += 1
        self.counts[char] += 1

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = LetterCounts(t)
        left, right = 0, 0
        candidate = s
        expect_candidate = False
        while right < len(s):
            if not t_counts.processed_substring():
                t_counts.mark_seen(s[right])
                right += 1
            else:
                expect_candidate = True
                candidate = min(candidate, s[left:right], key=len)
                t_counts.remove_seen(s[left])
                left += 1
                
                
        while t_counts.processed_substring() and left < len(s):
            expect_candidate = True
            candidate = min(candidate, s[left:right], key=len)
            t_counts.remove_seen(s[left])
            left += 1
        return candidate if expect_candidate else ''

        