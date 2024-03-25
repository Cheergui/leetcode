from collections import defaultdict

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = set()

        freq = defaultdict(int)

        for num in nums:
            if freq[num] == 1:
                res.add(num)
            if freq[num] == 2:
                res.remove(num)
            freq[num] += 1

        res = list(res)

        return res