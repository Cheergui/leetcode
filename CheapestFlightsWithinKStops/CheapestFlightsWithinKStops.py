from collections import defaultdict, deque

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        adj = defaultdict(list)
        visited = [float('inf')] * n
        visited[src] = 0
        
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))
            
        queue = deque([(src, 0)])
        k += 1
        
        while k > 0 and queue:
            size = len(queue)
            while size > 0:
                curr_node, curr_price = queue.popleft()
                for neighbor, price in adj[curr_node]:
                    new_price = curr_price + price
                    if new_price < visited[neighbor]:
                        visited[neighbor] = new_price
                        queue.append((neighbor, new_price))
                size -= 1
            k -= 1
        
        return visited[dst] if visited[dst] != float('inf') else -1