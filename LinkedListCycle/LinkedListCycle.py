class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        curr = head
        visited = set()

        while curr != None and curr not in visited:
            visited.add(curr)
            curr = curr.next

        return not curr == None