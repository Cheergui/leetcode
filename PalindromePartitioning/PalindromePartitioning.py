class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        n = len(s)

        def recursive(i, part):
            if i == n:
                return part

            if i == 0:
                part.append([s[i]])
                return recursive(i+1, part[:])
            else:
                tmp = []

                for p in part:
                    copy = p[:]
                    copy[-1] = copy[-1] + s[i]
                    tmp.append(copy[:])

                    copy = p[:]
                    copy.append(s[i])
                    tmp.append(copy[:])

                part = tmp[:]

                return recursive(i+1, part)

        partition = recursive(0, [])

        def helper(string):
            n = len(string)
            reverted = string[::-1]
            print(reverted[:n//2])
            return string[:n//2] == reverted[:n//2]

        res = []

        for i in range(len(partition)):
            part = partition[i]
            bool_list = list(map(helper, part))
            if all(bool_list):
                res.append(part)

        return res