from collections import defaultdict

class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        res = [0] * n
        count = [1] * n
        tree = defaultdict(set)

        for u, v in edges:
            tree[u].add(v)
            tree[v].add(u)

        def postorder(node, parent=None):
            for child in tree[node]:
                if child == parent:
                    continue
                postorder(child, node)
                count[node] += count[child]
                res[node] += res[child] + count[child]

        def preorder(node, parent=None):
            for child in tree[node]:
                if child == parent:
                    continue
                res[child] = res[node] - count[child] + (n - count[child])
                preorder(child, node)

        postorder(0)
        preorder(0)
        return res