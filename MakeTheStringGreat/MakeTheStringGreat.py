class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """

        letters = list(s)[::-1]
        
        res = letters[-1]

        letters.pop()


        while letters:
            new_letter = letters.pop()
            if res and new_letter.islower()*res[-1].islower() == False and \
                    new_letter.isupper()*res[-1].isupper() == False and \
                    new_letter.lower() == res[-1].lower():
                res = res[:-1]
            else:
                res += new_letter

        return res