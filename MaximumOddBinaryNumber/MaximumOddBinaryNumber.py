class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)

        count = s.count('1')
        
        res = '1'*(count-1) + '0'*(n-count) + '1'

        return res