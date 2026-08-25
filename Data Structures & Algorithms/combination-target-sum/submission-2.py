class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i, tgt):
            if tgt == 0:
                res.append(subset.copy())
                return
            elif tgt < 0 or i >= len(nums):
                return None
            subset.append(nums[i])
            dfs(i, tgt - nums[i])
            subset.pop()
            dfs(i + 1, tgt)            

        dfs(0, target)
        return res