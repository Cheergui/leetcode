class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []
        pos = []
        neg = []

        n = len(nums)

        for i in range(n-1, -1, -1):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        for i in range(n):
            if i%2 == 0:
                res.append(pos.pop())
            else:
                res.append(neg.pop())

        return res