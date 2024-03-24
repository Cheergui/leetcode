from collections import defaultdict

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums) - 1

        freq = defaultdict(int)

        for num in nums:
            if freq[num] == 1:
                return num
            else:
                freq[num] += 1