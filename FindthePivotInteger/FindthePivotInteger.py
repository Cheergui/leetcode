class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [num for num in range(1,n+1)]
        right = sum(nums)
        left = 0

        res = -1

        for num in nums:
            left += num
            if left == right:
                res = num
                break
            right -= num
        
        return res