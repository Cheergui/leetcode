class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if head.next == None:
            return None

        def reverse(head):

            prev, curr = None, head

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            return prev

        count = 1

        tail = reverse(head)

        curr = tail

        if n == 1:
            tail = tail.next
        else:
            while count != n-1:
                curr = curr.next
                count += 1

            curr.next = curr.next.next

        res = reverse(tail)

        return res