import heapq

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted((float(w)/q, q, w) for q, w in zip(quality, wage))

        heap = []
        sum_quality = 0
        min_cost = float('inf')

        for rate, q, w in workers:
            heapq.heappush(heap, -q)
            sum_quality += q

            if len(heap) > k:
                sum_quality += heapq.heappop(heap)

            if len(heap) == k:
                min_cost = min(min_cost, rate * sum_quality)

        return min_cost