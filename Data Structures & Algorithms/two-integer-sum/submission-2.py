class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        goal = {}
        for i,n in enumerate(nums):
            if target - n in goal:
                return [goal[target - n], i]
            goal[n] = i
        return [0,0]