class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        n = len(people)

        people.sort()

        L, R = 0, n-1

        res = 0

        while L <= R:
            res += 1
            person1 = people[R]
            person2 = people[L]
            R -= 1
            if person1 + person2 <= limit:
                L += 1

        return res