class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)

        res = 0

        for i in range(n-1):
            res += abs(ord(s[i+1])-ord(s[i]))

        return res