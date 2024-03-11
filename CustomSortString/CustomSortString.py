class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """

        hashmap = {order[i]:i for i in range(len(order))}

        i = 0

        n = len(s)

        s = list(s)

        while i < n:
            if s[i] in hashmap:
                order_i = hashmap[s[i]]
                j = i
                order_j = hashmap[s[i]]
                for k in range(i+1, n):
                    if s[k] in hashmap and hashmap[s[k]] < order_j:
                        j = k
                        order_j = hashmap[s[k]]
                s[i], s[j] = s[j], s[i]
            i += 1
        
        res = "".join(s)

        return res