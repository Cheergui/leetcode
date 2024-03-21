class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev