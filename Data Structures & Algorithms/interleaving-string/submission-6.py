from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def checkInterleaving(i: int, j: int, k: int) -> bool:
            if i > len(s1) or j > len(s2) or k > len(s3):
                return False
            while i < len(s1) and j < len(s2) and k < len(s3):
                # No match possible
                if s1[i] != s3[k] and s2[j] != s3[k]:
                    return False
                # We can ONLY pull from S1
                if s1[i] == s3[k] and s2[j] != s3[k]:
                    i += 1
                    k += 1
                # You can ONLY pull from S2
                elif s1[i] != s3[k] and s2[j] == s3[k]:
                    j += 1
                    k += 1
                else:
                    # We have to check both interleavings
                    return (
                        checkInterleaving(i + 1, j, k + 1)
                        or
                        checkInterleaving(i, j + 1, k + 1)
                    )
            
            if i < len(s1):
                return s1[i:] == s3[k:]
            if j < len(s2):
                return s2[j:] == s3[k:]
            return k == len(s3)
        return checkInterleaving(0, 0, 0)

        