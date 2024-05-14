class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        res = [0]

        m = len(grid)
        n = len(grid[0])

        def recursive(grid, i, j, visited, amount):
            if i == -1 or i == m or j == -1 or j == n or (i,j) in visited or grid[i][j] == 0:
                if amount > res[0]:
                    res[0] = amount
                return
            
            visited.add((i,j))
            amount += grid[i][j]

            recursive(grid, i, j+1, visited, amount)
            recursive(grid, i-1, j, visited, amount)
            recursive(grid, i, j-1, visited, amount)
            recursive(grid, i+1, j, visited, amount)

            visited.remove((i,j))
        
        for i in range(m):
            for j in range(n):
                recursive(grid, i, j, set(), 0)

        return res[0]