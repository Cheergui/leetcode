class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """

        n=len(heights)
        ans=[]
        for i in range(n-1):
            h=heights[i+1]-heights[i]
            if h<=0:
                continue
            heappush(ans,h)
            if len(ans)>ladders:
                min_h=heappop(ans)
                bricks-=min_h
            if bricks<0:
                return i
        return n-1    
        


            



        