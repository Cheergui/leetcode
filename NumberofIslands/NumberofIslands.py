class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        rows, cols = len(grid), len(grid[0])

        res = [int(grid[0][0])]

        visited = set()
        neighbors = set()

        def in_range(i, j):
            if i > -1 and i < rows and j > -1 and j < cols:
                return True
            return False

        def recursive(grid, i, j, val):
            if not in_range(i, j) or (i,j) in visited:
                return
            elif grid[i][j] != val:
                neighbors.add((i,j))
                return
            
            visited.add((i,j))

            recursive(grid, i, j+1, val)
            recursive(grid, i-1, j, val)
            recursive(grid, i, j-1, val)
            recursive(grid, i+1, j, val)
        
        recursive(grid, 0, 0, grid[0][0])

        while neighbors:
            i, j = neighbors.pop()
            if (i,j) not in visited:
                res[0] += int(grid[i][j])
                recursive(grid, i, j, grid[i][j])

        return res[0]