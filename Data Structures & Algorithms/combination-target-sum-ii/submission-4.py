class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
        def dfs(i, tgt):
            if tgt == 0:
                res.append(subset.copy())
                return None
            elif tgt < 0 or i >= len(candidates):
                return None
            subset.append(candidates[i])
            dfs(i + 1, tgt - candidates[i])
            while i + 1 <len(candidates) and \
            candidates[i] == candidates[i + 1]:
                i += 1
            subset.pop()
            dfs(i + 1, tgt)
        dfs(0, target)
        return res