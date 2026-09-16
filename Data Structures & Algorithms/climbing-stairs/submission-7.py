class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [0] * (n+1)
        def dfs(n):
            if n <= 1:
                return 1
            if mem[n] != 0:
                return mem[n]
            mem[n] = dfs(n-1) + dfs(n-2)
            return mem[n]
        return dfs(n)