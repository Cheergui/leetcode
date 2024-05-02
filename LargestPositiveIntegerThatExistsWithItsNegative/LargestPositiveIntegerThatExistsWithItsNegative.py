class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)

        res = -1

        for num in nums:
            if -num in nums and num>res:
                res = num

        return res