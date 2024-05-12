class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """

        n = len(grid)


        res = []

        for i in range(1,n-1):
            row = []
            for j in range(1, n-1):
                row.append(max([max(grid[i-1][j-1:j+2]), max(grid[i][j-1:j+2]), max(grid[i+1][j-1:j+2])]))
            res.append(row)
        
        return res