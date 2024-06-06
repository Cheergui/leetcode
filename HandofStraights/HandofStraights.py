from collections import defaultdict

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """

        if len(hand) % groupSize != 0:
            return False

        freq = defaultdict(int)

        for card in hand:
            freq[card] += 1
        
        keys = freq.keys()

        keys.sort()

        for key in keys:
            freq_key = freq[key]
            if freq_key > 0:
                for i in range(groupSize):
                    freq[key+i] -= freq_key
                    if freq[key+i] < 0:
                        return False
        
        return True