import heapq
from collections import deque

class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid) - 1] == 1:
            return 0
        test = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    test[i][j] = 0
                    q.append([i, j])
        level = 0
        while q:
            size = len(q)
            level += 1
            for i in range(size):
                pop = q.popleft()
                x, y = pop[0], pop[1]
                for nx, ny in dirs:
                    newX = x + nx
                    newY = y + ny
                    if 0 <= newX < len(test) and 0 <= newY < len(test[0]) and test[newX][newY] == float('inf'):
                        test[newX][newY] = level
                        q.append([newX, newY])
        m = len(grid)
        n = len(grid[0])
        min_heap = []
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        heapq.heappush(min_heap, (-test[0][0], 0, 0))
        dp[0][0] = test[0][0]
        while min_heap: 
            pop = heapq.heappop(min_heap)
            dist, i, j = -pop[0], pop[1], pop[2]
            for x, y in dirs:
                nx = i + x
                ny = j + y
                if 0 <= nx < m and 0 <= ny < n and dp[nx][ny] < min(dist, test[nx][ny]):
                    dp[nx][ny] = min(dist, test[nx][ny])
                    heapq.heappush(min_heap, (-dp[nx][ny], nx, ny))
        return dp[-1][-1]