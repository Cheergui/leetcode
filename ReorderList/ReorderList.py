from collections import deque

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        queue = deque()

        curr = head

        while curr:
            queue.append(curr)
            curr = curr.next

        i = 1
        
        curr = queue.popleft()

        res = curr

        while queue:
            if i % 2 == 0:
                tmp = queue.popleft()
                curr.next = tmp
                curr = tmp
            else:
                tmp = queue.pop()
                curr.next = tmp
                curr = tmp
            i += 1
        
        curr.next = None
        
        return res