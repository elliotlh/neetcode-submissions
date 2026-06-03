class Solution:
    def areWordsSorted(self, ord_weight: Dict[str, int], a: str, b: str) -> bool:
        r = min(len(a), len(b))
        for i in range(r):
            if ord_weight[a[i]] < ord_weight[b[i]]:
                return True
            if ord_weight[a[i]] > ord_weight[b[i]]:
                return False
        return len(a) <= len(b)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord_weight = {}
        for weight, char in enumerate(order):
            ord_weight[char] = weight
        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]
            if not self.areWordsSorted(ord_weight, a, b):
                return False
        return True




        