class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        n = len(nums)

        res = [0]

        def recursive(i, subset):
            if i == n:
                if len(subset) > 0:
                    res[0] += 1
                return
            
            recursive(i+1, subset)

            if  nums[i] + k not in subset and nums[i] - k not in subset:
                tmp = subset.copy()
                tmp.add(nums[i])
                subset = tmp.copy()
                recursive(i+1, subset)
            else:
                return

        recursive(0, set())

        return res[0]