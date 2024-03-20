# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """

        # Dummy node to handle edge cases
        dummy_node = ListNode()
        dummy_node.next = list1

        # intialize index and current node
        index = -1
        curr = dummy_node

        # get the node before the first node to remove
        while index != a-1:
            curr = curr.next
            index += 1

        prev_list2 = curr


        # get the node after the last node to remove
        while index != b+1:
            curr = curr.next
            index += 1
        
        next_list2 = curr

        # get the tail of list2
        tmp = list2

        while tmp.next:
            tmp = tmp.next

        tail = tmp

        # link everything properly
        prev_list2.next = list2
        tail.next = next_list2
        
        return dummy_node.next