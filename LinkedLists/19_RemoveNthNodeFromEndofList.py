# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Create a dummy node and point it to the head
        # This helps us handle edge cases like removing the head node
        dummy = ListNode(0, head)
        curr = head
        prev = None


        # Reverse the list
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp


        # remove nth node from teh front
        i = 1
        curr = tail = prev
        perv = None
        while curr:
            if i == n:
                prev.next = curr.next
                break
            
            i += 1
            prev = curr
            curr = curr.next

        curr = tail
        prev = None
        
        # Reverse the list again
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        
        return prev
                