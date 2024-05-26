class Solution:
    def checkRecord(self, n):   

        MOD = 10**9+7


        dp = [[[0 for _ in range (2) ] for _ in range(3)] for _ in range(n+1)]

        dp[1][0][0]=1
        dp[1][0][1]=1
        dp[1][1][0]=1
        dp[1][1][1]=0
        dp[1][2][0]=0
        dp[1][2][1]=0        

        for i in range (2,n+1):
            dp[i][0][0] = (dp[i-1][0][0] + dp[i-1][1][0] + dp[i-1][2][0]) % MOD 
            dp[i][0][1] = (dp[i-1][0][0] + dp[i-1][1][0] + dp[i-1][2][0]) % MOD + (dp[i-1][0][1] + dp[i-1][1][1] + dp[i-1][2][1]) %MOD 
            dp[i][1][0] = dp[i-1][0][0] % MOD 
            dp[i][1][1] = dp[i-1][0][1] % MOD 
            dp[i][2][0] = dp[i-1][1][0] % MOD 
            dp[i][2][1] = dp[i-1][1][1] % MOD 
            
        res = 0

        for i in range(3):
            for j in range(2):
                res += dp[-1][i][j]
                res %= MOD 
                
        return res