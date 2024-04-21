from collections import deque, defaultdict

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """

        if edges == []:
            return True

        adjList = defaultdict(list)
        visited = set()

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        queue = deque()
        queue.append(source)

        while queue:
            for i in range(len(queue)):
                vertex = queue.popleft()
                for neighbor in adjList[vertex]:
                    if neighbor not in visited:
                        if neighbor == destination:
                            return True
                        else:
                            queue.append(neighbor)
                            visited.add(neighbor)
        
        return False