class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """


        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        curr = prev
        prev = None
        carry_over = 0

        while curr:
            new_val = (2*curr.val+carry_over) % 10
            carry_over = (2*curr.val+carry_over) // 10
            curr.val = new_val
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        head = prev

        if carry_over > 0:
            new_head = ListNode(val=carry_over)
            new_head.next = head
            head = new_head

        return head