class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        long = 0

        for n in ns:
            if (n-1) not in ns:
                length = 1
                while (n + length) in ns:
                    length += 1
                long = max(length, long)
        return long