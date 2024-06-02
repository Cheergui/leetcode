class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        k = len(s) // 2
        
        for i in range(k):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]