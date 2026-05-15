class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 0:
            return []
        # Step 1: get the last occurrence of each letter
        last_occurrence = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in last_occurrence:
                last_occurrence[s[i]] = i
        
        # Process the substring, for each char in the substring,
        # update the right pointer in two pointer to max(right, last_occurrence)
        # if right == last_occurrence, snapshot that as a valid substring
        right = last_occurrence[s[0]]
        left = -1
        results = []
        for i in range(len(s)):
            right = max(right, last_occurrence[s[i]])
            if i == right:
                results.append(right - left)
                left = i
            
            
        return results

        