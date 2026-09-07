class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        if len(nums) < 2:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        def dfs(i):
            if i < 2:
                return dp[i]
            if i in dp:
                return dp[i]
            dp[i] = max(dfs(i-2) + nums[i], dfs(i-1))
            return dp[i]
        return dfs(len(nums) - 1) 
        