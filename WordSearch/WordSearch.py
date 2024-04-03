class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        N, M = len(board), len(board[0])

        visit = set()

        def dfs(i, j, curr):
            if curr == len(word):
                return True
            
            if i == N or i == -1 or j == M or j == -1 or board[i][j] != word[curr] or (i, j) in visit:
                return False

            visit.add((i, j))

            res = dfs(i+1, j, curr+1) or dfs(i, j-1, curr+1) or dfs(i-1, j, curr+1) or dfs(i, j+1, curr+1)

            visit.remove((i, j))

            return res

        for i in range(N):
            for j in range(M):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False