class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        One brute force idea is that we iterate over s. Each time we find a matching
        word, we store the current state (e.g. splitting neet with a space) and then
        recurse. We will do this for ALL possible breaks. Since wordDict is unique,
        this should result in unique sentences. 

        This is expensive because we perform a lot of repeated subcalculations. To
        optimize, we could store a list of possible sentences from any index dp[i]
        where dp[i] = List[str] where List[str] = a list of possible _sentences_ from
        that index. When constructing a sentence this way, we simply take our current
        sentence and apply it to the list of possible sentences from this particular index

        Space complexity might be enormous to cache it this way, but that would yield
        better time complexity.

        Brute force pseudocode:

        """
        biggest_word = len(max(wordDict, key=len))
        word_set = set(wordDict)
        res = []
        def splitWord(i: int, current_sentence: List[str]):
            if i > len(s):
                return
            if i == len(s):
                res.append(' '.join(current_sentence))
                return
            for j in range(i, i + biggest_word + 1):
                if s[i:j+1] in word_set:
                    current_sentence.append(s[i:j+1])
                    splitWord(j+1,current_sentence)
                    current_sentence.pop()
            
        splitWord(0, [])
        return res
        