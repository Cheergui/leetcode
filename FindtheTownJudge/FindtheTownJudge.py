class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        town = {i: [] for i in range(1, n+1)}

        for t in trust:
            town[t[0]].append(t[1])

        judge = None

        for person in town:
            if town[person] == [] and judge == None:
                judge = person
                break

        if judge == None:
            return -1
        
        for person in town:
            if person != judge:
                if judge not in town[person]:
                    return -1

        return judge