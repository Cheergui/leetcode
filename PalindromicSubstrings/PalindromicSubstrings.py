class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)

        res = 0

        dp = [[False]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            res += 1

        for i in range(n-1):
            dp[i][i+1] = (s[i] == s[i+1])
            res += dp[i][i+1]

        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                res += dp[i][j]

        return res

