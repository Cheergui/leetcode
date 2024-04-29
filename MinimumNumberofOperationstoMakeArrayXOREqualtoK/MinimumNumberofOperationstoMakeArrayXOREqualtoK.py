class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        final_xor = 0

        for n in nums:
            final_xor = final_xor ^ n

        res = 0

        while k or final_xor:
            if (k % 2) != (final_xor % 2):
                res += 1
            k //= 2
            final_xor //= 2

        return res