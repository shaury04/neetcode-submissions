class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = defaultdict(int)
        n = len(cost)

        def dfs(i):
            if i < 2:
                return 0
            if i in dp:
                return dp[i]
            dp[i] = min(dfs(i - 1) + cost[i-1], dfs(i - 2) + cost[i - 2])
            return dp[i]

        return dfs(n)