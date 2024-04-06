from collections import defaultdict

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        count = defaultdict(int)

        for character in s:
            if character == '(' or character == ')':
                count[character] += 1
        
        res = ''
        tmp = 0

        for character in s:
            if character == '(':
                if tmp < count[')']:
                    res += character
                    tmp += 1
            elif character == ')':
                if tmp > 0:
                    res += character
                    tmp -= 1
                count[character] -= 1
            else:
                res += character
        
        return res