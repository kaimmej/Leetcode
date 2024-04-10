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
