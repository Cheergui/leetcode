class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        def helper(arr):
            
            n = len(arr)
            return arr[:n//2] == arr[:n//2 + 1*(n%2==1)-1:-1]

        for word in words:
            if helper(word):
                return word

        return ""