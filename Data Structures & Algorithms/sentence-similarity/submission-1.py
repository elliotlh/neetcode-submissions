class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        similarDict = collections.defaultdict(set)
        for a, b in similarPairs:
            similarDict[a].add(b)
            similarDict[b].add(a)

        for a, b in zip(sentence1, sentence2):
            if a != b and b not in similarDict[a]:
                return False
        return True

        