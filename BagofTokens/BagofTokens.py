from collections import deque

class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """

        score = 0
        
        if len(tokens) == 0:
            return score

        tokens.sort()

        queue = deque(tokens)

        while queue:
            while queue and power >= queue[0]:
                token = queue.popleft()
                power -= token
                score += 1
            if len(queue) > 1 and score >= 1:
                token = queue.pop()
                power += token
                score -= 1
            else:
                break
        return score