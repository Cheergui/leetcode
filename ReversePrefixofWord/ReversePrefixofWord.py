class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """

        if ch not in word:
            return word
        
        n = len(word)

        stack = []

        i = 0 

        while i < n and word[i] != ch:
            stack.append(word[i])
            i += 1

        stack.append(ch)

        res = "".join(stack[::-1])

        for k in range(i+1, n):
            res += word[k]

        return res