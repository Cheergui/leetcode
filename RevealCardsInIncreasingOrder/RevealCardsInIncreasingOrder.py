from collections import deque

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """

        deck.sort()

        queue = deque()

        while deck:
            if queue:
                last = queue.pop()
                queue.appendleft(last)
            card = deck.pop()
            queue.appendleft(card)

        return list(queue)