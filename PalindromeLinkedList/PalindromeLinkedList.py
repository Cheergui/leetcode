class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        left_to_right = []
        right_to_left = []

        prev, curr = None, head

        while curr:
            left_to_right.append(curr.val)
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        prev, curr = None, prev

        while curr:
            right_to_left.append(curr.val)
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return left_to_right == right_to_left