from collections import deque, defaultdict

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        adjList = defaultdict(set)

        for a,b in edges:
            adjList[a].add(b)
            adjList[b].add(a)
        
        leaves = [i for i in adjList if len(adjList[i]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in range(len(leaves)):
                leaf = leaves.pop()
                for neighbor in adjList[leaf]:
                    adjList[neighbor].remove(leaf)
                    if len(adjList[neighbor]) == 1:
                        newLeaves.append(neighbor)
            leaves = newLeaves
        
        return leaves