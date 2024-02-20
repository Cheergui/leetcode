class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        numbers = set([i for i in range(n+1)])

        for num in nums:
            numbers.remove(num)

        return numbers.pop()