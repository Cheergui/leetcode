class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = [0]*101

        for num in nums:
            count[num] += 1

        max_freq = max(count)

        res = 0

        for f in count:
            if f == max_freq:
                res += 1

        res *= max_freq
        
        return res