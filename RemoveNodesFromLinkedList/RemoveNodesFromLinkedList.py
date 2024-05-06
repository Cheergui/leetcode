class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        stack = [head]

        curr = head.next

        while curr:
            while curr and stack and curr.val > stack[-1].val:
                stack.pop()
            stack.append(curr)
            if len(stack) > 1:
                stack[-2].next = stack[-1]
            curr = curr.next
        
        stack[-1].next = None

        res = stack[0]

        return res