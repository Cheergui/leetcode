class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows, cols = len(grid), len(grid[0])
        
        res = [0]

        visited = set()

        def in_range(i, j):
            if i > -1 and i < rows and j > -1 and j < cols:
                return True
            return False

        i_start, j_start = 0, 0

        found = False

        for i in range(rows):
            if found:
                break
            for j in range(cols):
                if grid[i][j] == 1:
                    i_start, j_start = i, j
                    found = True
                    break
            

        def recursive(grid, i, j):
            if (i,j) in visited:
                return
        
            visited.add((i,j))

            if in_range(i, j+1) and grid[i][j+1] == 1:
                recursive(grid, i, j+1)
            else:
                res[0] += 1

            if in_range(i-1, j) and grid[i-1][j] == 1:
                recursive(grid, i-1, j)
            else:
                res[0] += 1

            if in_range(i, j-1) and grid[i][j-1] == 1:
                recursive(grid, i, j-1)
            else:
                res[0] += 1

            if in_range(i+1, j) and grid[i+1][j] == 1:
                recursive(grid, i+1, j)
            else:
                res[0] += 1

        recursive(grid, i_start, j_start)

        return res[0]