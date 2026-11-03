class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0 for _ in range(n+2)]
        memo[1] = 1
        memo[2] = 2
        def dfs(n,memo):
            if memo[n] > 0:
                return memo[n]
            res = dfs(n-1,memo) + dfs(n-2,memo)
            memo[n] = res
            return res
        
        return dfs(n,memo)

            
