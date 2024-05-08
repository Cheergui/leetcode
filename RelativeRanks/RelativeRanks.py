class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        sorted_score = score[:]

        sorted_score.sort(reverse=True)

        hashmap = {}

        medal_map = {1:'Gold Medal', 2:'Silver Medal', 3:'Bronze Medal'}

        for i, s in enumerate(sorted_score):
            rank = i+1
            if rank in medal_map:
                hashmap[s] = medal_map[rank]
            else:
                hashmap[s] = str(rank)
        
        res = [hashmap[s] for s in score]

        return res