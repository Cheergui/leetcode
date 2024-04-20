class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """

        m, n = len(land), len(land[0])

        visited = set()
        neighbors = set()
        farmland = [m-1, n-1, 0, 0]

        res = []

        def in_range(i, j):
            if i > -1 and i < m and j > -1 and j < n:
                return True
            return False


        def recursive(land, i, j, val):
            if not in_range(i,j) or (i,j) in visited:
                return
            elif land[i][j] != val:
                neighbors.add((i,j))
                return

            if val == 1:
                if i <= farmland[0] and j <= farmland[1]:
                    farmland[0], farmland[1] = i, j
                if i >= farmland[2] and j >= farmland[3]:
                    farmland[2], farmland[3] = i, j

            visited.add((i,j))

            recursive(land, i, j+1, val)
            recursive(land, i-1, j, val)
            recursive(land, i, j-1, val)
            recursive(land, i+1, j, val)

        recursive(land, 0, 0, land[0][0])
        if land[0][0] == 1:
            res.append(farmland)

        while neighbors:
            farmland = [m-1, n-1, 0, 0]
            i,j = neighbors.pop()
            if (i,j) not in visited:
                recursive(land, i, j, land[i][j])
                if land[i][j] == 1:
                    res.append(farmland)
        
        return res