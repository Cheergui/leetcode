class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        if left == right:
            return left

        b_left = bin(left)[2:]
        b_right = bin(right)[2:]

        res = 0

        if len(b_right) - len(b_left) >= 1:
            return res
        else:
            k = len(b_right)
            diff = right - left
            b_diff = bin(diff)[2:]
            i = 0
            while i < k - len(b_diff):
                if b_left[i] == b_right[i] and b_left[i] == '1':
                    res += 2**(k-1-i)
                i += 1
            return res