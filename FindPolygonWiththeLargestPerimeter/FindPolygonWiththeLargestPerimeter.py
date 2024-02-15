class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        n = len(nums)

        res = -1
        
        curr = nums[0] + nums[1]

        for i in range(2,n):
            tmp = curr
            curr += nums[i]
            if tmp > nums[i]:
                res = curr

        return res