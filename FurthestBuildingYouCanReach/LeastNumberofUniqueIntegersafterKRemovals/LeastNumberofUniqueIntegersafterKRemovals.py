class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        freq = {}

        for num in arr:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        tmp = []

        for num in freq:
            tmp.append([num, freq[num]])

        def f(x):
            return x[1]

        tmp.sort(key=f)

        length = len(tmp)
        
        count = 0
        
        for i in range(length):
            count += tmp[i][1]
            if count == k:
                return length - i - 1
            elif count > k:
                return length - i
