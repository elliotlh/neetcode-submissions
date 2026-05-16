class Solution:
    def firstMissingPositive(self, nums) -> int:
        nums.append(len(nums) + 1)
        n = len(nums)
        for i in range(len(nums)):
            nums[i] = (nums[i], False)
        for num, _ in nums:
            if num > 0 and num < n:
                nums[num] = (nums[num][0], True)
        for i in range(1, len(nums)):
            _, present = nums[i]
            if not present:
                return i
        return len(nums)
            


        