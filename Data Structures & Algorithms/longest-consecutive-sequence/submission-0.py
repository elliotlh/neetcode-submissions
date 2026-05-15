class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set(nums)
        biggest = 0
        for num in nums:
            seq_len = 0
            if (num - 1) not in exists:
                start = num
                while start in exists:
                    seq_len += 1
                    start += 1
                biggest = max(seq_len, biggest)
        return biggest
        
