class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(arr):
            mem = {}

            def dfs(i):
                if i < 0:
                    return 0
                if i in mem:
                    return mem[i]
                mem[i] = max(dfs(i-1), dfs(i-2) + arr[i])
                return mem[i]
            return dfs(len(arr) - 1)
        return max(solve(nums[:-1]), solve(nums[1:]))
        