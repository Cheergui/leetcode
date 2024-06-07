class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """

        n = len(sentence)

        words = sentence.split()

        dictionary = set(dictionary)

        res = []

        for word in words:
            i = 0
            m = len(word)
            while i < m and word[:i+1] not in dictionary:
                i += 1
            if i == m:
                res.append(word)
            else:
                res.append(word[:i+1])
            
        res = " ".join(res)

        return res