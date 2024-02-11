class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])

        hashmap = {}
        
        def dp(i, j1, j2):

            if j1 < 0 or j1 == cols or j2 < 0 or j2 == cols or i == rows:
                return 0

            if (i, j1, j2) in hashmap:
                return hashmap[(i, j1, j2)]

            if j1 == j2:
                res = grid[i][j1] + max(dp(i+1, j1-1, j2-1),
            dp(i+1, j1, j2-1),
            dp(i+1, j1+1, j2-1),
            dp(i+1, j1-1, j2),
            dp(i+1, j1, j2),
            dp(i+1, j1+1, j2),
            dp(i+1, j1-1, j2+1),
            dp(i+1, j1, j2+1),
            dp(i+1, j1+1, j2+1))
            else:
                res = grid[i][j1] + grid[i][j2] + max(dp(i+1, j1-1, j2-1),
            dp(i+1, j1, j2-1),
            dp(i+1, j1+1, j2-1),
            dp(i+1, j1-1, j2),
            dp(i+1, j1, j2),
            dp(i+1, j1+1, j2),
            dp(i+1, j1-1, j2+1),
            dp(i+1, j1, j2+1),
            dp(i+1, j1+1, j2+1))

            hashmap[(i, j1, j2)] = res

            return res


        return dp(0, 0, cols-1)