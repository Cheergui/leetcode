class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0

        product = 1
        n = len(nums)

        j, res = 0, 0

        for i in range(n):
            product *= nums[i]
            while product >= k and j <= i:
                product /= nums[j]
                j += 1
            res += i-j+1

        return res