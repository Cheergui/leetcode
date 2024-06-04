from collections import defaultdict

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = defaultdict(int)

        for letter in s:
            count[letter] += 1
        
        res = 0

        flag = False

        for key in count:
            if count[key] % 2 == 0:
                res += count[key]
            else:
                flag = True
                res += count[key] - 1

        if flag:
            res += 1
        
        return res