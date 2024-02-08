import math 

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #initialization of the dynamic programming array
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        
        #computing the least number of perfect square numbers that sum to i for each i
        for i in range(1,n+1):
            m = int(math.sqrt(i))
            
            """
            If we assume that we have all the values before dp[i], we can compute dp[i] by going 
            through all the possible perfect square numbers before i and choose the one (say k) 
            that gives the least number of perfect square numbers that sum to i-k.
            """
            for j in range(1,m+1):
                dp[i] = min(dp[i], dp[i-j**2]+1)

        #returning the least number of perfect square numbers that sum to n
        return dp[n]