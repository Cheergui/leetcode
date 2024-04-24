class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        cache = {0:0, 1:1, 2:1}

        def recursive(n):
            if n in cache:
                return cache[n]
            
            res = recursive(n-1) + recursive(n-2) + recursive(n-3)

            cache[n] = res

            return res

        res = recursive(n)

        return res