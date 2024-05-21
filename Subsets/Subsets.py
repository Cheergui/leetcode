class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n = len(nums)

        res = [[]]

        def recursive(i, tmp):
            if i == n:
                return
            
            recursive(i+1, tmp[:])

            tmp.append(nums[i])
            res.append(tmp[:])
            recursive(i+1, tmp[:])

        recursive(0, [])

        return res