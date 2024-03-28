from collections import defaultdict

class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = defaultdict(int)

        n = len(nums)

        L = 0
        res = 0

        for R in range(n):
            count[nums[R]] += 1
            if count[nums[R]] <= k:
                res = max(res, R - L + 1)
            else:
                while count[nums[R]] > k:
                    count[nums[L]] -= 1
                    L += 1

        return res