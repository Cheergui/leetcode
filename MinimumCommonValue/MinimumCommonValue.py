class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        n, m = len(nums1), len(nums2)
        i, j = 0, 0

        res = -1

        while i < n and j < m and nums1[i] != nums2[j]:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            
        if i < n and j < m:
            res = nums1[i]
        
        return res