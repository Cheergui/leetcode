from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        
        def findNeighbours(code):
            res = []
            for i in range(4):
                updatedDigit = str((int(code[i]) + 1) % 10)
                res.append(code[:i] + updatedDigit + code[i + 1:])
                
                updatedDigit = str((int(code[i]) - 1) % 10)
                res.append(code[:i] + updatedDigit + code[i + 1:])
            return res
            
        visited = set(deadends)

        if '0000' in visited:
            return -1

        queue = deque()
        queue.append(('0000', 0))

        while queue:
            code, moves = queue.popleft()
            if code == target:
                return moves
            for neighbor in findNeighbours(code):
                if neighbor not in visited:
                    queue.append((neighbor, moves + 1))
                    visited.add(neighbor)

        return -1