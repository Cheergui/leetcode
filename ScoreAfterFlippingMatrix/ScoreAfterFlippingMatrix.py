class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])

        for i in range(m):
            if grid[i][0] == 0:
                grid[i] = [1-grid[i][j] for j in range(n)]

        res = 0

        for j in range(n):
            number_ones = 0
            for i in range(m):
                number_ones += grid[i][j]
            if 2*number_ones < m:
                number_ones = m-number_ones
            res += 2**(n-1-j) * number_ones

        return res