class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        N = len(s)

        i = 0
        wordmap = {}
        mapped = set()

        while i < N:
            if s[i] not in wordmap:
                if t[i] not in mapped:
                    wordmap[s[i]] = t[i]
                    mapped.add(t[i])
                else:
                    return False
            else:
                if t[i] != wordmap[s[i]]:
                    return False
            i += 1
        
        return True