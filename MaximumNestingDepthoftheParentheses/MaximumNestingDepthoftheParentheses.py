class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        depth = 0

        for character in s:
            if character == "(":
                depth += 1
                res = max(res, depth)
            elif character == ")":
                depth -= 1

        return res