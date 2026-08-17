class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums) - 1
        l, r = 0, size
        pivot = nums[l]
        while l <= r:
            m = (l + r) // 2
            if nums[r] > nums[m]:
                r = m
            else:
                pivot = m
                l = m + 1
        l, r = 0, size
        if target > nums[r]:
            r = pivot
        else:
            l = pivot
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

