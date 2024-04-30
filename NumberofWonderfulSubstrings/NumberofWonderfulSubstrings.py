class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """

        res = 0
        prefix = 0  
        count = [0] * 1024  
        count[0] = 1  

        for c in word:
            prefix ^= 1 << ord(c) - ord('a')
            res += count[prefix]
            res += sum(count[prefix ^ 1 << i] for i in range(10))
            count[prefix] += 1

        return res