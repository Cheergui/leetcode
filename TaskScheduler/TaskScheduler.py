from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        counter = Counter(tasks)
        freqs = list(counter.values())
        max_freq = max(freqs)

        count = 0

        for freq in freqs:
            if freq == max_freq:
                count += 1

        res = max((max_freq-1)*(n+1) + count, len(tasks))

        return res