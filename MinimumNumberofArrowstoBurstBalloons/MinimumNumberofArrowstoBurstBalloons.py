class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        res = 0

        n = len(points)

        def myKey(x):
            return x[0]

        points.sort(key=myKey)

        i = n-1

        while i > -1:
            curr = points[i][0]
            res += 1
            while i > -1 and curr >= points[i][0] and curr <= points[i][1]:
                i -= 1
        
        return res