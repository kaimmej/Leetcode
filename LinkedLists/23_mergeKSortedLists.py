# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """


        if not lists or len(lists) == 0:
            return None
        
        if len(lists) == 1: 
            return lists[0]

        
        head = lists[0]
        # skip the first list
        for i in range(1, len(lists)):
            head = self.mergeTwoLists(head, lists[i])

        return head
            



    def mergeTwoLists(self, l1, l2):
        
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
