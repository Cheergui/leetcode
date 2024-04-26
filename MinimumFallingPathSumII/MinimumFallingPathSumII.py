from collections import deque

class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)

        for i in range(1,n):
            tmp =  sorted(grid[i-1])
            for j in range(n):
                if grid[i-1][j] == tmp[0]:
                    grid[i][j] += tmp[1]
                else:
                    grid[i][j] += tmp[0]

        return min(grid[-1])