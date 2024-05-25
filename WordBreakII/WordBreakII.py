class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        n = len(s)
        word_set = set(wordDict)
        res = []

        def recursive(start, path):
            if start == n:
                res.append(' '.join(path))
                return

            for end in range(start + 1, n + 1):
                word = s[start:end]
                if word in word_set:
                    recursive(end, path + [word])

        recursive(0, [])
        return res