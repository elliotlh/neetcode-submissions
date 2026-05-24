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
        """
        biggest_word = len(max(wordDict, key=len))
        word_set = set(wordDict)
        possible_words_from_index = collections.defaultdict(list)
        for i in range(len(s)):
            for j in range(i, min(i+biggest_word, len(s))):
                if s[i:j+1] in word_set:
                    possible_words_from_index[i].append(s[i:j+1])
        res = []
        current_sentence = []
        def splitWord(i: int, current_sentence: List[str]):
            if i > len(s):
                return
            if i == len(s):
                return res.append(' '.join(current_sentence))
            for candidate in possible_words_from_index[i]:
                current_sentence.append(candidate)
                splitWord(i + len(candidate), current_sentence)
                current_sentence.pop()
            
        splitWord(0, [])
        return res
        