class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        if n == 0:
            return 0
        
        res = [0]

        def recursive(i, xor_total):
            if i == n:
                return

            recursive(i+1, xor_total)

            xor_total ^= nums[i]
            res[0] += xor_total
            recursive(i+1, xor_total)

        recursive(0, 0)

        return res[0]