class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_dict: Dict[str, List[str]] = collections.defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            key_dict[key].append(word)
        return [x for x in key_dict.values()]
        