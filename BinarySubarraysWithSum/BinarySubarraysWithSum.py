from collections import Counter
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        res = 0

        prefix = 0

        count = Counter({0:1})

        for num in nums:
            prefix += num
            res += count[prefix-goal]
            count[prefix] += 1

        return res