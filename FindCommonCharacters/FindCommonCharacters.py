import string

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        res = []

        letters = string.ascii_lowercase

        for letter in letters:
            min_freq = float('inf')
            for word in words:
                freq = 0
                for char in word:
                    if char == letter:
                        freq += 1
                if freq < min_freq:
                    min_freq = freq
            if min_freq != float('inf'):
                for _ in range(min_freq):
                    res.append(letter)
        
        return res