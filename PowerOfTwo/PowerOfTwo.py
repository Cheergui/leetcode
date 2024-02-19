class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n == 0:
            return False

        curr = n
        
        while curr%2 == 0:
            curr = curr // 2

        if curr == 1:
            return True

        return False