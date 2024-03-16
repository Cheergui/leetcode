class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashmap = {}

        sum = 0
        
        res = 0

        for i, num in enumerate(nums):
            if num == 1:
                sum += 1
            else:
                sum -= 1
            if sum == 0:
                res = i + 1
            elif sum in hashmap:
                if i - hashmap[sum] > res:
                    res = i - hashmap[sum]
            else:
                hashmap[sum] = i

        return res