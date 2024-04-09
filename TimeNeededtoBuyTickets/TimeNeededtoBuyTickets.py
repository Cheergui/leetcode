from collections import deque

class Node:
    def __init__(self, val=0):
        self.val = val

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """

        queue = deque()

        N = len(tickets)

        node_k = None

        res = 0

        for i in range(N):
            node = Node(val=tickets[i])
            queue.append(node)
            if i == k:
                node_k = node

        while node_k.val != 0:
            
            node = queue.popleft()

            if node.val > 0:
                node.val -= 1
                res += 1

            queue.append(node)

        return res  