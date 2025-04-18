# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode()
        tail = dummy

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        # are there still list-nodes to process? (For each?)
        while l1 and l2:

            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # broke out of the while loop... 
        # if there is any length in the other linked list, append it to the result.
        # this really just matters if list2 ran out of nodes first.
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2        

        dummy = dummy.next
        return dummy



#
#


        l1 = list1
        l2 = list2
        dummy = node = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next

            else:
                dummy.next = l2
                l2 = l2.next
            
            dummy = dummy.next
        
        dummy.next = l1 or l2

        # We need to keep track of the head. 
        return node.next

        # dummy = node = ListNode()

        # while list1 and list2:
        #     if list1.val < list2.val:
        #         node.next = list1
        #         list1 = list1.next
        #     else:
        #         node.next = list2
        #         list2 = list2.next
        #     node = node.next

        # node.next = list1 or list2