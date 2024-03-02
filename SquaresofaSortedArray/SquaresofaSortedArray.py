class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        neg = []
        pos = []

        for num in nums:
            if num < 0:
                neg.append(num**2)
            else:
                pos.append(num**2)

        res = []

        i, j = len(neg)-1, 0


        while i > -1 and j < len(pos):
            if neg[i] < pos[j]:
                res.append(neg[i])
                i -= 1
            else:
                res.append(pos[j])
                j += 1
        
        if i == -1:
            while j < len(pos):
                res.append(pos[j])
                j += 1
        if j == len(pos):
            while i > -1:
                res.append(neg[i])
                i -= 1
        
        return res