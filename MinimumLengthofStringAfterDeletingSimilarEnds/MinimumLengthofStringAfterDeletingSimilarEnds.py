class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """

        L, R = 0, len(s) - 1

        while L < R and s[L] == s[R]:
            val = s[L]
            while L <= R and s[L] == val:
                L += 1
            while L <= R and s[R] == val:
                R -= 1
        
        return max(0, R-L+1)