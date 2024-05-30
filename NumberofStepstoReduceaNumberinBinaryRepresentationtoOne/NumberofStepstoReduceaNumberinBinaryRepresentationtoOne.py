class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """

        step = len(s) - 1
        carry_over = 0
        res = 0

        while (step > 0):
            if int(s[step]) + carry_over == 0:
                carry_over = 0
                res += 1
            elif int(s[step]) + carry_over == 2:
                carry_over = 1
                res += 1
            else:
                carry_over = 1
                res += 2
            step -= 1
            
        if carry_over == 1:
            res += 1

        return res