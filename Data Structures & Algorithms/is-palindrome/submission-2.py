import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = r"[^a-zA-Z0-9]"
        cleaned = re.sub(stripped, '', s)
        clean = cleaned.lower().strip()
        return clean == clean[::-1]
        