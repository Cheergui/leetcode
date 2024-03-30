from collections import defaultdict

class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # constants
        N = len(nums)
        K = k

        # variables
        count = defaultdict(int)
        visited = set()
        right_idx = 0
        left_idx = 0
        res = 0

        while right_idx < N:
            while right_idx < N and (len(visited) < K or nums[right_idx] in visited):
                num = nums[right_idx]
                visited.add(num)
                count[num] += 1
                if right_idx + 1 < N and len(visited) == K and nums[right_idx+1] in visited:
                    right_idx += 1
                    res += 1
            if right_idx == N:
                break
            while len(visited) == K:
                res += 1
                num = nums[left_idx]
                count[num] -= 1
                left_idx += 1
                if count[num] == 0:
                    visited.remove(num)
            right_idx += 1

        return res