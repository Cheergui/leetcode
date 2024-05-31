class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.sort()
        nums.append(None)
        n = len(nums)

        res = []

        i = 0

        while i < n-1 :
            if nums[i] == nums[i+1]:
                i += 2
            else:
                res.append(nums[i])
                i += 1
        
        return res