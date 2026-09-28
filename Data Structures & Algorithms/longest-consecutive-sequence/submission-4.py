class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in numbers:
                length = 1
                while nums[i] + length in numbers:
                    length += 1
                count = max(count, length)
        return count 