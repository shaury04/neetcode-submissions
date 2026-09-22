class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def recurse(i, ns, goal):
            if i >= len(nums) or goal < 0:
                return None
            if goal == 0:
                res.append(ns.copy())
                return None
            ns.append(nums[i])
            recurse(i, ns, goal - nums[i])
            ns.pop()
            recurse(i + 1, ns, goal)
        recurse(0, [], target)
        return res

