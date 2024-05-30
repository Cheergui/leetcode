class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        
        L, R = 0, 0

        n = len(s)

        res = 0
        cost = 0

        while R < n:
            if L > R:
                R = L
            while R < n and cost <= maxCost:
                cost += abs(ord(s[R])-ord(t[R]))
                R += 1
                if R-L> res and cost <= maxCost:
                    res = R-L
            if R == n:
                break
            while L <= R and cost > maxCost:
                cost -= abs(ord(s[L])-ord(t[L]))
                L += 1

        return res