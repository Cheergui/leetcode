class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        revisions1 = version1.split('.')
        revisions2 = version2.split('.')

        n1 = len(revisions1)
        n2 = len(revisions2)

        if n1 < n2:
            for _ in range(n2-n1):
                revisions1.append('0')
        else:
            for _ in range(n1-n2):
                revisions2.append('0')
        
        n = len(revisions1)

        i = 0

        while i < n  and int(revisions1[i]) == int(revisions2[i]):
            i += 1

        if i == n:
            return 0
        
        if int(revisions1[i]) < int(revisions2[i]):
            return -1
        
        return 1