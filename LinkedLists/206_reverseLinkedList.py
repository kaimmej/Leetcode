# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        
        curr = head
        prev = None

        while curr:
            # print(curr)
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        head = prev
        # print(head)
        return head