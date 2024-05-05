class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        curr = node
        prev = None

        while curr.next:
            next = curr.next
            curr.val = next.val
            prev = curr
            curr = curr.next

        prev.next = None