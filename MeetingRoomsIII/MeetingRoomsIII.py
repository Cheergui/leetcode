class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """

        def myKey(x):
            return x[0]


        meetings.sort(key=myKey)

        rooms = [0]*n

        count = [0]*n

        for meeting in meetings:
            start, end = meeting[0], meeting[1]
            min, argmin = rooms[0], 0
            full = False
            for i in range(n):
                if rooms[i] < min:
                    argmin = i
                    min = rooms[i]
                if start >= rooms[i]:
                    rooms[i] = end
                    count[i] += 1
                    break
                if i == n-1:
                    full = True
            if full:
                rooms[argmin] = end + rooms[argmin] - start
                count[argmin] += 1
        
        min, res = count[0], 0
        for i in range(n):
            if count[i] > min:
                res = i
                min = count[i]

        return res