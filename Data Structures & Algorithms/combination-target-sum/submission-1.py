class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(subset, i, tgt):
            if tgt == 0:
                return res.append(subset.copy())
            elif tgt < 0 or i >= len(nums):
                return None
            subset.append(nums[i])
            dfs(subset, i, tgt - nums[i])
            subset.pop()
            dfs(subset, i + 1, tgt)            

        dfs(subset, 0, target)
        return res