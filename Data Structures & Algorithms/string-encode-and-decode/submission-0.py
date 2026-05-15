from typing import Tuple

class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        for x in strs:
            out.append(str(len(x)) + '|' + x)
        return ''.join(out)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            loop_length, word_start = self.extractLoopLength(s, i)
            decoded.append(s[word_start:word_start + loop_length])
            i = word_start + loop_length
        return decoded


    def extractLoopLength(self, s: str, i: int) -> Tuple[int, int]:
        length = ''
        word_start = i
        for k in range(i, len(s)):
            if s[k].isnumeric():
                length += s[k]
            elif s[k] == '|':
                word_start = k + 1
                break
        if length == '':
            return 0, word_start
        return int(length), word_start

