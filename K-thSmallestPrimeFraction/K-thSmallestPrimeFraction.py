import heapq

class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        arr.sort()

        heap = []
        n = len(arr)

        for i in range(n):
            for j in range(i+1, n):
                val = float(arr[i])/float(arr[j])
                heapq.heappush(heap, (val, [arr[i], arr[j]]))

        c = 0

        while c < k:
            val, res = heapq.heappop(heap)
            c += 1

        return res