class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type K: int
        :rtype: int
        """

        # constants
        MAX_VALUE = max(nums)
        K = k
        N = len(nums)

        # variables
        left_idx = 0
        right_idx = 0
        res = 0
        count = 0


        while right_idx < N:
            while right_idx < N and count < K:
                if nums[right_idx] == MAX_VALUE:
                    count += 1
                if count != K:
                    right_idx += 1
            if right_idx == N:
                break
            tmp_res = (N-1 - right_idx) + 1
            old_left_idx = left_idx
            while count == K:
                if nums[left_idx] == MAX_VALUE:
                    count -= 1
                left_idx += 1
            res += (left_idx - old_left_idx)*tmp_res
            right_idx += 1

        return res